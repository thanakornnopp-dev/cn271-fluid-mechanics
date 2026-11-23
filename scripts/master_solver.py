import math

class FluidSolver:
    G = 9.81
    RHO_WATER = 1000.0
    GAMMA_WATER = 9810.0

    @staticmethod
    def shear_stress(mu: float, v: float, h: float) -> float:
        """Tau = mu * (dv / dy)"""
        return mu * (v / h)

    @staticmethod
    def hydrostatic_pressure(h: float, gamma: float = None, sg: float = 1.0) -> float:
        """P = gamma * h = sg * gamma_w * h"""
        g = gamma if gamma is not None else sg * FluidSolver.GAMMA_WATER
        return g * h

    @staticmethod
    def hydrostatic_force_plane(h_cg: float, area: float, gamma: float = GAMMA_WATER) -> float:
        """F_R = gamma * h_cg * A"""
        return gamma * h_cg * area

    @staticmethod
    def center_of_pressure_rect(h_top: float, height: float, width: float, theta_deg: float = 90.0) -> dict:
        """
        Hydrostatic force and location for rectangular gate.
        h_top: vertical depth to top of gate
        height: length of gate along incline
        width: width into paper
        theta_deg: angle with horizontal
        """
        rad = math.radians(theta_deg)
        sin_th = math.sin(rad)
        area = height * width
        y_top = h_top / sin_th if sin_th > 0 else h_top
        y_cg = y_top + height / 2.0
        h_cg = y_cg * sin_th
        i_xc = (width * (height ** 3)) / 12.0
        y_cp = y_cg + i_xc / (y_cg * area)
        h_cp = y_cp * sin_th
        f_r = FluidSolver.GAMMA_WATER * h_cg * area
        return {
            "area": area,
            "y_cg": y_cg,
            "h_cg": h_cg,
            "y_cp": y_cp,
            "h_cp": h_cp,
            "f_r": f_r,
            "cp_from_cg": y_cp - y_cg
        }

    @staticmethod
    def jet_on_curved_vane(v: float, area: float, u: float = 0.0, turning_angle_deg: float = 180.0, rho: float = RHO_WATER) -> dict:
        """
        Jet hitting curved vane.
        v: absolute jet velocity
        u: vane velocity in jet direction
        turning_angle_deg: deflection angle (180 for U-turn)
        """
        v_rel = v - u
        mass_flow_hit = rho * area * v_rel
        angle_rad = math.radians(turning_angle_deg)
        f_x = mass_flow_hit * v_rel * (1.0 - math.cos(angle_rad))
        f_y = mass_flow_hit * v_rel * math.sin(angle_rad)
        f_res = math.sqrt(f_x**2 + f_y**2)
        return {
            "v_rel": v_rel,
            "mass_flow": mass_flow_hit,
            "f_x": f_x,
            "f_y": f_y,
            "f_resultant": f_res
        }

    @staticmethod
    def froude_scale(scale_ratio: float, v_m: float = None, v_p: float = None) -> dict:
        """
        Froude similarity: Fr_m = Fr_p => v_m / sqrt(g*L_m) = v_p / sqrt(g*L_p)
        scale_ratio = L_m / L_p (e.g. 1/80)
        """
        lambda_L = scale_ratio
        lambda_v = math.sqrt(lambda_L)
        lambda_Q = lambda_L ** 2.5
        lambda_F = lambda_L ** 3.0
        if v_m is not None:
            calc_v_p = v_m / lambda_v
            return {"lambda_L": lambda_L, "lambda_v": lambda_v, "v_p": calc_v_p, "lambda_Q": lambda_Q}
        if v_p is not None:
            calc_v_m = v_p * lambda_v
            return {"lambda_L": lambda_L, "lambda_v": lambda_v, "v_m": calc_v_m, "lambda_Q": lambda_Q}
        return {"lambda_L": lambda_L, "lambda_v": lambda_v, "lambda_Q": lambda_Q, "lambda_F": lambda_F}

    @staticmethod
    def reynolds_scale(scale_ratio: float, nu_ratio: float = 1.0, v_p: float = None, v_m: float = None) -> dict:
        """
        Reynolds similarity: Re_m = Re_p => (v_m * L_m)/nu_m = (v_p * L_p)/nu_p
        scale_ratio = L_m / L_p
        nu_ratio = nu_m / nu_p
        """
        lambda_L = scale_ratio
        lambda_v = nu_ratio / lambda_L
        if v_p is not None:
            calc_v_m = v_p * lambda_v
            return {"lambda_L": lambda_L, "lambda_v": lambda_v, "v_m": calc_v_m}
        if v_m is not None:
            calc_v_p = v_m / lambda_v
            return {"lambda_L": lambda_L, "lambda_v": lambda_v, "v_p": calc_v_p}
        return {"lambda_L": lambda_L, "lambda_v": lambda_v}

    @staticmethod
    def fluid_acceleration_field(x: float = 2.0, y: float = 1.0, z: float = 3.0, t: float = 0.5) -> dict:
        """
        Calculates velocity and acceleration for field:
        V = (10*x^2) i - (15*x*y) j + (32*t) k
        """
        # Velocity components
        u = 10.0 * (x ** 2)
        v = -15.0 * x * y
        w = 32.0 * t
        v_mag = math.sqrt(u**2 + v**2 + w**2)

        # Derivatives
        du_dx = 20.0 * x
        du_dy = 0.0
        du_dz = 0.0
        du_dt = 0.0

        dv_dx = -15.0 * y
        dv_dy = -15.0 * x
        dv_dz = 0.0
        dv_dt = 0.0

        dw_dx = 0.0
        dw_dy = 0.0
        dw_dz = 0.0
        dw_dt = 32.0

        # Acceleration components (Material Derivative)
        a_x = u * du_dx + v * du_dy + w * du_dz + du_dt
        a_y = u * dv_dx + v * dv_dy + w * dv_dz + dv_dt
        a_z = u * dw_dx + v * dw_dy + w * dw_dz + dw_dt
        a_mag = math.sqrt(a_x**2 + a_y**2 + a_z**2)

        return {
            "u": u,
            "v": v,
            "w": w,
            "v_mag": v_mag,
            "a_x": a_x,
            "a_y": a_y,
            "a_z": a_z,
            "a_mag": a_mag,
            "du_dx": du_dx,
            "dv_dx": dv_dx,
            "dv_dy": dv_dy,
            "dw_dt": dw_dt
        }

