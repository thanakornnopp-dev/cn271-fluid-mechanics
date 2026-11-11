/* แผ่นที่ 1: สรุปวิธีทำหน้าเดียว */
(function () {
  var R = String.raw;
  (window.SHEETS = window.SHEETS || []).push({
    id: "cheat", order: 0, group: "start", no: "สรุป", type: "สรุปวิธีทำ", src: "sum",
    title: "สรุปวิธีทำ หน้าเดียว",
    sub: "เลือกประเภทโจทย์ + สมการ + ลำดับเขียนในห้องสอบ",
    srcNote: "สไลด์ ch5 + เฉลยอาจารย์",
    html: R`
<h2 class="sec"><span>1 · ดูโจทย์แล้วจัดเป็นประเภทไหน</span></h2>
<div class="tbl-wrap"><table>
<thead><tr><th>ประเภท</th><th>รู้ → หา และวิธี</th><th>ข้อ</th></tr></thead><tbody>
<tr><td><b>Type 1</b></td><td>รู้ \(Q\) หรือ \(v\), \(D\), \(L\), \(\varepsilon\) → หา \(h_L\), \(\Delta P\), \(P_1\)<br><span class="pr">ตรง ๆ ไม่ต้องเดา:</span> \(v\to Re\to f\to h_f\)</td><td><a href="#/q1">1</a> <a href="#/q2">2</a> <a href="#/q3">3</a> <a href="#/q4">4</a> <a href="#/q5">5</a></td></tr>
<tr><td><b>Type 2</b></td><td>รู้ \(h_L\) หรือผลต่างระดับ, \(D\), \(L\), \(\varepsilon\) → หา \(v\) หรือ \(Q\)<br><span class="pr">เดา \(f\)</span> → \(v\) → \(Re\) → \(f\) ใหม่ วนจนตรงกัน</td><td><a href="#/q6">6</a> <a href="#/q7">7</a> <a href="#/ea">ข้อสอบ A</a></td></tr>
<tr><td><b>Type 3</b></td><td>รู้ \(Q\), \(h_L\), \(L\), \(\varepsilon\) → หา \(D\)<br>จัดรูป \(D^5\) → <span class="pr">เดา \(f\)</span> → \(D\) → \(v\), \(Re\), \(\varepsilon/D\) → \(f\) ใหม่</td><td><a href="#/q8">8</a></td></tr>
<tr><td><b>ท่อต่อกัน</b></td><td>อนุกรม: \(Q\) เท่ากัน \(h\) บวกกัน<br>ขนาน: \(h\) เท่ากัน \(Q\) บวกกัน</td><td><a href="#/eb">ข้อสอบ B</a></td></tr>
</tbody></table></div>

<h2 class="sec"><span>2 · สมการที่ต้องเขียนก่อนทุกข้อ</span></h2>
<p><strong>สมการพลังงาน</strong> (จุด 1 ต้นทาง → จุด 2 ปลายทาง)</p>
$$\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2+h_L$$
$$h_L=\underbrace{f\,\frac{L}{D}\,\frac{v^2}{2g}}_{\text{major loss}}+\underbrace{\sum K_L\,\frac{v^2}{2g}}_{\text{minor loss}}$$
<p><strong>Reynolds number</strong> และชนิดการไหล</p>
$$Re=\frac{\rho vD}{\mu}=\frac{vD}{\nu},\qquad Re<2000\ \text{Laminar},\quad 2000\text{–}4000\ \text{Transitional},\quad Re>4000\ \text{Turbulent}$$
<p>Laminar ใช้ \(f=64/Re\) (ไม่ขึ้นกับ \(\varepsilon\)). Turbulent อ่าน \(f\) จากชาร์ต ที่ \(Re\) และ \(\varepsilon/D\) หรือใช้ Colebrook</p>
$$\frac{1}{\sqrt f}=-2\log_{10}\!\left(\frac{\varepsilon/D}{3.7}+\frac{2.51}{Re\sqrt f}\right)$$
<p><strong>ความต่อเนื่อง</strong> \(Q=vA=v\,\dfrac{\pi D^2}{4}\) และเมื่อจัดรูปหา \(D\): \(h_f=\dfrac{8fLQ^2}{\pi^2 g D^5}\) ค่าคงที่ของน้ำ \(\gamma=9810\ \text{N/m}^3\), \(\nu=10^{-6}\ \text{m}^2/\text{s}\)</p>

<h2 class="sec"><span>3 · ลำดับที่เขียนในห้องสอบ</span></h2>
<ol>
<li>เขียนข้อมูล พร้อม<span class="pr">แปลงหน่วย</span>: mm → m, cm → m, kPa → Pa</li>
<li>เขียนสมการพลังงานจุด 1 → 2 ก่อนแทนค่า</li>
<li>ขีดฆ่าเทอมที่เป็นศูนย์ และเขียนเหตุผล (ผิวถังใหญ่ \(v\approx0\), ปล่อยสู่อากาศ \(P=0\) เกจ, ท่อขนาดเท่ากัน \(v_1=v_2\))</li>
<li>คำนวณ \(\varepsilon/D\) แล้วแทนค่า รวม \(\sum K_L\) เป็นก้อนเดียว</li>
<li>ข้อที่ต้องเดา: เขียน <b>1<sup>st</sup> guess</b> ทำตารางเล็ก \(f\to v\to Re\to f_{\text{Moody}}\) เทียบ แล้วเขียน <span class="pr">No</span> หรือ <span class="pr">OK</span></li>
<li>ตอบพร้อมหน่วย ขีดเส้นใต้ ตรวจ \(Re\) กับ \(f\) รอบสุดท้ายว่าตรงกันจริง</li>
</ol>

<h2 class="sec"><span>4 · ค่า f ที่ควรเดารอบแรก</span></h2>
<p>ที่ \(Re\) สูงมาก (โซน fully turbulent เส้นนอนในชาร์ต) \(f\) ขึ้นกับ \(\varepsilon/D\) อย่างเดียว ใช้เป็นจุดเริ่ม ค่าจริงจะต่ำกว่าเล็กน้อยถ้า \(Re\) ไม่สูงมาก</p>
<div class="tbl-wrap"><table>
<thead><tr><th class="num">\(\varepsilon/D\)</th><th class="num">0.0002</th><th class="num">0.0003</th><th class="num">0.0005</th><th class="num">0.0008</th><th class="num">0.001</th><th class="num">0.0015</th><th class="num">0.002</th><th class="num">0.003</th><th class="num">0.005</th></tr></thead>
<tbody><tr><td><b>\(f\)</b></td><td class="num">0.0137</td><td class="num">0.0149</td><td class="num">0.0167</td><td class="num">0.0186</td><td class="num">0.0196</td><td class="num">0.0217</td><td class="num">0.0234</td><td class="num">0.0262</td><td class="num">0.0304</td></tr></tbody></table></div>

<h2 class="sec"><span>5 · ค่า K ที่ใช้บ่อย (minor loss)</span></h2>
<div class="tbl-wrap"><table>
<thead><tr><th>จุดที่เกิด</th><th>\(K_L\)</th><th>คูณกับความเร็วของท่อไหน</th></tr></thead><tbody>
<tr><td>ปากท่อจากถัง: reentrant</td><td class="num">0.8</td><td>ท่อที่ต่อจากถัง</td></tr>
<tr><td>ปากท่อ: sharp-edged (ขอบคม)</td><td class="num">0.5</td><td>ท่อที่ต่อจากถัง</td></tr>
<tr><td>ปากท่อ: slightly / well rounded</td><td class="num">0.2 / 0.04</td><td>ท่อที่ต่อจากถัง</td></tr>
<tr><td>ท่อไหลลงถัง (ทางออก ทุกแบบ)</td><td class="num">1.0</td><td>ท่อที่ไหลออก</td></tr>
<tr><td>ข้องอ 90° และอื่น ๆ</td><td class="num">โจทย์ให้ / ดูชาร์ต</td><td>ท่อนั้น</td></tr>
<tr><td>Sudden expansion</td><td class="num">\((1-A_1/A_2)^2\) หรืออ่านชาร์ต</td><td><b>ท่อเล็กก่อนขยาย</b> \(v_1\)</td></tr>
<tr><td>Sudden contraction</td><td class="num">อ่านชาร์ตที่ \(A_{\text{เล็ก}}/A_{\text{ใหญ่}}\)</td><td><b>ท่อเล็กหลังหด</b> \(v_{\text{เล็ก}}\)</td></tr>
</tbody></table></div>

<h2 class="sec"><span>6 · จุดดักที่ทำให้เสียคะแนนบ่อย</span></h2>
<div class="note trap"><b>แปลงหน่วย</b><p>\(\varepsilon\) เป็น mm แต่ \(D\) เป็น m: \(0.12\ \text{mm}/150\ \text{mm}=0.0008\) ต้องหารหน่วยเดียวกัน ความดัน kPa × 1000 ก่อนหารด้วย \(\gamma\)</p></div>
<div class="note trap"><b>ท่อเปลี่ยนขนาด ต้องแปลง v ทุกท่อน</b><p>\(v_2=v_1(D_1/D_2)^2\) ห้ามใช้ \(v_1\) กับท่อ 2 และพจน์ \(v^2/2g\) ที่จุด 1 กับจุด 2 ไม่ตัดกันเมื่อ \(D\) ต่างกัน</p></div>
<div class="note trap"><b>ปล่อยสู่อากาศ ต้องมี v²/2g ที่ปลายท่อ</b><p>ที่จุด 2 \(P_2=0\) แต่ \(v_2\neq0\) ข้อ 7 ใช้ \(\dfrac{v^2}{2g}\) ที่ปลายท่อ เป็นเทอมแยก (บวกกับก้อน minor)</p></div>
<div class="note trap"><b>เครื่องหมายของ z</b><p>ของไหลขึ้นเนิน \(z_2>z_1\) เมื่อย้ายข้างไปรวมกับ \(P_1-P_2\) ต้องเป็นลบ: \(\dfrac{P_1-P_2}{\gamma}-(z_2-z_1)\)</p></div>
<div class="note trap"><b>ท่อขนาน อย่าบวก h</b><p>ท่อขนานมี \(h_2=h_3\) หา \(h_L\) รวมใช้ทางเดียว \(h_1+h_2+h_4\) ไม่ใช่ \(h_2+h_3\)</p></div>
<div class="note trap"><b>ตรวจรอบสุดท้าย</b><p>\(f\) ที่เดาต้องตรงกับ \(f\) จากชาร์ตที่ \(Re\) รอบสุดท้าย ถ้าต่างเกิน ~2% ให้ทำอีกรอบ</p></div>
`
  });
})();
