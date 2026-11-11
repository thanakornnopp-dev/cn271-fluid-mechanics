# -*- coding: utf-8 -*-
"""เครื่องมือ: เครื่องคิดเลข (ตัวโปรแกรมอยู่ที่ assets/calc.js) และตารางอ้างอิง"""

CALC = r'''<section id="calc">
<h2 class="prob"><span class="tag">เครื่องมือ</span>เครื่องคิดเลข เดา f แล้ววนจนลู่เข้า</h2>
<div class="stmt"><p>ใช้ตรวจคำตอบที่ทำมือ ไม่ใช่แทนการเขียนวิธีทำ ตารางแต่ละรอบหน้าตาเหมือนที่ต้องเขียนในข้อสอบ ใช้ Colebrook-White แทนการอ่านชาร์ต จึงต่างจากค่าที่อ่านจากชาร์ตได้เล็กน้อย (ไม่เกิน ~2%)</p></div>
<form class="calc" id="calcform" onsubmit="return false">
<label class="full">โจทย์แบบไหน
<select name="mode">
<option value="v">Type 2: หา v (รู้ผลต่างระดับ H ที่ใช้ได้)</option>
<option value="D">Type 3: หา D (รู้ Q และ h<sub>f</sub>)</option>
<option value="h">Type 1: หา h<sub>f</sub> (รู้ Q และ D)</option>
</select></label>
<label data-m="v">H ที่ใช้ได้ (m)<input name="H" inputmode="decimal" value="5"></label>
<label data-m="D h">Q (m³/s)<input name="Q" inputmode="decimal" value="0.5"></label>
<label data-m="D">h<sub>f</sub> (m)<input name="hf" inputmode="decimal" value="10"></label>
<label data-m="v h">D (m)<input name="D" inputmode="decimal" value="0.15"></label>
<label>L (m)<input name="L" inputmode="decimal" value="100"></label>
<label>ε (mm)<input name="eps" inputmode="decimal" value="0.12"></label>
<label data-m="v h">ΣK<input name="K" inputmode="decimal" value="1.6"></label>
<label>ν (m²/s)<input name="nu" inputmode="decimal" value="0.000001"></label>
<label>f เดารอบแรก<input name="f0" inputmode="decimal" value="0.02"></label>
<label class="full chk" data-m="v"><input type="checkbox" name="ex" checked> ปลายท่อปล่อยสู่อากาศ (มีเทอม v²/2g ที่ปลายท่อ)</label>
<div class="full"><button class="run" type="button" id="calcrun">คำนวณ</button></div>
</form>
<div class="calcout" id="calcout" role="status"></div>
<div class="bx chk"><b>ลองกับข้อสอบ</b><div>ค่าเริ่มต้นคือข้อ 7 (H = 5, D = 0.15, L = 100, ε = 0.12, ΣK = 1.6, ปลายท่อสู่อากาศ) ได้ v ≈ 2.51 m/s · ข้อ 6: H = 3, D = 0.15, L = 700, ε = 0.12, ΣK = 0 และไม่ติ๊กช่องปลายท่อ ได้ 0.77 m/s · ข้อ 8: เลือก Type 3, Q = 0.5, h<sub>f</sub> = 10, L = 200 ได้ D ≈ 0.365 m</div></div>
</section>'''

