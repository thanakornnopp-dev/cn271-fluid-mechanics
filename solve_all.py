import math

g = 9.81
nu = 1e-6 # m^2/s
rho = 1000.0
gamma = 9810.0

def colebrook(Re, k_over_d):
    if Re < 2000:
        return 64.0 / Re
    # Swamee-Jain start
    f = 0.25 / (math.log10(k_over_d / 3.7 + 5.74 / (Re**0.9)))**2
    for _ in range(30):
        rhs = -2.0 * math.log10(k_over_d / 3.7 + 2.51 / (Re * math.sqrt(f)))
        f_new = (1.0 / rhs)**2
        if abs(f_new - f) < 1e-8:
            break
        f = f_new
    return f

print("--- PROBLEM 1: Series inclined pipes ---")
# Pipe 1: D=0.4, L=80, k=0.08mm
# Pipe 2: D=0.5, L=120, k=0.15mm
# Pipe 3: D=0.3, L=80, k=0.12mm
D1, L1, k1 = 0.4, 80.0, 0.08e-3
D2, L2, k2 = 0.5, 120.0, 0.15e-3
D3, L3, k3 = 0.3, 80.0, 0.12e-3

kd1 = k1 / D1 # 0.0002
kd2 = k2 / D2 # 0.0003
kd3 = k3 / D3 # 0.0004
print(f"k/D: kd1={kd1:.6f}, kd2={kd2:.6f}, kd3={kd3:.6f}")

# Energy equation:
# (PA - PB)/gamma - zB = [ v3^2/2g - v1^2/2g + f1*L1/D1*v1^2/2g + f2*L2/D2*v2^2/2g + f3*L3/D3*v3^2/2g + K12*v1^2/2g + K23*v3^2/2g ]
# v2 = (0.4/0.5)^2 * v1 = 0.64 * v1
# v3 = (0.4/0.3)^2 * v1 = (16/9) * v1 = 1.77777778 * v1
# With teacher approximation: 1.78
# Let's test both exact and 1.78:
zB = 280.0 * math.sin(math.radians(5.0))
dHead = 245.25e3 / 9810.0 - zB
print(f"zB = {zB:.4f} m, dHead = {dHead:.4f} m")

# Let's iterate starting with initial guess of fully turbulent f from chart:
# For kd1=0.0002 -> f_turb ~ 0.014
# For kd2=0.0003 -> f_turb ~ 0.015
# For kd3=0.0004 -> f_turb ~ 0.016
f1, f2, f3 = 0.014, 0.015, 0.016
for it in range(1, 6):
    coeff = (1.78**2 - 1.0) + f1*(L1/D1) + f2*(L2/D2)*(0.64**2) + f3*(L3/D3)*(1.78**2) + 0.15 + 0.35*(1.78**2)
    # dHead = coeff * v1^2 / (2g)
    v1 = math.sqrt(2 * g * dHead / coeff)
    v2 = 0.64 * v1
    v3 = 1.78 * v1
    Re1 = v1 * D1 / nu
    Re2 = v2 * D2 / nu
    Re3 = v3 * D3 / nu
    f1_new = colebrook(Re1, kd1)
    f2_new = colebrook(Re2, kd2)
    f3_new = colebrook(Re3, kd3)
    print(f"Iter {it}: v1={v1:.4f}, v2={v2:.4f}, v3={v3:.4f} | Re1={Re1:.1e}, Re2={Re2:.1e}, Re3={Re3:.1e} | f1={f1_new:.4f}, f2={f2_new:.4f}, f3={f3_new:.4f}")
    f1, f2, f3 = f1_new, f2_new, f3_new

print("\n--- PROBLEM 2: Constant diameter pipe (find D) ---")
# z2 - z1 = 10, L = 1500, Q = 0.14 m3/s, k = 0.9 mm, P1 = 105.13 kPa, P2 = 0 (open jet)
# If open jet: P2 = 0, and exit loss is 0 (point 2 is at the exit section inside the pipe, or jet)
# If point 2 is just inside exit: P2 = 0, v2 = v1 = v -> v^2/2g cancels.
# hf = P1/gamma - 10 = 105130/9810 - 10 = 10.7166 - 10 = 0.7166 m.
hf = 105.13e3 / gamma - 10.0
print(f"hf = {hf:.4f} m")

# hf = f * (L/D) * (v^2/(2g))
# v = Q / (pi/4 * D^2) = 4Q / (pi D^2)
# v^2 = 16 Q^2 / (pi^2 D^4)
# hf = f * L / D * 16 Q^2 / (2 g pi^2 D^4) = (8 f L Q^2) / (g pi^2 D^5)
# D^5 = (8 f L Q^2) / (g pi^2 hf)
# D = [ (8 f L Q^2) / (pi^2 g hf) ]^(1/5)
f_guess = 0.02
for it in range(1, 8):
    D = ((8 * f_guess * 1500.0 * (0.14**2)) / (math.pi**2 * g * hf))**(0.2)
    v = 0.14 / (math.pi * (D**2) / 4.0)
    Re = v * D / nu
    kd = 0.9e-3 / D
    f_new = colebrook(Re, kd)
    print(f"Iter {it}: D={D:.4f} m ({D*1000:.1f} mm), v={v:.4f} m/s, Re={Re:.2e}, k/D={kd:.5f}, f={f_new:.4f}")
    if abs(f_new - f_guess) < 1e-5:
        break
    f_guess = f_new

