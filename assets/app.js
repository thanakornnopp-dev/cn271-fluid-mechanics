/* วย 271 บทที่ 5: เปลี่ยนแผ่น (hash route), สารบัญแผ่น, โหมดฝึก, ติ๊กทำแล้ว, KaTeX */
(function () {
  "use strict";

  var GROUPS = [
    ["start", "เริ่มที่นี่"],
    ["main", "ข้อสอบหลัก: ตัวอย่างข้อ 1–8"],
    ["exam", "โจทย์ 15 คะแนน แบบข้อสอบ"],
    ["extra", "เสริม: ข้อ 9–13 (นอกขอบเขตที่เพื่อนบอก)"],
    ["tools", "เครื่องมือ"]
  ];
  var SRC = {
    prof: ["เฉลยอาจารย์", "src-prof"],
    team: ["เฉลยทีม ตรวจด้วยโปรแกรม", "src-team"],
    gap: ["โจทย์ข้อมูลไม่ครบ", "src-gap"],
    sum: ["สรุปโดยทีม", "src-team"]
  };
  var store = {
    get: function (k, d) { try { var v = localStorage.getItem(k); return v === null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* private mode */ } }
  };

  var sheets = (window.SHEETS || []).slice().sort(function (a, b) { return a.order - b.order; });
  var main = document.getElementById("sheet");
  var indexEl = document.getElementById("index");
  var countEl = document.getElementById("count");
  var pnEl = document.getElementById("pn");
  var idxBtn = document.getElementById("idxbtn");
  var done = store.get("pf-done", {});
  var practice = store.get("pf-practice", false);
  var firstLoad = true;

  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function find(id) { for (var i = 0; i < sheets.length; i++) if (sheets[i].id === id) return i; return -1; }

  function buildIndex(current) {
    var html = "";
    GROUPS.forEach(function (g) {
      var items = sheets.filter(function (s) { return s.group === g[0]; });
      if (!items.length) return;
      html += "<h2>" + esc(g[1]) + "</h2><ul>";
      items.forEach(function (s) {
        var i = find(s.id);
        html += '<li><a href="#/' + s.id + '"' + (s.id === current ? ' aria-current="page"' : "") + ">" +
          '<span class="n">' + esc(s.idx || s.no || pad(i + 1)) + "</span><span>" + esc(s.title) +
          (s.sub ? "<small>" + esc(s.sub) + "</small>" : "") + "</span>" +
          '<span class="ok">' + (done[s.id] ? '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12.5l5 5L20 6.5"/></svg><span class="sr">ทำแล้ว</span>' : "") + "</span></a></li>";
      });
      html += "</ul>";
    });
    indexEl.innerHTML = html;
  }

  function given(list) {
    if (!list || !list.length) return "";
    return '<div class="given" role="list">' + list.map(function (g) {
      return '<div role="listitem"><small>' + g[0] + "</small><b>" + g[1] + "</b></div>";
    }).join("") + "</div>";
  }

  function sheetHTML(s, i) {
    var src = SRC[s.src] || SRC.team;
    var h = '<article class="sheet' + (practice && s.steps ? " practice" : "") + '" id="s-' + s.id + '">';
    h += '<header class="tb">' +
      '<div class="wide title"><b id="h1" tabindex="-1">' + s.title + "</b></div>" +
      "<div><small>ข้อ</small><b>" + (s.no || "–") + "</b></div>" +
      "<div><small>ประเภท</small><b>" + (s.type || "–") + "</b></div>" +
      '<div><label><input type="checkbox" id="chk"' + (done[s.id] ? " checked" : "") + '><b>ทำแล้ว</b></label></div>' +
      '<div class="src"><b><span class="src-tag ' + src[1] + '">' + src[0] + "</span></b></div>" +
      "</header>";
    if (s.steps) {
      h += '<p class="pens"><span class="pb">น้ำเงิน ให้/แทนค่า</span><span class="pr">แดง ผล/จุดดัก</span><span class="pv">ม่วง ตรวจ</span></p>';
    }
    if (s.ask) h += '<h2 class="sec"><span>โจทย์</span></h2><div class="ask">' + s.ask + "</div>";
    if (s.given) h += given(s.given);
    if (s.fig) h += '<figure class="fig">' + s.fig + (s.cap ? "<figcaption>" + s.cap + "</figcaption>" : "") + "</figure>";
    if (s.html) h += s.html;
    if (s.steps) {
      h += '<h2 class="sec"><span>วิธีทำ</span><span class="practice-toggle"><button type="button" id="ptog" aria-pressed="' + practice + '">โหมดฝึก: ซ่อนวิธีทำ</button></span></h2><ol class="steps">';
      s.steps.forEach(function (st) {
        h += '<li class="tone-' + (st[2] || "") + '"><button type="button" class="st" aria-expanded="true">' + st[0] + '</button><div class="body">' + st[1] + "</div></li>";
      });
      h += "</ol>";
    }
    if (s.answer) h += '<section class="answer"><b>คำตอบ</b>' + s.answer + "</section>";
    if (s.revs && s.revs.length) {
      h += '<h2 class="sec"><span>REVISION: จุดที่มักพลาดในข้อนี้</span></h2><div class="tbl-wrap"><table class="rev"><thead><tr><th>REV</th><th>จุดดัก</th><th>ถ้าพลาดจะเป็นอย่างไร</th></tr></thead><tbody>' +
        s.revs.map(function (r, k) { return "<tr><td>" + "ABCDEFG".charAt(k) + "</td><td>" + r[0] + "</td><td>" + r[1] + "</td></tr>"; }).join("") +
        "</tbody></table></div>";
    }
    if (s.srcNote) h += '<p class="n src-note">ที่มา: ' + s.srcNote + "</p>";
    h += "</article>";
    return h;
  }

  function nav(i) {
    var p = sheets[i - 1], n = sheets[i + 1];
    pnEl.innerHTML =
      (p ? '<a href="#/' + p.id + '" rel="prev"><small><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>ก่อนหน้า</small><b>' + esc(p.no || p.title) + "</b></a>" : "<span></span>") +
      (n ? '<a href="#/' + n.id + '" rel="next"><small>ถัดไป<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></small><b>' + esc(n.no || n.title) + "</b></a>" : "<span></span>");
  }

  function math(el) {
    if (window.renderMathInElement) {
      window.renderMathInElement(el, {
        delimiters: [{ left: "$$", right: "$$", display: true }, { left: "\\(", right: "\\)", display: false }],
        throwOnError: false
      });
    }
  }

  function show() {
    var id = (location.hash.match(/^#\/([\w-]+)/) || [])[1] || sheets[0].id;
    var i = find(id);
    if (i < 0) { i = 0; id = sheets[0].id; }
    var s = sheets[i];
    main.innerHTML = sheetHTML(s, i);
    document.title = (s.no ? s.no + " · " : "") + s.title.replace(/<[^>]+>/g, "") + " · วย 271 บท 5";
    countEl.textContent = pad(i + 1) + " / " + pad(sheets.length);
    buildIndex(id);
    nav(i);
    indexEl.classList.remove("open");
    idxBtn.setAttribute("aria-expanded", "false");
    window.scrollTo(0, 0);
    math(main);
    if (s.init) s.init(main);

    var chk = main.querySelector("#chk");
    chk.addEventListener("change", function () { done[id] = chk.checked; store.set("pf-done", done); buildIndex(id); });
    var tog = main.querySelector("#ptog");
    function sync() {
      main.querySelectorAll("ol.steps > li").forEach(function (li) {
        li.querySelector(".st").setAttribute("aria-expanded", String(!practice || li.classList.contains("open")));
      });
    }
    if (tog) tog.addEventListener("click", function () {
      practice = !practice; store.set("pf-practice", practice);
      tog.setAttribute("aria-pressed", practice);
      main.querySelector(".sheet").classList.toggle("practice", practice);
      sync();
    });
    main.querySelectorAll("ol.steps > li > .st").forEach(function (st) {
      st.addEventListener("click", function () { if (practice) { st.parentNode.classList.toggle("open"); sync(); } });
    });
    sync();
    var h1 = main.querySelector("#h1");
    if (h1 && !firstLoad) h1.focus({ preventScroll: true });
    firstLoad = false;
  }

  if ("serviceWorker" in navigator && /^https?:/.test(location.protocol)) {
    window.addEventListener("load", function () { navigator.serviceWorker.register("sw.js").catch(function () {}); });
  }
  idxBtn.addEventListener("click", function () {
    var open = indexEl.classList.toggle("open");
    idxBtn.setAttribute("aria-expanded", open);
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") indexEl.classList.remove("open");
    if (e.target.matches("input, select, textarea")) return;
    var i = find((location.hash.match(/^#\/([\w-]+)/) || [])[1] || sheets[0].id);
    if (e.key === "ArrowRight" && sheets[i + 1]) location.hash = "#/" + sheets[i + 1].id;
    if (e.key === "ArrowLeft" && sheets[i - 1]) location.hash = "#/" + sheets[i - 1].id;
  });
  window.addEventListener("hashchange", show);
  window.addEventListener("load", function () { math(main); });
  show();
})();
