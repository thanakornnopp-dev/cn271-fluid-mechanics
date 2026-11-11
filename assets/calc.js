/* เครื่องคิดเลข: เดา f แล้ววนจนลู่เข้า (Colebrook-White) ตัวเดียวกับ scripts/pipeflow.py */
(function () {
  "use strict";
  var G = 9.81;
  var form = document.getElementById("calcform");
  if (!form) return;
  var out = document.getElementById("calcout");

  function colebrook(re, rr) {
    if (re < 2000) return 64 / re;
    var f = 0.02;
    for (var i = 0; i < 300; i++) {
      var n = Math.pow(-2 * Math.log10(rr / 3.7 + 2.51 / (re * Math.sqrt(f))), -2);
      if (Math.abs(n - f) < 1e-12) return n;
      f = n;
    }
    return f;
  }
  function fmt(x, d) {
    var s = Number(x).toPrecision(d || 4);
    return s.indexOf("e") >= 0 ? s : s.replace(/(\.\d*?)0+$/, "$1").replace(/\.$/, "");
  }
  function val(name) { return parseFloat(form.elements[name].value); }
  function row(cells) { return "<tr>" + cells.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>"; }
  function verdict(ok) { return ok ? '<b class="ok">OK</b>' : "No"; }
  function table(head, body) {
    return '<div class="tw"><table><thead><tr>' + head.map(function (h) { return "<th>" + h + "</th>"; }).join("") + "</tr></thead><tbody>" + body + "</tbody></table></div>";
  }

  function solve() {
    var mode = form.elements.mode.value;
    var L = val("L"), eps = val("eps") / 1000, nu = val("nu"), f = val("f0");
    var rows = "", res = "", head;
    try {
      if (!(L > 0 && eps >= 0 && nu > 0 && f > 0)) throw new Error("กรอก L, ε, ν และ f เริ่มต้น เป็นตัวเลขบวก");
      if (mode === "v") {
        var H = val("H"), D = val("D"), K = val("K") || 0, ex = form.elements.ex.checked ? 1 : 0, v = 0;
        if (!(H > 0 && D > 0)) throw new Error("กรอก H และ D เป็นตัวเลขบวก");
        for (var i = 1; i <= 20; i++) {
          v = Math.sqrt(2 * G * H / (ex + K + f * L / D));
          var re = v * D / nu, fn = colebrook(re, eps / D), ok = Math.abs(fn - f) < 0.00006;
          rows += row([i, fmt(f, 4), fmt(v, 4), fmt(re, 3), fmt(eps / D, 3), fmt(fn, 4), verdict(ok)]);
          if (ok) break;
          f = fn;
        }
        res = "v ≈ " + fmt(v, 3) + " m/s,  Q ≈ " + fmt(v * Math.PI * D * D / 4, 3) + " m³/s";
        head = ["รอบ", "f เดา", "v (m/s)", "Re", "ε/D", "f Colebrook", "ผล"];
      } else if (mode === "D") {
        var Q = val("Q"), h = val("hf"), D2 = 0;
        if (!(Q > 0 && h > 0)) throw new Error("กรอก Q และ h_f เป็นตัวเลขบวก");
        for (var j = 1; j <= 20; j++) {
          D2 = Math.pow(8 * f * L * Q * Q / (Math.PI * Math.PI * G * h), 0.2);
          var v2 = Q / (Math.PI * D2 * D2 / 4), re2 = v2 * D2 / nu, fn2 = colebrook(re2, eps / D2), ok2 = Math.abs(fn2 - f) < 0.00006;
          rows += row([j, fmt(f, 4), fmt(D2, 4), fmt(v2, 4), fmt(re2, 3), fmt(eps / D2, 3), fmt(fn2, 4), verdict(ok2)]);
          if (ok2) break;
          f = fn2;
        }
        res = "D ≈ " + fmt(D2, 3) + " m (" + fmt(D2 * 1000, 3) + " mm)";
        head = ["รอบ", "f เดา", "D (m)", "v (m/s)", "Re", "ε/D", "f Colebrook", "ผล"];
      } else {
        var Q3 = val("Q"), D3 = val("D"), K3 = val("K") || 0;
        if (!(Q3 > 0 && D3 > 0)) throw new Error("กรอก Q และ D เป็นตัวเลขบวก");
        var v3 = Q3 / (Math.PI * D3 * D3 / 4), re3 = v3 * D3 / nu, f3 = colebrook(re3, eps / D3);
        var hf = f3 * L / D3 * v3 * v3 / (2 * G), hm = K3 * v3 * v3 / (2 * G);
        res = "h_f ≈ " + fmt(hf, 4) + " m,  h_m ≈ " + fmt(hm, 3) + " m,  รวม " + fmt(hf + hm, 4) + " m";
        rows = row(["v", fmt(v3, 4) + " m/s"]) + row(["Re", fmt(re3, 4)]) + row(["ε/D", fmt(eps / D3, 3)]) + row(["f (Colebrook)", fmt(f3, 4)]);
        head = ["ค่า", "ผล"];
      }
      out.innerHTML = '<p class="res">' + res + "</p>" + table(head, rows);
    } catch (e) {
      out.innerHTML = '<p class="err"></p>';
      out.firstChild.textContent = e.message;
    }
  }

  function fields() {
    var mode = form.elements.mode.value;
    [].forEach.call(form.querySelectorAll("[data-m]"), function (el) {
      el.hidden = el.getAttribute("data-m").split(" ").indexOf(mode) < 0;
    });
  }

  form.elements.mode.addEventListener("change", function () { fields(); out.innerHTML = ""; });
  document.getElementById("calcrun").addEventListener("click", solve);
  form.addEventListener("keydown", function (e) { if (e.key === "Enter") solve(); });
  fields();
  solve();
})();