print("\n--- PROBLEM: Two huge tanks (find D) ---")
# Q = 12 m3/s, k = 0.48 mm, L = 120 m, angle = 12 deg
# hf = 45 - (120*sin(12 deg) + 16.5) = 45 - (24.949 + 16.5) = 3.551 m
hf_tanks = 45.0 - (120.0 * math.sin(math.radians(12.0)) + 16.5)
print(f"hf_tanks = {hf_tanks:.4f} m")
f_guess = 0.02
for it in range(1, 8):
    D = ((8 * f_guess * 120.0 * (12.0**2)) / (math.pi**2 * g * hf_tanks))**(0.2)
    v = 12.0 / (math.pi * (D**2) / 4.0)
    Re = v * D / (1e-3 / 1000.0)
    kd = 0.48e-3 / D
    f_new = colebrook(Re, kd)
    print(f"Iter {it}: D={D:.4f} m ({D*1000:.1f} mm), v={v:.4f} m/s, Re={Re:.2e}, k/D={kd:.5f}, f={f_new:.4f}")
    if abs(f_new - f_guess) < 1e-5:
        break
    f_guess = f_new

print("\n--- PROBLEM 3: Parallel & Series Pipes (AA to BB) ---")
# Pipe 1: D=0.9, L=900, k=0.90mm -> k/D = 0.001
# Pipe 2: D=0.8, L=800, k=0.32mm -> k/D = 0.0004
# Pipe 3: D=0.6, L=800, k=0.48mm -> k/D = 0.0008
# Pipe 4: D=?, L=1000, k=0.96mm
# Given h3 = 0.42 m. Parallel -> h2 = h3 = 0.42 m.
# Between A and B on Pipe 4: L_AB = 300 m, zB - zA = 10 m, PA = 910 kPa, PB = 811.41 kPa
# PA/gamma - PB/gamma = (910 - 811.41)*1e3 / 9810 = 98.59e3 / 9810 = 10.04995 m
# h_AB = 10.04995 - 10.0 = 0.04995 m ~ 0.05 m
# h4 = h_AB * (1000 / 300) = 0.05 * 10 / 3 = 0.1667 m ~ 0.17 m
h_AB = (910e3 - 811.41e3)/gamma - 10.0
h4 = h_AB * (1000.0 / 300.0)
print(f"h_AB = {h_AB:.4f} m, h4 = {h4:.4f} m")

# For Pipe 3: h3 = 0.42 m
# h3 = f3 * (L3/D3) * (v3^2 / 2g) => v3 = sqrt( 2*g*h3 / (f3 * L3/D3) )
kd3 = 0.48e-3 / 0.6 # 0.0008
# solve for v3
f3 = 0.019 # guess from chart for k/d = 0.0008
for _ in range(10):
    v3 = math.sqrt(2 * g * 0.42 / (f3 * 800.0 / 0.6))
    Re3 = v3 * 0.6 / nu
    f3 = colebrook(Re3, kd3)
Q3 = v3 * math.pi * (0.6**2) / 4.0
print(f"Pipe 3: v3={v3:.4f} m/s, Re3={Re3:.2e}, f3={f3:.4f}, Q3={Q3:.4f} m3/s")

# For Pipe 2: h2 = 0.42 m
kd2 = 0.32e-3 / 0.8 # 0.0004
f2 = 0.016
for _ in range(10):
    v2 = math.sqrt(2 * g * 0.42 / (f2 * 800.0 / 0.8))
    Re2 = v2 * 0.8 / nu
    f2 = colebrook(Re2, kd2)
Q2 = v2 * math.pi * (0.8**2) / 4.0
print(f"Pipe 2: v2={v2:.4f} m/s, Re2={Re2:.2e}, f2={f2:.4f}, Q2={Q2:.4f} m3/s")

# Total Q = Q2 + Q3
Q_total = Q2 + Q3
print(f"Q_total = Q1 = Q4 = {Q_total:.4f} m3/s")

# For Pipe 1: D=0.9, L=900, k=0.90mm -> k/D = 0.001
kd1 = 0.90e-3 / 0.9 # 0.001
v1 = Q_total / (math.pi * (0.9**2) / 4.0)
Re1 = v1 * 0.9 / nu
f1 = colebrook(Re1, kd1)
h1 = f1 * (900.0 / 0.9) * (v1**2 / (2 * g))
print(f"Pipe 1: v1={v1:.4f} m/s, Re1={Re1:.2e}, f1={f1:.4f}, h1={h1:.4f} m")

# Total head loss AA to BB:
h_total = h1 + 0.42 + h4
print(f"Total head loss AA to BB = h1 + h2 + h4 = {h1:.4f} + 0.42 + {h4:.4f} = {h_total:.4f} m")
