/* CN 271: Universal Fluid Mechanics Calculator */
(function () {
  "use strict";
  var G = 9.81;
  var RHO = 1000.0;
  var GAMMA = 9810.0;

  var form = document.getElementById("calcform");
  if (!form) return;
  var out = document.getElementById("calcout");

  function fmt(x, d) {
    if (x === null || x === undefined || isNaN(x)) return "-";
    var n = Number(x);
    if (Math.abs(n) >= 1e6 || (Math.abs(n) < 1e-4 && Math.abs(n) > 0)) {
      return n.toExponential(d || 3);
    }
    return n.toPrecision(d || 4).replace(/(\.\d*?)0+$/, "$1").replace(/\.$/, "");
  }

  function val(name) {
    var el = form.elements[name];
    if (!el) return NaN;
    var v = parseFloat(el.value);
    return isNaN(v) ? 0 : v;
  }

  function colebrook(re, rr) {
    if (re < 2000) return 64 / re;
    var f = 0.02;
    for (var i = 0; i < 200; i++) {
      var n = Math.pow(-2 * Math.log10(rr / 3.7 + 2.51 / (re * Math.sqrt(f))), -2);
      if (Math.abs(n - f) < 1e-9) return n;
      f = n;
    }
    return f;
  }

  function table(head, rows) {
    var h = "<tr>" + head.map(function (c) { return "<th>" + c + "</th>"; }).join("") + "</tr>";
    var b = rows.map(function (r) {
      return "<tr>" + r.map(function (c) { return "<td>" + c + "</td>"; }).join("") + "</tr>";
    }).join("");
    return '<div class="tw"><table><thead>' + h + "</thead><tbody>" + b + "</tbody></table></div>";
  }

  function solve() {
    var mode = form.elements.mode.value;
    var resHtml = "", tableHead = ["พารามิเตอร์", "ค่าที่คำนวณได้", "หน่วย / คำอธิบาย"], tableRows = [];

    try {
      if (mode === "shear") {
        var mu = val("sh_mu"), V = val("sh_v"), hMm = val("sh_h"), A = val("sh_a");
        if (mu <= 0 || V <= 0 || hMm <= 0) throw new Error("กรุณากรอกความหนืด μ, ความเร็ว V และระยะ h เป็นตัวเลขบวก");
        var hM = hMm * 1e-3;
        var dudy = V / hM;
        var tau = mu * dudy;
        var F = (A > 0) ? tau * A : null;
        resHtml = "τ = " + fmt(tau, 4) + " N/m² (Pa)" + (F !== null ? ",  F = " + fmt(F, 4) + " N (เมื่อ A = " + A + " m²)" : "");
        tableRows = [
          ["ความหนืดไดนามิก (μ)", fmt(mu, 4), "Pa·s (N·s/m²)"],
          ["ความเร็ว (V)", fmt(V, 3), "m/s"],
          ["ระยะห่างระหว่างแผ่น (h)", fmt(hM, 4), "m  (" + fmt(hMm, 3) + " mm)"],
          ["ความลาดความเร็ว (dv/dy)", fmt(dudy, 4), "s⁻¹ (Linear Velocity Gradient)"],
          ["ความเค้นเฉือน (τ)", fmt(tau, 4), "N/m² (Pa)"],
          ["แรงเฉือนฉุดแผ่น (F)", F !== null ? fmt(F, 4) : "-", "N (เมื่อพื้นที่ A = " + fmt(A, 3) + " m²)"]
        ];
      } else if (mode === "mano") {
        var sg = val("mn_sg"), dh = val("mn_dh"), theta = val("mn_theta");
        if (sg <= 0 || dh < 0) throw new Error("กรุณากรอก SG และ Δh เป็นตัวเลขบวก");
        var rad = theta * Math.PI / 180;
        var vertH = (theta >= 90) ? dh : dh * Math.sin(rad);
        var gammaFluid = sg * GAMMA;
        var dp = gammaFluid * vertH;
        var dpKpa = dp / 1000;
        resHtml = "ΔP = " + fmt(dp, 4) + " Pa  (" + fmt(dpKpa, 4) + " kPa, " + fmt(vertH, 3) + " m ของของเหลว)";
        tableRows = [
          ["ความถ่วงจำเพาะ (SG)", fmt(sg, 3), "-"],
          ["น้ำหนักจำเพาะของเหลว (γ)", fmt(gammaFluid, 4), "N/m³"],
          ["ระยะแนวดิ่ง (Δh)", fmt(vertH, 4), "m (คำนวณจากมุม " + theta + "°)"],
          ["ผลต่างความดัน (ΔP)", fmt(dp, 4), "Pa (N/m²)"],
          ["ผลต่างความดัน (kPa)", fmt(dpKpa, 4), "kPa"]
        ];
      } else if (mode === "gate") {
        var gb = val("gt_b"), gh = val("gt_h"), ghw = val("gt_hw");
        if (gb <= 0 || gh <= 0) throw new Error("กรุณากรอกความกว้าง b และความสูง h ของผนังเป็นค่าบวก");
        var gArea = gb * gh;
        var hc = ghw + (gh / 2.0);
        var FR = GAMMA * hc * gArea;
        var Ic = (gb * Math.pow(gh, 3)) / 12.0;
        var ycp = hc + (Ic / (hc * gArea));
        var yFromBottom = (ghw + gh) - ycp;
        resHtml = "FR = " + fmt(FR / 1000, 4) + " kN,  y_cp = " + fmt(ycp, 4) + " m (จากผิวน้ำ, สูงจากก้น " + fmt(yFromBottom, 3) + " m)";
        tableRows = [
          ["พื้นที่รับแรง (A)", fmt(gArea, 4), "m² (กว้าง " + gb + " m × สูง " + gh + " m)"],
          ["ความลึกจุดศูนย์ถ่วง (hc)", fmt(hc, 4), "m (วัดจากผิวน้ำ)"],
          ["แรงดันน้ำลัพธ์ (FR)", fmt(FR / 1000, 4), "kN (" + fmt(FR, 5) + " N)"],
          ["โมเมนต์ความเฉื่อยรอบแกน C (Ic)", fmt(Ic, 4), "m⁴ (bh³/12)"],
          ["จุดศูนย์กลางแรงกด (y_cp)", fmt(ycp, 4), "m (วัดจากผิวน้ำ)"],
          ["ระยะสูงจากขอบล่างของผนัง", fmt(yFromBottom, 4), "m"]
        ];
      } else if (mode === "jet") {
        var jv = val("jt_v"), ja = val("jt_a"), ju = val("jt_u"), jTheta = val("jt_theta");
        if (jv <= 0 || ja <= 0) throw new Error("กรุณากรอกความเร็ว v และพื้นที่ A เป็นค่าบวก");
        var vr = jv - ju;
        if (vr <= 0) throw new Error("ความเร็วแผ่น u ต้องน้อยกว่าความเร็วลำน้ำ v");
        var mRel = RHO * ja * vr;
        var jRad = jTheta * Math.PI / 180;
        var Rx = mRel * vr * (1 - Math.cos(jRad));
        resHtml = "Rx = " + fmt(Rx / 1000, 4) + " kN (" + fmt(Rx, 5) + " N)";
        tableRows = [
          ["ความเร็วสัมพัทธ์ (vr = v - u)", fmt(vr, 3), "m/s (v = " + jv + ", u = " + ju + ")"],
          ["อัตราการไหลมวลปะทะ (ṁ_rel)", fmt(mRel, 4), "kg/s [ρ A (v - u)]"],
          ["มุมการหักเลี้ยวของลำน้ำ", jTheta, "องศา"],
          ["แรงดันสุทธิต่อแผ่น (Rx)", fmt(Rx / 1000, 4), "kN (" + fmt(Rx, 5) + " N)"]
        ];
      } else if (mode === "scale") {
        var scType = form.elements.sc_type.value;
        var scale = val("sc_scale"), vm = val("sc_vm");
        if (scale <= 1 || vm <= 0) throw new Error("กรุณากรอกอัตราส่วนสเกล N > 1 และความเร็วโมเดล vm > 0");
        if (scType === "froude") {
          var vpF = vm * Math.sqrt(scale);
          var qScaleF = Math.pow(scale, 2.5);
          resHtml = "[Froude Similitude] vp = " + fmt(vpF, 4) + " m/s (อัตราส่วนความเร็ว 1 : " + fmt(Math.sqrt(scale), 3) + ")";
          tableRows = [
            ["เกณฑ์แบบจำลอง", "Froude Number (Fr_m = Fr_p)", "ใช้กับผิวน้ำอิสระ แม่น้ำ เขื่อน"],
            ["อัตราส่วนความยาว (λL = Lm/Lp)", "1 : " + scale, "-"],
            ["ความเร็วในแม่น้ำจริง (vp)", fmt(vpF, 4), "m/s  (vm × √" + scale + ")"],
            ["อัตราส่วนอัตราการไหล (Qp/Qm)", fmt(qScaleF, 4), "เท่า  (λL^2.5)"]
          ];
        } else {
          var vpR = vm / scale;
          resHtml = "[Reynolds Similitude] vp = " + fmt(vpR, 4) + " m/s (กรณีของไหลชนิดเดียวกัน vm = vp × " + scale + ")";
          tableRows = [
            ["เกณฑ์แบบจำลอง", "Reynolds Number (Re_m = Re_p)", "ใช้กับท่อปิดเต็มท่อ อากาศยาน"],
            ["อัตราส่วนขนาด (λL = Dm/Dp)", "1 : " + scale, "-"],
            ["ความเร็วในท่อจริง (vp)", fmt(vpR, 4), "m/s  (vm / " + scale + ")"],
            ["ความเร็วที่ต้องใช้ทดสอบ (vm)", fmt(vm, 4), "m/s"]
          ];
        }
      } else if (mode === "v") {
        var H = val("H"), L = val("L"), D = val("D"), eps = val("eps") / 1000, K = val("K") || 0;
        var nu = val("nu") || 1e-6, fGuess = val("f0") || 0.02;
        var ex = form.elements.ex.checked ? 1.0 : 0.0;
        if (H <= 0 || L <= 0 || D <= 0) throw new Error("กรุณากรอก H, L และ D เป็นค่าบวก");
        tableHead = ["รอบที่", "f เดา", "v (m/s)", "Re", "ε/D", "f Colebrook", "สถานะ"];
        var iterRows = [], vFinal = 0;
        for (var i = 1; i <= 20; i++) {
          vFinal = Math.sqrt((2 * G * H) / (ex + K + (fGuess * L / D)));
          var re = (vFinal * D) / nu;
          var fn = colebrook(re, eps / D);
          var ok = Math.abs(fn - fGuess) < 0.00006;
          iterRows.push([i, fmt(fGuess, 4), fmt(vFinal, 4), fmt(re, 3), fmt(eps / D, 3), fmt(fn, 4), ok ? '<b style="color:var(--green)">ลู่เข้า (OK)</b>' : "คำนวณซ้ำ"]);
          if (ok) break;
          fGuess = fn;
        }
        var qFinal = vFinal * (Math.PI * D * D / 4.0);
        resHtml = "v = " + fmt(vFinal, 4) + " m/s,  Q = " + fmt(qFinal, 4) + " m³/s (" + fmt(qFinal * 1000, 3) + " L/s)";
        tableRows = iterRows;
      } else if (mode === "D") {
        var qD = val("Q"), hfD = val("hf"), lD = val("L_d"), epsD = val("eps_d") / 1000;
        var nuD = 1e-6, fGuessD = 0.02;
        if (qD <= 0 || hfD <= 0 || lD <= 0) throw new Error("กรุณากรอก Q, hf และ L เป็นค่าบวก");
        tableHead = ["รอบที่", "f เดา", "D (m)", "v (m/s)", "Re", "ε/D", "f Colebrook", "สถานะ"];
        var iterDRows = [], dFinal = 0;
        for (var j = 1; j <= 20; j++) {
          dFinal = Math.pow((8.0 * fGuessD * lD * qD * qD) / (Math.PI * Math.PI * G * hfD), 0.2);
          var vD = qD / (Math.PI * dFinal * dFinal / 4.0);
          var reD = (vD * dFinal) / nuD;
          var fnD = colebrook(reD, epsD / dFinal);
          var okD = Math.abs(fnD - fGuessD) < 0.00006;
          iterDRows.push([j, fmt(fGuessD, 4), fmt(dFinal, 4), fmt(vD, 4), fmt(reD, 3), fmt(epsD / dFinal, 3), fmt(fnD, 4), okD ? '<b style="color:var(--green)">ลู่เข้า (OK)</b>' : "คำนวณซ้ำ"]);
          if (okD) break;
          fGuessD = fnD;
        }
        resHtml = "D ≈ " + fmt(dFinal, 4) + " m (" + fmt(dFinal * 1000, 3) + " mm)";
        tableRows = iterDRows;
      } else if (mode === "venturi") {
        var cd = val("vt_cd"), d1 = val("vt_d1"), d2 = val("vt_d2"), dpV = val("vt_dp");
        if (cd <= 0 || d1 <= 0 || d2 <= 0 || dpV <= 0) throw new Error("กรุณากรอกข้อมูล Venturi ทุกช่องเป็นค่าบวก");
        if (d2 >= d1) throw new Error("ขนาดคอคอด d2 ต้องเล็กกว่าท่อหลัก d1");
        var a1 = Math.PI * d1 * d1 / 4.0;
        var a2 = Math.PI * d2 * d2 / 4.0;
        var dhV = dpV / GAMMA;
        var qVent = cd * ((a1 * a2) / Math.sqrt(Math.pow(a1, 2) - Math.pow(a2, 2))) * Math.sqrt(2 * G * dhV);
        resHtml = "Q = " + fmt(qVent, 4) + " m³/s (" + fmt(qVent * 1000, 3) + " L/s),  Δh = " + fmt(dhV * 100, 3) + " cm";
        tableRows = [
          ["พื้นที่ท่อหลัก (A1)", fmt(a1, 4), "m² (D1 = " + d1 + " m)"],
          ["พื้นที่คอคอด (A2)", fmt(a2, 4), "m² (D2 = " + d2 + " m)"],
          ["ผลต่างเฮดความดัน (Δh)", fmt(dhV, 4), "m ของน้ำ (" + fmt(dhV * 100, 3) + " cm)"],
          ["อัตราเร็วทฤษฎี √(2gΔh)", fmt(Math.sqrt(2 * G * dhV), 4), "m/s"],
          ["อัตราการไหลจริง (Q)", fmt(qVent, 4), "m³/s  (" + fmt(qVent * 1000, 3) + " L/s)"]
        ];
      } else if (mode === "cavitation") {
        var pAtmKpa = val("cv_patm"), pvPa = val("cv_pv"), npshr = val("cv_npshr");
        var qPump = val("cv_q"), dPump = val("cv_d"), klPump = val("cv_kl");
        if (pAtmKpa <= 0 || npshr <= 0 || qPump <= 0 || dPump <= 0) throw new Error("กรุณากรอกข้อมูลปั๊มเป็นค่าบวก");
        var hAtm = (pAtmKpa * 1000) / GAMMA;
        var hVapor = pvPa / GAMMA;
        var vPump = (4 * qPump) / (Math.PI * dPump * dPump);
        var vHead = Math.pow(vPump, 2) / (2 * G);
        var hLoss = klPump * vHead;
        var z1Max = (hAtm - hVapor) - npshr - hLoss - vHead;
        resHtml = "Z1,max = " + fmt(z1Max, 3) + " m (ระดับติดตั้งปั๊มสูงสุดเหนือผิวน้ำ)";
        tableRows = [
          ["เฮดความดันบรรยากาศ (Patm / γ)", fmt(hAtm, 4), "m (ที่ความดัน " + pAtmKpa + " kPa)"],
          ["เฮดความดันไอ (Pv / γ)", fmt(hVapor, 4), "m (ที่อุณหภูมิน้ำ)"],
          ["ความเร็วท่อดูด (v)", fmt(vPump, 4), "m/s"],
          ["เฮดความเร็ว (v²/2g)", fmt(vHead, 4), "m"],
          ["การสูญเสียในท่อดูด (hL = ΣKL v²/2g)", fmt(hLoss, 4), "m (ΣKL = " + klPump + ")"],
          ["เฮดดูดที่ปั๊มต้องการ (NPSHR)", fmt(npshr, 3), "m"],
          ["ระยะความสูงปลอดภัยสูงสุด (Z1,max)", fmt(z1Max, 4), "m (ป้องกันการเกิด Cavitation 100%)"]
        ];
      }

      out.innerHTML = '<p class="res">' + resHtml + "</p>" + table(tableHead, tableRows);
    } catch (e) {
      out.innerHTML = '<p class="err" style="color:var(--red);font-weight:700;">⚠️ ข้อผิดพลาด: ' + e.message + "</p>";
    }
  }

  function updateModeFields() {
    var mode = form.elements.mode.value;
    [].forEach.call(form.querySelectorAll("[data-m]"), function (el) {
      var modes = el.getAttribute("data-m").split(" ");
      el.hidden = modes.indexOf(mode) < 0;
    });
    out.innerHTML = "";
  }

  form.elements.mode.addEventListener("change", updateModeFields);
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    solve();
  });

  updateModeFields();
})();
