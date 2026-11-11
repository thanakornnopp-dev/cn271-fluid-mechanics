/* เครื่องมือ: เครื่องคิดเลข trial and error และตารางอ้างอิง */
(function () {
  var R = String.raw;
  var P = function (o) { (window.SHEETS = window.SHEETS || []).push(o); };
  var G = 9.81;

  function colebrook(re, rr) {
    if (re < 2000) return 64 / re;
    var f = 0.02;
    for (var i = 0; i < 200; i++) {
      var n = Math.pow(-2 * Math.log10(rr / 3.7 + 2.51 / (re * Math.sqrt(f))), -2);
      if (Math.abs(n - f) < 1e-12) return n;
      f = n;
    }
    return f;
  }
  function fmt(x, d) { return Number(x).toPrecision(d || 4).replace(/\.?0+$/, function (m) { return m.indexOf("e") >= 0 ? m : ""; }); }
  function num(root, id) { return parseFloat(root.querySelector("#" + id).value); }

  function solve(root) {
    var out = root.querySelector("#out");
    var mode = root.querySelector("#mode").value;
    var L = num(root, "L"), eps = num(root, "eps") / 1000, nu = num(root, "nu"), f = num(root, "f0");
    var rows = "", res = "", err = "";
    try {
      if (!(L > 0 && eps >= 0 && nu > 0 && f > 0)) throw new Error("กรอกค่า L, ε, ν, f เริ่มต้น ให้เป็นตัวเลขบวก");
      if (mode === "v") {
        var H = num(root, "H"), D = num(root, "D"), K = num(root, "K") || 0, ex = root.querySelector("#ex").checked ? 1 : 0, v = 0;
        if (!(H > 0 && D > 0)) throw new Error("กรอก H และ D ให้เป็นตัวเลขบวก");
        for (var i = 1; i <= 15; i++) {
          v = Math.sqrt(2 * G * H / (ex + K + f * L / D));
          var re = v * D / nu, fn = colebrook(re, eps / D), ok = Math.abs(fn - f) < 0.00006;
          rows += "<tr><td>" + i + '</td><td class="num">' + fmt(f, 4) + '</td><td class="num">' + fmt(v, 4) + '</td><td class="num">' + fmt(re, 3) + '</td><td class="num">' + fmt(eps / D, 3) + '</td><td class="num">' + fmt(fn, 4) + "</td><td>" + (ok ? '<b class="pr">OK</b>' : "No") + "</td></tr>";
          if (ok) break; f = fn;
        }
        res = "v ≈ " + fmt(v, 3) + " m/s   Q ≈ " + fmt(v * Math.PI * D * D / 4, 3) + " m³/s";
        rows = "<table><thead><tr><th>รอบ</th><th>f เดา</th><th>v (m/s)</th><th>Re</th><th>ε/D</th><th>f Colebrook</th><th>ผล</th></tr></thead><tbody>" + rows + "</tbody></table>";
      } else if (mode === "D") {
        var Q = num(root, "Q"), h = num(root, "h"), D2 = 0;
        if (!(Q > 0 && h > 0)) throw new Error("กรอก Q และ h_f ให้เป็นตัวเลขบวก");
        for (var j = 1; j <= 15; j++) {
          D2 = Math.pow(8 * f * L * Q * Q / (Math.PI * Math.PI * G * h), 0.2);
          var v2 = Q / (Math.PI * D2 * D2 / 4), re2 = v2 * D2 / nu, fn2 = colebrook(re2, eps / D2), ok2 = Math.abs(fn2 - f) < 0.00006;
          rows += "<tr><td>" + j + '</td><td class="num">' + fmt(f, 4) + '</td><td class="num">' + fmt(D2, 4) + '</td><td class="num">' + fmt(v2, 4) + '</td><td class="num">' + fmt(re2, 3) + '</td><td class="num">' + fmt(eps / D2, 3) + '</td><td class="num">' + fmt(fn2, 4) + "</td><td>" + (ok2 ? '<b class="pr">OK</b>' : "No") + "</td></tr>";
          if (ok2) break; f = fn2;
        }
        res = "D ≈ " + fmt(D2, 3) + " m (" + fmt(D2 * 1000, 3) + " mm)";
        rows = "<table><thead><tr><th>รอบ</th><th>f เดา</th><th>D (m)</th><th>v (m/s)</th><th>Re</th><th>ε/D</th><th>f Colebrook</th><th>ผล</th></tr></thead><tbody>" + rows + "</tbody></table>";
      } else {
        var Q3 = num(root, "Q"), D3 = num(root, "D"), K3 = num(root, "K") || 0;
        if (!(Q3 > 0 && D3 > 0)) throw new Error("กรอก Q และ D ให้เป็นตัวเลขบวก");
        var v3 = Q3 / (Math.PI * D3 * D3 / 4), re3 = v3 * D3 / nu, f3 = colebrook(re3, eps / D3);
        var hf = f3 * L / D3 * v3 * v3 / (2 * G), hm = K3 * v3 * v3 / (2 * G);
        res = "h_f = " + fmt(hf, 4) + " m   h_m = " + fmt(hm, 3) + " m   รวม " + fmt(hf + hm, 4) + " m";
        rows = "<table><tbody><tr><td>v</td><td class=\"num\">" + fmt(v3, 4) + " m/s</td></tr><tr><td>Re</td><td class=\"num\">" + fmt(re3, 4) + "</td></tr><tr><td>ε/D</td><td class=\"num\">" + fmt(eps / D3, 3) + "</td></tr><tr><td>f (Colebrook)</td><td class=\"num\">" + fmt(f3, 4) + "</td></tr></tbody></table>";
      }
    } catch (e) { err = e.message; }
    out.innerHTML = err ? '<p class="err">' + err + "</p>" : '<p class="res">' + res + '</p><div class="tbl-wrap">' + rows + "</div>";
  }

  function fields(root) {
    var mode = root.querySelector("#mode").value;
    root.querySelectorAll("[data-m]").forEach(function (el) {
      el.hidden = el.getAttribute("data-m").split(" ").indexOf(mode) < 0;
    });
  }

  P({
    id: "calc", idx: "คิดเลข", order: 40, group: "tools", no: "เครื่องมือ", type: "Trial and error", src: "sum",
    title: "เครื่องคิดเลข เดา f แล้ววนจนลู่เข้า",
    sub: "ใช้ตรวจคำตอบที่ทำมือ",
    srcNote: "ใช้ Colebrook-White แทนการอ่านชาร์ต",
    html: R`<p>ใช้ตรวจคำตอบตัวเอง ไม่ใช่แทนการเขียนวิธีทำ ตารางแต่ละรอบหน้าตาเหมือนที่ต้องเขียนในข้อสอบ ค่า f ต่างจากชาร์ตได้เล็กน้อย</p>
<form class="calc" id="form" onsubmit="return false">
<div class="full"><label>โจทย์แบบไหน<select id="mode"><option value="v">Type 2 · หา v (รู้ H = ผลต่างพลังงานที่ใช้ได้)</option><option value="D">Type 3 · หา D (รู้ Q, h_f)</option><option value="h">Type 1 · หา h_f (รู้ Q, D)</option></select></label></div>
<div data-m="v"><label>H ที่ใช้ได้ (m)<input id="H" inputmode="decimal" value="5"></label></div>
<div data-m="D h"><label>Q (m³/s)<input id="Q" inputmode="decimal" value="0.5"></label></div>
<div data-m="D"><label>h_f (m)<input id="h" inputmode="decimal" value="10"></label></div>
<div data-m="v h"><label>D (m)<input id="D" inputmode="decimal" value="0.15"></label></div>
<div><label>L (m)<input id="L" inputmode="decimal" value="100"></label></div>
<div><label>ε (mm)<input id="eps" inputmode="decimal" value="0.12"></label></div>
<div data-m="v h"><label>ΣK<input id="K" inputmode="decimal" value="1.6"></label></div>
<div><label>ν (m²/s)<input id="nu" inputmode="decimal" value="0.000001"></label></div>
<div><label>f เดารอบแรก<input id="f0" inputmode="decimal" value="0.02"></label></div>
<div class="full check" data-m="v"><label><input type="checkbox" id="ex" checked> ปลายท่อปล่อยสู่อากาศ (มีเทอม v²/2g ที่ปลายท่อ)</label></div>
<div class="full"><button class="run" type="button" id="run">คำนวณ</button></div>
</form>
<div class="out" id="out" aria-live="polite"></div>
<div class="note hint"><b>ลองกับข้อ 7</b><p>ค่าเริ่มต้นในฟอร์มคือข้อ 7: H = 5, D = 0.15, L = 100, ε = 0.12, ΣK = 1.6, ปลายท่อสู่อากาศ → v ≈ 2.51 m/s. ข้อ 6: H = 3, L = 700, ΣK = 0 และไม่ติ๊กช่องปลายท่อ → 0.77 m/s. ข้อ 8: เลือก Type 3, Q = 0.5, h_f = 10, L = 200 → D ≈ 0.365 m</p></div>`,
    init: function (root) {
      root.querySelector("#mode").addEventListener("change", function () { fields(root); root.querySelector("#out").innerHTML = ""; });
      root.querySelector("#run").addEventListener("click", function () { solve(root); });
      fields(root); solve(root);
    }
  });

  P({
    id: "ref", idx: "ตาราง", order: 41, group: "tools", no: "อ้างอิง", type: "ตาราง", src: "sum",
    title: "ตารางอ้างอิง: ศัพท์ ค่าคงที่ และวิธีอ่านชาร์ต",
    sub: "ศัพท์ไทย–อังกฤษ, หน่วย, อ่านชาร์ต Glasgow",
    srcNote: "สไลด์ ch5",
    html: R`
<h2 class="sec"><span>วิธีอ่านชาร์ต Glasgow / Moody</span></h2>
<ol>
<li>คำนวณ \(Re=vD/\nu\) แล้วหาแกนนอน (log) ของชาร์ต</li>
<li>คำนวณ \(\varepsilon/D\) <span class="pr">หน่วยเดียวกัน</span> แล้วเลือกเส้นโค้งที่มีค่านั้น (ป้ายอยู่ทางขวาของชาร์ต) ถ้าอยู่ระหว่างเส้น ให้ประมาณตามสัดส่วน</li>
<li>ลากแนวตั้งจาก \(Re\) ไปชนเส้นโค้ง แล้วลากแนวนอนไปแกนตั้งอ่านค่า \(f\)</li>
<li>\(Re<2000\): ใช้เส้นตรง Laminar \(f=64/Re\) โดยไม่ดู \(\varepsilon/D\) · \(2000\text{–}4000\) ช่วง Critical/Transition ไม่น่าเชื่อถือ · เส้นโค้งขนานแกนนอนทางขวาคือโซน fully turbulent</li>
</ol>
<h2 class="sec"><span>ศัพท์ไทย–อังกฤษ</span></h2>
<div class="tbl-wrap"><table><thead><tr><th>English</th><th>ไทย</th></tr></thead><tbody>
<tr><td>Major loss \(h_f\)</td><td>การสูญเสียพลังงานหลัก (แรงเสียดทานตามความยาวท่อ)</td></tr>
<tr><td>Minor loss \(h_m\)</td><td>การสูญเสียพลังงานรอง (ข้องอ ขยาย หด ลิ้น ทางเข้า/ออก)</td></tr>
<tr><td>Friction factor \(f\)</td><td>สัมประสิทธิ์ความเสียดทาน (Darcy)</td></tr>
<tr><td>Relative roughness \(\varepsilon/D\)</td><td>ความขรุขระสัมพัทธ์</td></tr>
<tr><td>Reynolds number</td><td>เลขเรย์โนลด์ส</td></tr>
<tr><td>Laminar / Transitional / Turbulent</td><td>ราบเรียบ / ช่วงเปลี่ยน / ปั่นป่วน</td></tr>
<tr><td>Dynamic viscosity \(\mu\) · Kinematic \(\nu\)</td><td>ความหนืดสัมบูรณ์ · ความหนืดจลน์ (\(\nu=\mu/\rho\))</td></tr>
<tr><td>Energy equation</td><td>สมการพลังงาน</td></tr>
<tr><td>Pressure / Velocity / Elevation head</td><td>เฮดความดัน / เฮดความเร็ว / เฮดระดับ</td></tr>
<tr><td>Series / Parallel pipes</td><td>ท่อต่ออนุกรม / ต่อขนาน</td></tr>
<tr><td>Sudden expansion / contraction</td><td>ท่อขยาย / หดกะทันหัน</td></tr>
</tbody></table></div>
<h2 class="sec"><span>ค่าคงที่และการแปลงหน่วย</span></h2>
<div class="tbl-wrap"><table><thead><tr><th>ค่า</th><th>ใช้</th></tr></thead><tbody>
<tr><td>น้ำ \(\rho=1000\ \text{kg/m}^3\), \(\gamma=9810\ \text{N/m}^3\), \(g=9.81\ \text{m/s}^2\)</td><td>ทุกข้อ</td></tr>
<tr><td>\(\nu=10^{-6}\ \text{m}^2/\text{s}\), \(\mu=10^{-3}\ \text{N·s/m}^2\)</td><td>น้ำที่ ~20 °C (ข้อ 1, 2, 4 ให้ μ)</td></tr>
<tr><td>1 kPa = 1000 Pa · 1 mm = 10⁻³ m · 1 cm = 10⁻² m</td><td>แปลงก่อนแทนค่า</td></tr>
<tr><td>\(A=\pi D^2/4\) · \(Q=vA\)</td><td>ความต่อเนื่อง</td></tr>
</tbody></table></div>`
  });
})();
