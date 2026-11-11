/* สลับหน้า (hash), เรนเดอร์สูตรเมื่อเปิดหน้า, โหมดสว่าง/มืด, โหมดฝึก */
(function () {
  "use strict";
  var root = document.documentElement;
  var secs = [].slice.call(document.querySelectorAll("main > section"));
  var links = [].slice.call(document.querySelectorAll("nav.toc a"));
  var done = {};
  var opts = {
    delimiters: [{ left: "$$", right: "$$", display: true }, { left: "\\(", right: "\\)", display: false }],
    throwOnError: false,
    trust: true
  };

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  function render(el) {
    if (done[el.id] || typeof renderMathInElement !== "function") return;
    renderMathInElement(el, opts);
    done[el.id] = true;
  }

  function show() {
    var id = decodeURIComponent((location.hash || "").slice(1));
    var target = id ? document.getElementById(id) : null;
    var sec = target ? target.closest("main > section") : null;
    if (!sec) { sec = document.getElementById("sum"); target = null; }
    secs.forEach(function (s) { s.classList.toggle("on", s === sec); });
    links.forEach(function (a) {
      if (a.getAttribute("href") === "#" + sec.id) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    });
    render(sec);
    var h = sec.querySelector("h2");
    if (h) { h = h.cloneNode(true); [].forEach.call(h.querySelectorAll(".tag,.star"), function (x) { x.remove(); }); }
    document.title = (h ? h.textContent.replace(/\s+/g, " ").trim() + " · " : "") + "วย 271 บทที่ 5";
    if (target && target !== sec) target.scrollIntoView(); else window.scrollTo(0, 0);
    var cur = document.querySelector('nav.toc a[aria-current="page"]');
    if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: "nearest", inline: "center" });
  }

  /* ธีม */
  var themeBtn = document.getElementById("theme"), themeLbl = document.getElementById("thl");
  function themeLabel() { themeLbl.textContent = root.getAttribute("data-theme") === "dark" ? "โหมดสว่าง" : "โหมดมืด"; }
  themeLabel();
  themeBtn.addEventListener("click", function () {
    var n = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", n); store("theme", n); themeLabel();
  });
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
    if (!store("theme")) { root.setAttribute("data-theme", e.matches ? "dark" : "light"); themeLabel(); }
  });

  /* โหมดฝึก: ซ่อนขั้นตอนของเฉลยวิธีทำ แตะทีละขั้น */
  var pracBtn = document.getElementById("practice");
  function setPractice(on) {
    document.body.classList.toggle("practice", on);
    pracBtn.setAttribute("aria-pressed", on ? "true" : "false");
    [].forEach.call(document.querySelectorAll(".exam .row.shown"), function (r) { r.classList.remove("shown"); });
    store("practice", on ? "1" : "0");
  }
  pracBtn.addEventListener("click", function () { setPractice(!document.body.classList.contains("practice")); });
  document.addEventListener("click", function (e) {
    if (!document.body.classList.contains("practice")) return;
    var r = e.target.closest && e.target.closest(".exam .row");
    if (r) r.classList.add("shown");
  });
  if (store("practice") === "1") setPractice(true);

  /* พิมพ์: เรนเดอร์ทุกหน้า */
  window.addEventListener("beforeprint", function () { secs.forEach(render); });

  window.addEventListener("hashchange", show);
  show();

  if ("serviceWorker" in navigator && /^https?:$/.test(location.protocol)) {
    navigator.serviceWorker.register("sw.js").catch(function () {});
  }
})();
