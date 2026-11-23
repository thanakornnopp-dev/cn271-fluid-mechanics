/* CN 271: สลับหน้าตาม URL hash, เรนเดอร์ KaTeX เมื่อเปิดหน้า, สลับโหมดมืด/สว่าง, โหมดฝึกซ่อนเฉลยวิธีทำ */
(function () {
  "use strict";
  var root = document.documentElement;
  var secs = [].slice.call(document.querySelectorAll("main > section"));
  var links = [].slice.call(document.querySelectorAll("nav.toc a"));
  var done = {};
  var opts = {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\(", right: "\\)", display: false },
      { left: "\\[", right: "\\]", display: true }
    ],
    throwOnError: false,
    trust: true
  };

  function store(k, v) {
    try {
      if (v === undefined) return localStorage.getItem(k);
      localStorage.setItem(k, v);
    } catch (e) {
      return null;
    }
  }

  function render(el) {
    if (!el || done[el.id] || typeof renderMathInElement !== "function") return;
    renderMathInElement(el, opts);
    done[el.id] = true;
  }

  function show() {
    var id = decodeURIComponent((location.hash || "").slice(1));
    var target = id ? document.getElementById(id) : null;
    var sec = target ? target.closest("main > section") : null;
    if (!sec) {
      sec = document.getElementById("sum") || secs[0];
      target = null;
    }
    secs.forEach(function (s) {
      s.classList.toggle("on", s === sec);
    });
    links.forEach(function (a) {
      if (a.getAttribute("href") === "#" + sec.id) {
        a.setAttribute("aria-current", "page");
      } else {
        a.removeAttribute("aria-current");
      }
    });
    render(sec);

    var h = sec.querySelector("h1, h2");
    if (h) {
      var titleText = h.textContent.replace(/\s+/g, " ").trim();
      document.title = titleText + " · CN 271 กลศาสตร์ของไหล มหาวิทยาลัยธรรมศาสตร์";
    }

    if (target && target !== sec) {
      target.scrollIntoView({ behavior: "smooth" });
    } else {
      window.scrollTo(0, 0);
    }

    var cur = document.querySelector('nav.toc a[aria-current="page"]');
    if (cur && cur.scrollIntoView) {
      cur.scrollIntoView({ block: "nearest", inline: "center" });
    }
  }

  /* จัดการธีม สว่าง / มืด */
  var themeBtn = document.getElementById("theme");
  var themeLbl = document.getElementById("thl");
  function updateThemeLabel() {
    if (themeLbl) {
      themeLbl.textContent = root.getAttribute("data-theme") === "dark" ? "โหมดสว่าง" : "โหมดมืด";
    }
  }
  updateThemeLabel();
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store("theme", next);
      updateThemeLabel();
    });
  }
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", function (e) {
    if (!store("theme")) {
      root.setAttribute("data-theme", e.matches ? "dark" : "light");
      updateThemeLabel();
    }
  });

  /* โหมดฝึก: ซ่อนขั้นตอนของเฉลยวิธีทำ (.exam .row) แตะเพื่อดูทีละขั้น */
  var pracBtn = document.getElementById("practice");
  function setPractice(on) {
    document.body.classList.toggle("practice", on);
    if (pracBtn) pracBtn.setAttribute("aria-pressed", on ? "true" : "false");
    [].forEach.call(document.querySelectorAll(".exam .row.shown"), function (r) {
      r.classList.remove("shown");
    });
    store("practice_cn271", on ? "1" : "0");
  }
  if (pracBtn) {
    pracBtn.addEventListener("click", function () {
      setPractice(!document.body.classList.contains("practice"));
    });
  }
  document.addEventListener("click", function (e) {
    if (!document.body.classList.contains("practice")) return;
    var r = e.target.closest && e.target.closest(".exam .row");
    if (r) r.classList.add("shown");
  });
  if (store("practice_cn271") === "1") {
    setPractice(true);
  }

  /* สลับแท็บในหน้าข้อสอบ (Forecast vs Step-by-Step) */
  window.switchExamTab = function (tab) {
    var forecastSec = document.getElementById("exam-tab-forecast");
    var stepSec = document.getElementById("exam-tab-step");
    var btnForecast = document.getElementById("btn-tab-forecast");
    var btnStep = document.getElementById("btn-tab-step");

    if (tab === "forecast") {
      if (forecastSec) forecastSec.style.display = "block";
      if (stepSec) stepSec.style.display = "none";
      if (btnForecast) btnForecast.classList.add("active");
      if (btnStep) btnStep.classList.remove("active");
    } else {
      if (forecastSec) forecastSec.style.display = "none";
      if (stepSec) stepSec.style.display = "block";
      if (btnForecast) btnForecast.classList.remove("active");
      if (btnStep) btnStep.classList.add("active");
    }
  };

  /* สั่งพิมพ์: เรนเดอร์สูตรครบทุกหน้าก่อนพิมพ์ */
  window.addEventListener("beforeprint", function () {
    secs.forEach(render);
  });

  window.addEventListener("hashchange", show);

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(show, 50);
    });
  } else {
    setTimeout(show, 50);
  }
})();
