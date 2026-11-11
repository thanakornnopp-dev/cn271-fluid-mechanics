/* โจทย์ 15 คะแนน แบบข้อสอบ: ท่ออนุกรมวางเอียง (A) และโครงข่ายท่อขนาน (B) */
(function () {
  var R = String.raw;
  var P = function (o) { (window.SHEETS = window.SHEETS || []).push(o); };

  /* ---------- ข้อสอบ A ---------- */
  P({
    id: "ea", idx: "สอบ A", order: 20, group: "exam", no: "ข้อสอบ A", type: "Type 2 · ท่ออนุกรม เอียง", src: "prof",
    srcNote: "ลายมืออาจารย์ หน้า 9 (ตั้งสมการ; ขั้นเดาค่า f เติมโดยทีม)",
    title: "ท่อ 3 เส้นต่ออนุกรม วางเอียง 5°: หาความเร็วในแต่ละท่อ",
    sub: "Series + sudden expansion/contraction",
    ask: "ท่อสามท่อต่อกันตามรูป มุมเอียง \\(\\theta=5^\\circ\\) ผลต่างความดัน A กับ B เท่ากับ 245.25 kPa จงประมาณความเร็วในแต่ละท่อ \\((\\nu=10^{-6}\\ \\text{m}^2/\\text{s})\\)",
    given: [["θ", "5°"], ["P_A − P_B", "245.25 kPa"], ["ท่อ 1", "D 0.4 · L 80 · ε 0.08 mm"], ["ท่อ 2", "D 0.5 · L 120 · ε 0.15 mm"], ["ท่อ 3", "D 0.3 · L 80 · ε 0.12 mm"]],
    fig: R`<svg viewBox="0 0 520 220" role="img" aria-label="ท่อสามเส้นต่ออนุกรม เอียงขึ้นจาก A ไป B มุม 5 องศา">
<line class="h" x1="30" y1="190" x2="480" y2="190"/><path class="t" style="stroke-width:7" d="M44 178L170 150"/><path class="t" style="stroke-width:12" d="M170 150L330 112"/><path class="t" style="stroke-width:5" d="M330 112L460 80"/>
<circle cx="44" cy="178" r="13" class="l" fill="var(--sheet)"/><text x="39" y="183">A</text><circle cx="460" cy="80" r="13" class="l" fill="var(--sheet)"/><text x="455" y="85">B</text>
<text x="90" y="144">ท่อ 1</text><text x="236" y="98">ท่อ 2</text><text x="380" y="82">ท่อ 3</text>
<path class="l" d="M110 190A66 66 0 0 0 106 182"/><text x="116" y="184" class="r">θ = 5°</text>
<line class="l" x1="488" y1="190" x2="488" y2="80"/><text x="430" y="140" class="r">z<tspan dy="4" font-size="10">B</tspan><tspan dy="-4"> = 280 sin 5°</tspan></text>
<text x="90" y="212" class="b">L₁=80 + L₂=120 + L₃=80 = 280 m</text></svg>`,
    cap: "รูปจำลองจากโจทย์ (ไม่ตามสัดส่วน)",
    steps: [
      ["หาความสูงของ B (A เป็น datum)", R`$$z_A=0,\qquad z_B=(L_1+L_2+L_3)\sin5^\circ=280\sin5^\circ=24.40\ \text{m}$$`, "b"],
      ["K ของ minor loss จากชาร์ตของอาจารย์", R`$$\frac{A_1}{A_2}=\Big(\frac{0.4}{0.5}\Big)^2=0.64\ \Rightarrow\ K_{12}=0.15\ (\text{expansion},\ \times\tfrac{v_1^2}{2g})$$$$\frac{A_3}{A_2}=\Big(\frac{0.3}{0.5}\Big)^2=0.36\ \Rightarrow\ K_{23}=0.35\ (\text{contraction},\ \times\tfrac{v_3^2}{2g})$$`, "b"],
      ["ความต่อเนื่อง Q₁ = Q₂ = Q₃  ทุกความเร็วในรูป v₁", R`$$v_2=v_1\frac{A_1}{A_2}=0.64\,v_1,\qquad v_3=v_1\frac{A_1}{A_3}=\Big(\frac{0.4}{0.3}\Big)^2v_1=1.78\,v_1$$`, "b"],
      ["สมการพลังงาน A → B", R`$$\frac{P_A}{\gamma}+\frac{v_1^2}{2g}+0=\frac{P_B}{\gamma}+\frac{v_3^2}{2g}+z_B+f_1\tfrac{80}{0.4}\tfrac{v_1^2}{2g}+f_2\tfrac{120}{0.5}\tfrac{v_2^2}{2g}+f_3\tfrac{80}{0.3}\tfrac{v_3^2}{2g}+0.15\tfrac{v_1^2}{2g}+0.35\tfrac{v_3^2}{2g}$$`, "b"],
      ["ย้ายข้างและรวมเป็น ก้อน × v₁²/2g", R`$$\frac{P_A-P_B}{\gamma}-z_B=\frac{245.25\times10^{3}}{9810}-24.40=0.60\ \text{m}$$$$0.60=\big[(1.78^2-1)+0.15+0.35(1.78)^2+200f_1+98.3f_2+844.9f_3\big]\frac{v_1^2}{2g}=\big[3.427+200f_1+98.3f_2+844.9f_3\big]\frac{v_1^2}{2g}\ \star$$<p class="n">\(98.3=\frac{120}{0.5}(0.64)^2\) และ \(844.9=\frac{80}{0.3}(1.78)^2\)</p>`, "r"],
      ["ε/D ของแต่ละท่อ", R`$$\Big(\frac{\varepsilon}{D}\Big)_1=\frac{0.08}{400}=0.0002,\quad \Big(\frac{\varepsilon}{D}\Big)_2=\frac{0.15}{500}=0.0003,\quad \Big(\frac{\varepsilon}{D}\Big)_3=\frac{0.12}{300}=0.0004$$`, "b"],
      ["1st guess: f จากโซน fully turbulent", R`<p>\(f_1=0.014,\ f_2=0.015,\ f_3=0.016\)</p>$$\text{ก้อน}=3.427+2.80+1.47+13.52=21.22\ \Rightarrow\ v_1=\sqrt{\frac{0.60(2g)}{21.22}}=0.745\ \text{m/s}$$$$v_2=0.477,\ v_3=1.326\ \Rightarrow\ Re_1=3.0\times10^5,\ Re_2=2.4\times10^5,\ Re_3=4.0\times10^5$$<p>อ่านชาร์ต: \(f_1=0.0163,\ f_2=0.0175,\ f_3=0.0173\) ไม่ตรงที่เดา → <span class="pr">No</span></p>`, "r"],
      ["2nd guess: ใช้ f ที่อ่านได้", R`$$\text{ก้อน}=3.427+3.26+1.72+14.62=23.02\ \Rightarrow\ v_1=\sqrt{\frac{0.60(2g)}{23.02}}=0.715\ \text{m/s}$$$$v_2=0.458,\ v_3=1.273\ \Rightarrow\ Re_1=2.9\times10^5,\ Re_2=2.3\times10^5,\ Re_3=3.8\times10^5$$<p>อ่านชาร์ตได้ \(f\) เท่าเดิมทั้งสามท่อ → <span class="pr">OK</span></p>`, "r"],
      ["ตรวจทาน", R`<p>วนด้วย Colebrook จนลู่เข้า ได้ \(v_1=0.713,\ v_2=0.457,\ v_3=1.268\) m/s \(Q=0.0897\) m³/s ต่างจากที่อ่านชาร์ตไม่ถึง 1%</p>`, "v"]
    ],
    answer: R`<p class="big">v₁ ≈ 0.71 m/s</p><p class="big">v₂ ≈ 0.46 m/s</p><p class="big">v₃ ≈ 1.27 m/s</p>`,
    revs: [["ท่อเอียงต้องหา z_B = L รวม × sin θ ย้ายข้างเป็นลบ \\(\\frac{P_A-P_B}{\\gamma}-z_B\\)", "ได้ 25 m แทน 0.60 m ผิดทั้งข้อ"], ["Expansion ใช้ \\(v_1\\) (ท่อเล็กก่อนขยาย) Contraction ใช้ \\(v_3\\) (ท่อเล็กหลังหด)", "ก้อน minor ผิด"], ["\\(v_A=v_1\\) และ \\(v_B=v_3\\) พจน์ \\(v^2/2g\\) สองข้างไม่ตัดกัน", "ลืม (1.78² − 1)"], ["ตั้งสมการเสร็จแล้ว อย่าลืมแปลง mm → m ใน ε/D", "f ผิดเป็นพันเท่า"]]
  });

  /* ---------- ข้อสอบ B ---------- */
  P({
    id: "eb", idx: "สอบ B", order: 21, group: "exam", no: "ข้อสอบ B", type: "ท่อขนาน + อนุกรม", src: "prof",
    srcNote: "ลายมืออาจารย์ หน้า 10 (ตั้งสมการถึง h_AB; ที่เหลือเติมโดยทีม)",
    title: "โครงข่ายท่อ 4 เส้น (15 คะแนน): หา major loss จาก AA ถึง BB",
    sub: "Parallel pipes, h₂ = h₃",
    ask: "ท่อ 4 เส้นต่อกันตามรูป จงประมาณ major loss จาก AA ถึง BB จุด A ต่ำกว่าจุด B 10 m ท่อจาก A ถึง B ยาว 300 m major loss ในท่อ 3 เท่ากับ 0.42 m ความดันที่ A และ B เท่ากับ 910 และ 811.41 kPa ไม่ต้องคิด minor loss",
    given: [["ท่อ 1", "D 0.9 · L 900 · ε 0.90 mm"], ["ท่อ 2", "D 0.8 · L 800 · ε 0.32 mm"], ["ท่อ 3", "D 0.6 · L 800 · ε 0.48 mm"], ["ท่อ 4", "D ไม่ทราบ · L 1000 · ε 0.96 mm"], ["h₃", "0.42 m"], ["P_A, P_B", "910, 811.41 kPa"], ["z_B − z_A", "10 m"], ["L_AB (ในท่อ 4)", "300 m"]],
    fig: R`<svg viewBox="0 0 520 190" role="img" aria-label="ท่อ 1 แยกเป็นท่อ 2 และท่อ 3 ขนานกัน แล้วรวมเป็นท่อ 4 ผ่านจุด A และ B">
<path class="t" d="M20 95H150"/><path class="l" style="stroke-width:3" d="M150 95C180 40 270 40 300 95"/><path class="l" style="stroke-width:4.5" d="M150 95C180 150 270 150 300 95"/><path class="t" style="stroke-width:3" d="M300 95H440"/>
<text x="20" y="80">AA</text><text x="78" y="118">ท่อ 1</text><text x="210" y="50">ท่อ 2</text><text x="210" y="154">ท่อ 3</text><text x="355" y="118">ท่อ 4</text><text x="470" y="80">BB</text>
<circle cx="330" cy="95" r="11" class="l" fill="var(--sheet)"/><text x="325" y="100">A</text><circle cx="400" cy="95" r="11" class="l" fill="var(--sheet)"/><text x="395" y="100">B</text>
<text x="196" y="20" class="r">h₂ = h₃ = 0.42 m</text><text x="318" y="152" class="b">L_AB = 300 m</text><text x="318" y="170" class="b">z_B − z_A = 10 m</text></svg>`,
    cap: "รูปจำลองจากโจทย์ (ไม่ตามสัดส่วน)",
    steps: [
      ["เขียนสมการ major loss รวมตามทางเดียว", R`<p>น้ำ 1 ก้อนเลือกเดินทางเดียว (ผ่านท่อ 2 หรือ 3) และ <span class="pr">\(h_2=h_3=0.42\) m</span> จึงบวกแค่ครั้งเดียว</p>$$h_{AA\to BB}=h_1+h_2+h_4=h_1+0.42+h_4$$`, "r"],
      ["หา h_AB ในท่อ 4 ด้วยสมการพลังงาน A → B", R`<p>ท่อ 4 ขนาดคงที่ \(v_A=v_B\) ตัดกัน:</p>$$\frac{P_A}{\gamma}=\frac{P_B}{\gamma}+z_B+h_{AB}\ \Rightarrow\ \frac{910\times10^3}{9810}-\frac{811.41\times10^3}{9810}=10+h_{AB}$$$$98.59/9.81=10.05=10+h_{AB}\ \Rightarrow\ h_{AB}=0.05\ \text{m}$$`, "b"],
      ["ขยายเป็นท่อ 4 ทั้งเส้น (ยาว 1000 m)", R`<p>ท่อเดียวกัน \(D_4, v_4, f_4\) เท่ากัน \(h\propto L\) (ไม่ต้องรู้ \(D_4\))</p>$$h_4=0.05\times\frac{1000}{300}=0.167\ \text{m}$$`, "r"],
      ["ท่อ 3: หา v₃ จาก h₃ = 0.42 (เดา f)", R`$$0.42=f_3\frac{800}{0.6}\frac{v_3^2}{2g}\Rightarrow v_3=\sqrt{\frac{0.00618}{f_3}},\quad \frac{\varepsilon}{D}=\frac{0.48}{600}=0.0008$$<p>เดา \(f=0.02\to v=0.556\), \(Re=3.3\times10^5\), ชาร์ต \(f=0.0196\) → \(v_3=0.56\) m/s</p>`, "r"],
      ["ท่อ 2: หา v₂ จาก h₂ = 0.42 (เดา f)", R`$$0.42=f_2\frac{800}{0.8}\frac{v_2^2}{2g}\Rightarrow v_2=\sqrt{\frac{0.00824}{f_2}},\quad \frac{\varepsilon}{D}=\frac{0.32}{800}=0.0004$$<p>เดา \(f=0.017\to v=0.70\), \(Re=5.6\times10^5\), ชาร์ต \(f=0.0169\) → \(v_2=0.70\) m/s</p>`, "r"],
      ["อัตราการไหลรวม Q = Q₂ + Q₃", R`$$Q=\frac{\pi(0.8)^2}{4}(0.70)+\frac{\pi(0.6)^2}{4}(0.56)=0.351+0.159=0.51\ \text{m}^3/\text{s}$$`, "b"],
      ["ท่อ 1: หา h₁", R`$$v_1=\frac{Q}{A_1}=\frac{0.51}{\pi(0.45)^2}=0.80\ \text{m/s},\quad Re=7.2\times10^{5},\quad \frac{\varepsilon}{D}=\frac{0.90}{900}=0.001\Rightarrow f_1=0.020$$$$h_1=f_1\frac{L_1}{D_1}\frac{v_1^2}{2g}=0.020\,\frac{900}{0.9}\,\frac{0.80^2}{2g}=0.66\ \text{m}$$`, "r"],
      ["รวม", R`$$h_{AA\to BB}=h_1+h_2+h_4=0.66+0.42+0.17=1.24\ \text{m}$$`, "r"],
      ["ตรวจทาน", R`<p>Colebrook ให้ \(Q=0.5096,\ h_1=0.656,\ h_4=0.166\) รวม \(1.243\) m ตรงกัน และ \(h_1\) สมเหตุสมผล: ท่อ 1 ใหญ่สุด ยาวสุด Q ผ่านหมด แต่ v ต่ำ</p>`, "v"]
    ],
    answer: R`<p class="big">h<sub>AA→BB</sub> ≈ 1.24 m</p>`,
    revs: [["ท่อขนาน อย่าเอา \\(h_2+h_3\\) มารวม ใช้ตัวใดตัวหนึ่ง", "ได้ 1.66 m ผิด"], ["\\(h_{AB}\\) ต้องหักระดับ 10 m ก่อน: 10.05 − 10 = 0.05", "ถ้าใช้ 10.05 เป็น \\(h_{AB}\\) ผิดเป็น 200 เท่า"], ["ท่อ 4 ไม่ทราบ D แต่ ratio ของความยาวพอ \\(h_4=h_{AB}\\cdot1000/300\\)", "ติดที่ไม่รู้ D_4"], ["ท่อ 1 ใช้ \\(Q_1=Q_2+Q_3\\) ไม่ใช่ \\(v_2\\)", "h₁ ผิด"]]
  });
})();
