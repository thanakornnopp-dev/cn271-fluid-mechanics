# -*- coding: utf-8 -*-

def get_section_calc():
    return r'''
<section id="calc">
  <header class="top">
    <p class="kick">เครื่องมือคำนวณสดสำหรับกลศาสตร์ของไหล CN 271</p>
    <h1>เครื่องคิดเลขวิศวกรรมของไหล (Universal Fluid Calculator)</h1>
    <p class="sub">ความเค้นเฉือน · มาโนมิเตอร์ · แรงดันประตูน้ำ · แรงกระแทกลำน้ำ · Froude/Reynolds Scale · ท่อ Type II &amp; III · Venturi · Cavitation</p>
    <p class="by">CN 271 กลศาสตร์ของไหลสำหรับวิศวกรโยธา · มหาวิทยาลัยธรรมศาสตร์</p>
  </header>

  <h2 class="prob"><span class="tag">คิดเลข</span>คำนวณและตรวจสอบผลการทดลอง/ข้อสอบสด</h2>
  <div class="stmt">
    <p>เครื่องคิดเลขนี้พัฒนาขึ้นเพื่อให้นักศึกษาใช้ตรวจสอบความถูกต้องของการทำแบบฝึกหัดและการบ้านทุกบท คำนวณตามมาตรฐานวิศวกรรมชลศาสตร์และสมการของอาจารย์ผู้สอน พร้อมแสดงขั้นตอนการคำนวณและตรวจสอบมิติ 100%</p>
  </div>

  <form id="calcform" class="calc" style="border:1.5px solid var(--ink);padding:18px;background:var(--hover);">
    <div class="full">
      <label>
        <b>เลือกหัวข้อที่ต้องการคำนวณ:</b>
        <select name="mode" style="font-weight:600;color:var(--navy);">
          <option value="shear">บทที่ 1: ความเค้นเฉือนและกฎความหนืดของนิวตัน (τ = μ V/h)</option>
          <option value="mano">บทที่ 2: มาโนมิเตอร์และผลต่างความดัน (ΔP = γ Δh)</option>
          <option value="gate">บทที่ 2: แรงดันบนผนังระนาบเรียบและจุดศูนย์กลางแรงกด (FR &amp; y_cp)</option>
          <option value="jet">บทที่ 3: แรงกระแทกของลำน้ำพุ่งชนแผ่นโค้ง 180° (Jet on Vane)</option>
          <option value="accel">บทที่ 3: ความเร็วและความเร่งของอนุภาคของไหล (V &amp; a Field)</option>
          <option value="scale">บทที่ 4: การสเกลแบบจำลอง Froude &amp; Reynolds Similitude</option>
          <option value="v" selected>บทที่ 5: ท่อ Type II วนรอบหาความเร็วและอัตราไหล (v, Q)</option>
          <option value="D">บทที่ 5: ท่อ Type III วนรอบออกแบบขนาดเส้นผ่านศูนย์กลาง (D)</option>
          <option value="venturi">เครื่องมือวัด: อัตราการไหลท่อเวนจูรี่ (Venturi Meter)</option>
          <option value="cavitation">เครื่องมือวัด: ขีดจำกัดความสูงปั๊มป้องกัน Cavitation (Z1,max)</option>
        </select>
      </label>
    </div>

    <!-- Mode: shear -->
    <div data-m="shear">
      <label>ความหนืดไดนามิก μ (Pa·s):
        <input type="number" step="any" name="sh_mu" value="0.29" placeholder="เช่น 0.29">
      </label>
    </div>
    <div data-m="shear">
      <label>ความเร็วแผ่น V (m/s):
        <input type="number" step="any" name="sh_v" value="3.2" placeholder="เช่น 3.2">
      </label>
    </div>
    <div data-m="shear">
      <label>ระยะห่างแผ่น h (mm):
        <input type="number" step="any" name="sh_h" value="8.0" placeholder="เช่น 8.0">
      </label>
    </div>
    <div data-m="shear">
      <label>พื้นที่แผ่น A (m², ไม่จำเป็น):
        <input type="number" step="any" name="sh_a" value="1.0" placeholder="เช่น 1.0">
      </label>
    </div>

    <!-- Mode: mano -->
    <div data-m="mano">
      <label>ความถ่วงจำเพาะของของเหลว SG:
        <input type="number" step="any" name="mn_sg" value="13.6" placeholder="เช่น 13.6 ปรอท หรือ 1.0 น้ำ">
      </label>
    </div>
    <div data-m="mano">
      <label>ผลต่างระดับความสูง Δh (m):
        <input type="number" step="any" name="mn_dh" value="0.20" placeholder="เช่น 0.20">
      </label>
    </div>
    <div data-m="mano">
      <label>มุมเอียงท่อ θ (องศา, ถ้าท่อดิ่งใส่ 90):
        <input type="number" step="any" name="mn_theta" value="90">
      </label>
    </div>

    <!-- Mode: gate -->
    <div data-m="gate">
      <label>ความกว้างผนัง b (m):
        <input type="number" step="any" name="gt_b" value="5.0" placeholder="เช่น 5.0">
      </label>
    </div>
    <div data-m="gate">
      <label>ความสูงผนัง h (m):
        <input type="number" step="any" name="gt_h" value="6.0" placeholder="เช่น 6.0">
      </label>
    </div>
    <div data-m="gate">
      <label>ระดับน้ำจากขอบบนผนัง hw (m, ถ้าน้ำเสมอขอบใส่ 0):
        <input type="number" step="any" name="gt_hw" value="0.0">
      </label>
    </div>

    <!-- Mode: jet -->
    <div data-m="jet">
      <label>ความเร็วลำน้ำ v (m/s):
        <input type="number" step="any" name="jt_v" value="24.0" placeholder="เช่น 24.0">
      </label>
    </div>
    <div data-m="jet">
      <label>พื้นที่หน้าตัดลำน้ำ A (m²):
        <input type="number" step="any" name="jt_a" value="0.010" placeholder="เช่น 0.010">
      </label>
    </div>
    <div data-m="jet">
      <label>ความเร็วการเคลื่อนที่ของแผ่น u (m/s, แผ่นนิ่งใส่ 0):
        <input type="number" step="any" name="jt_u" value="6.0" placeholder="เช่น 6.0 หรือ 0">
      </label>
    </div>
    <div data-m="jet">
      <label>มุมหักเลี้ยวของแผ่น (องศา, ตัวยูใส่ 180):
        <input type="number" step="any" name="jt_theta" value="180">
      </label>
    </div>

    <!-- Mode: accel -->
    <div data-m="accel">
      <label>ตำแหน่ง X (m):
        <input type="number" step="any" name="ac_x" value="2.0" placeholder="เช่น 2.0">
      </label>
    </div>
    <div data-m="accel">
      <label>ตำแหน่ง Y (m):
        <input type="number" step="any" name="ac_y" value="1.0" placeholder="เช่น 1.0">
      </label>
    </div>
    <div data-m="accel">
      <label>ตำแหน่ง Z (m):
        <input type="number" step="any" name="ac_z" value="3.0" placeholder="เช่น 3.0">
      </label>
    </div>
    <div data-m="accel">
      <label>เวลา t (s):
        <input type="number" step="any" name="ac_t" value="0.5" placeholder="เช่น 0.5">
      </label>
    </div>

    <!-- Mode: scale -->
    <div data-m="scale">
      <label>ประเภทแบบจำลอง:
        <select name="sc_type">
          <option value="froude">Froude Scale (ผิวน้ำอิสระ แม่น้ำ คลื่น เขื่อน)</option>
          <option value="reynolds">Reynolds Scale (ท่อปิด อากาศยาน ใต้น้ำ)</option>
        </select>
      </label>
    </div>
    <div data-m="scale">
      <label>อัตราส่วนขนาดโมเดล:จริง (1:N เช่น 80 ใส่ 80):
        <input type="number" step="any" name="sc_scale" value="80" placeholder="เช่น 80">
      </label>
    </div>
    <div data-m="scale">
      <label>ความเร็วที่วัดได้ในโมเดล vm (m/s):
        <input type="number" step="any" name="sc_vm" value="18.0" placeholder="เช่น 18.0">
      </label>
    </div>

    <!-- Mode: v (Pipe Flow Type II) -->
    <div data-m="v">
      <label>เฮดสูญเสียรวม H (m):
        <input type="number" step="any" name="H" value="20.0" placeholder="เช่น 20">
      </label>
    </div>
    <div data-m="v">
      <label>ความยาวท่อ L (m):
        <input type="number" step="any" name="L" value="150.0" placeholder="เช่น 150">
      </label>
    </div>
    <div data-m="v">
      <label>เส้นผ่านศูนย์กลาง D (m):
        <input type="number" step="any" name="D" value="0.15" placeholder="เช่น 0.15">
      </label>
    </div>
    <div data-m="v">
      <label>ความขรุขระสัมพัทธ์ ε (mm):
        <input type="number" step="any" name="eps" value="0.15" placeholder="เช่น 0.15">
      </label>
    </div>
    <div data-m="v">
      <label>สัมประสิทธิ์การสูญเสียรองรวม ΣKL:
        <input type="number" step="any" name="K" value="1.5" placeholder="เช่น 1.5">
      </label>
    </div>
    <div data-m="v">
      <label>คิดการสูญเสียที่ทางออก exit (v²/2g):
        <input type="checkbox" name="ex" checked> คิด (K_exit = 1.0)
      </label>
    </div>
    <div data-m="v">
      <label>ความหนืดคิเนมาติก ν (m²/s):
        <input type="number" step="any" name="nu" value="0.000001" placeholder="เช่น 1e-6">
      </label>
    </div>
    <div data-m="v">
      <label>ค่า f เดาเริ่มต้น:
        <input type="number" step="any" name="f0" value="0.02" placeholder="เช่น 0.02">
      </label>
    </div>

    <!-- Mode: D (Pipe Flow Type III) -->
    <div data-m="D">
      <label>อัตราการไหลเป้าหมาย Q (m³/s):
        <input type="number" step="any" name="Q" value="0.20" placeholder="เช่น 0.20">
      </label>
    </div>
    <div data-m="D">
      <label>เฮดสูญเสียยอมให้ hf (m):
        <input type="number" step="any" name="hf" value="20.0" placeholder="เช่น 20">
      </label>
    </div>
    <div data-m="D">
      <label>ความยาวท่อ L (m):
        <input type="number" step="any" name="L_d" value="3000.0" placeholder="เช่น 3000">
      </label>
    </div>
    <div data-m="D">
      <label>ความขรุขระ ε (mm):
        <input type="number" step="any" name="eps_d" value="0.045" placeholder="เช่น 0.045">
      </label>
    </div>

    <!-- Mode: venturi -->
    <div data-m="venturi">
      <label>สัมประสิทธิ์เครื่อง Cd (ปกติ 0.85–0.98):
        <input type="number" step="any" name="vt_cd" value="0.85" placeholder="เช่น 0.85">
      </label>
    </div>
    <div data-m="venturi">
      <label>เส้นผ่านศูนย์กลางท่อหลัก D1 (m):
        <input type="number" step="any" name="vt_d1" value="0.20" placeholder="เช่น 0.20">
      </label>
    </div>
    <div data-m="venturi">
      <label>เส้นผ่านศูนย์กลางคอคอด D2 (m):
        <input type="number" step="any" name="vt_d2" value="0.10" placeholder="เช่น 0.10">
      </label>
    </div>
    <div data-m="venturi">
      <label>ผลต่างความดัน ΔP (Pa):
        <input type="number" step="any" name="vt_dp" value="300.0" placeholder="เช่น 300">
      </label>
    </div>

    <!-- Mode: cavitation -->
    <div data-m="cavitation">
      <label>ความดันบรรยากาศ Patm (kPa):
        <input type="number" step="any" name="cv_patm" value="101.0" placeholder="เช่น 101.0">
      </label>
    </div>
    <div data-m="cavitation">
      <label>ความดันไอ Pv (Pa):
        <input type="number" step="any" name="cv_pv" value="5950.0" placeholder="เช่น 5950">
      </label>
    </div>
    <div data-m="cavitation">
      <label>เฮดดูดที่ปั๊มต้องการ NPSHR (m):
        <input type="number" step="any" name="cv_npshr" value="4.60" placeholder="เช่น 4.60">
      </label>
    </div>
    <div data-m="cavitation">
      <label>อัตราการสูบ Q (m³/s):
        <input type="number" step="any" name="cv_q" value="0.015" placeholder="เช่น 0.015">
      </label>
    </div>
    <div data-m="cavitation">
      <label>ขนาดท่อดูด D (m):
        <input type="number" step="any" name="cv_d" value="0.20" placeholder="เช่น 0.20">
      </label>
    </div>
    <div data-m="cavitation">
      <label>สัมประสิทธิ์การสูญเสียในท่อดูด ΣKL:
        <input type="number" step="any" name="cv_kl" value="20.0" placeholder="เช่น 20.0">
      </label>
    </div>

    <div class="full" style="margin-top:14px;">
      <button type="submit" class="run" style="width:100%;padding:12px;font-size:16px;font-weight:700;background:var(--navy);color:#fff;border:none;border-radius:6px;cursor:pointer;">คำนวณผลลัพธ์ (Calculate)</button>
    </div>
  </form>

  <div id="calcout" class="calcout" style="margin-top:20px;"></div>

  <div class="pn" style="margin-top:40px;">
    <a href="#exam">← คลังข้อสอบ &amp; เก็งข้อสอบ</a>
    <a href="#ref">ตารางอ้างอิง &amp; คำศัพท์ →</a>
  </div>
</section>
'''