REF = r'''<section id="ref">
<h2 class="prob"><span class="tag">อ้างอิง</span>คำตอบทุกข้อ วิธีอ่านชาร์ต และศัพท์</h2>
<h3 class="grp">คำตอบทุกข้อ (ไว้เช็คหลังทำเอง)</h3>
<div class="tw"><table><thead><tr><th>ข้อ</th><th>ประเภท</th><th>คำตอบ</th></tr></thead><tbody>
<tr><td><a href="#q1">1</a></td><td>ชนิดการไหล</td><td>\(Re=10{,}000\) Turbulent, \(v_{max}=0.02\) m/s</td></tr>
<tr><td><a href="#q2">2</a></td><td>\(\Delta P\) ท่อราบ</td><td>Laminar, 0.05 Pa, ≈ 15 Pa</td></tr>
<tr><td><a href="#q3">3</a></td><td>Type 1</td><td>\(h_{L,12}=9.84\), \(h_{L,23}=5.47\) m</td></tr>
<tr><td><a href="#q4">4</a></td><td>Type 1</td><td>\(h_f\approx37\) m (36.7–37.2), \(h_m=0.52\) m</td></tr>
<tr><td><a href="#q5">5</a></td><td>Type 1</td><td>\(P_{1,min}\approx219.6\) kPa</td></tr>
<tr><td><a href="#q6">6</a></td><td>Type 2</td><td>\(v\approx0.77\) m/s</td></tr>
<tr><td><a href="#q7">7</a></td><td>Type 2</td><td>\(v\approx2.51\) m/s</td></tr>
<tr><td><a href="#q8">8</a></td><td>Type 3</td><td>\(D\approx0.36\) m (0.365)</td></tr>
<tr><td><a href="#ea">สอบ A</a></td><td>อนุกรม เอียง 5°</td><td>\(v_1,v_2,v_3\approx0.713,\ 0.457,\ 1.268\) m/s</td></tr>
<tr><td><a href="#eb">สอบ B</a></td><td>โครงข่าย 4 ท่อ</td><td>\(h_{AA\to BB}\approx1.24\) m (\(Q=0.51\) m³/s)</td></tr>
<tr><td><a href="#q9">9</a></td><td>อนุกรมแนวราบ</td><td>\(Q\approx3.6\times10^{-3}\) m³/s</td></tr>
<tr><td><a href="#q10">10</a></td><td>ขนาน</td><td>\(Q=0.0149,\ 0.0053,\ 0.0035\); รวม \(0.0237\) m³/s</td></tr>
<tr><td><a href="#q11">11</a></td><td>ข้อมูลไม่ครบ</td><td>ไม่มี \(\varepsilon\) จึงยังหาไม่ได้</td></tr>
<tr><td><a href="#q12">12</a></td><td>ถัง → ท่อ 2 ขนาด</td><td>\(Q\approx0.54\) m³/s</td></tr>
<tr><td><a href="#q13">13</a></td><td>ขนาน + Type 3</td><td>\(D_4\approx0.39\) m</td></tr>
</tbody></table></div>
<h3 class="grp">วิธีอ่านชาร์ต Glasgow / Moody</h3>
<ol class="st">
<li>คำนวณ \(Re=vD/\nu\) แล้วหาแกนนอน (log) ของชาร์ต</li>
<li>คำนวณ \(\varepsilon/D\) <b>หน่วยเดียวกัน</b> แล้วเลือกเส้นโค้งที่มีค่านั้น (ป้ายอยู่ทางขวาของชาร์ต) ถ้าอยู่ระหว่างเส้น ให้ประมาณตามสัดส่วน</li>
<li>ลากแนวตั้งจาก \(Re\) ไปชนเส้นโค้ง แล้วลากแนวนอนไปแกนตั้งอ่านค่า \(f\)</li>
<li>\(Re<2000\): ใช้เส้นตรง Laminar \(f=64/Re\) โดยไม่ดู \(\varepsilon/D\) · ช่วง 2000–4000 คือ Critical/Transition ไม่น่าเชื่อถือ · เส้นโค้งที่ขนานแกนนอนทางขวาคือโซน fully turbulent</li>
</ol>
<h3 class="grp">ศัพท์ไทย–อังกฤษ</h3>
<div class="tw"><table><thead><tr><th>English</th><th>ไทย</th></tr></thead><tbody>
<tr><td>Major loss \(h_f\)</td><td>การสูญเสียพลังงานหลัก (แรงเสียดทานตามความยาวท่อ)</td></tr>
<tr><td>Minor loss \(h_m\)</td><td>การสูญเสียพลังงานรอง (ข้องอ ขยาย หด วาล์ว ทางเข้า/ออก)</td></tr>
<tr><td>Friction factor \(f\)</td><td>สัมประสิทธิ์ความเสียดทาน (Darcy)</td></tr>
<tr><td>Relative roughness \(\varepsilon/D\)</td><td>ความขรุขระสัมพัทธ์</td></tr>
<tr><td>Reynolds number</td><td>เลขเรย์โนลด์ส</td></tr>
<tr><td>Laminar / Transitional / Turbulent</td><td>ราบเรียบ / ช่วงเปลี่ยน / ปั่นป่วน</td></tr>
<tr><td>Dynamic viscosity \(\mu\) · Kinematic \(\nu\)</td><td>ความหนืดสัมบูรณ์ · ความหนืดจลน์ (\(\nu=\mu/\rho\))</td></tr>
<tr><td>Energy equation</td><td>สมการพลังงาน</td></tr>
<tr><td>Pressure / Velocity / Elevation head</td><td>เฮดความดัน / เฮดความเร็ว / เฮดระดับ</td></tr>
<tr><td>Series / Parallel pipes</td><td>ท่อต่ออนุกรม / ต่อขนาน</td></tr>
<tr><td>Sudden expansion / contraction</td><td>ท่อขยาย / หดกะทันหัน</td></tr>
<tr><td>Pump / Turbine · Cavitation</td><td>ปั๊ม / เทอร์ไบน์ · การเกิดโพรงไอ</td></tr>
</tbody></table></div>
</section>'''
