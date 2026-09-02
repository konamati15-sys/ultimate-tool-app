import flet as ft
import math

# ==========================================
# 1. Logic Engine (คำนวณตามมาตรฐานวิศวกรรม)
# ==========================================
class ShapeCalculator:
    @staticmethod
    def box_volume(width: float, depth: float, height: float) -> float:
        return width * depth * height

    @staticmethod
    def cylinder_volume(radius: float, height: float) -> float:
        return math.pi * (radius ** 2) * height

    @staticmethod
    def polygon_deduction_volume(width: float, depth: float, height: float, deduct_percent: float) -> float:
        base_volume = width * depth * height
        deduction_multiplier = (100 - deduct_percent) / 100
        return base_volume * deduction_multiplier

class CapacityConverter:
    @staticmethod
    def mm3_to_liters(mm3_volume: float) -> float:
        return mm3_volume / 1000000

# ==========================================
# 2. UI View & Controller 
# ==========================================
def main(page: ft.Page):
    page.title = "Ultimate Tool App"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width = 400
    page.window_height = 850
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO 

    # =====================================================================
    # 📌 ระบบเมนูสลับโปรแกรมหลัก (3 โปรแกรม)
    # =====================================================================
    def switch_main_app(index):
        view_capacity.visible = (index == 0)
        view_electrical.visible = (index == 1)
        view_air.visible = (index == 2)
        
        btn_app_cap.style = ft.ButtonStyle(bgcolor="green" if index == 0 else "transparent", color="white" if index == 0 else "green")
        btn_app_elec.style = ft.ButtonStyle(bgcolor="green" if index == 1 else "transparent", color="white" if index == 1 else "green")
        btn_app_air.style = ft.ButtonStyle(bgcolor="green" if index == 2 else "transparent", color="white" if index == 2 else "green")
        page.update()

    btn_app_cap = ft.ElevatedButton("📦 ความจุ", on_click=lambda e: switch_main_app(0), style=ft.ButtonStyle(bgcolor="green", color="white"), height=40)
    btn_app_elec = ft.ElevatedButton("⚡ ไฟฟ้า", on_click=lambda e: switch_main_app(1), style=ft.ButtonStyle(color="green"), height=40)
    btn_app_air = ft.ElevatedButton("💨 ระบบฮู้ดลม", on_click=lambda e: switch_main_app(2), style=ft.ButtonStyle(color="green"), height=40)
    
    main_app_menu = ft.Container(
        content=ft.Row([btn_app_cap, btn_app_elec, btn_app_air], alignment=ft.MainAxisAlignment.CENTER),
        padding=10,
        margin=20
    )

    # =====================================================================
    # 📌 ส่วนที่ 1: แอปคำนวณความจุ (Capacity App)
    # =====================================================================
    cap_header = ft.Text("📦 คำนวณความจุ", size=24, weight=ft.FontWeight.BOLD)
    cap_result_text = ft.Text("พร้อมคำนวณ", size=20, weight=ft.FontWeight.BOLD, color="grey")

    box_w = ft.TextField(label="ความกว้าง (w) มม.", keyboard_type=ft.KeyboardType.NUMBER)
    box_d = ft.TextField(label="ความลึก (d) มม.", keyboard_type=ft.KeyboardType.NUMBER)
    box_h = ft.TextField(label="ความสูงรวม (h) มม.", keyboard_type=ft.KeyboardType.NUMBER)

    cyl_dia = ft.TextField(label="เส้นผ่านศูนย์กลาง (เต็มวง) มม.", keyboard_type=ft.KeyboardType.NUMBER)
    cyl_h = ft.TextField(label="ความสูงรวม (h) มม.", keyboard_type=ft.KeyboardType.NUMBER)

    poly_edges = ft.TextField(label="ระบุจำนวนเหลี่ยม (เช่น 5, 6, 8)", keyboard_type=ft.KeyboardType.NUMBER)
    poly_deduct = ft.TextField(label="ใส่เปอร์เซ็นต์ที่ต้องการหักออก (%)", keyboard_type=ft.KeyboardType.NUMBER)
    poly_w = ft.TextField(label="ความกว้างภายนอก (w) มม.", keyboard_type=ft.KeyboardType.NUMBER)
    poly_d = ft.TextField(label="ความลึกภายนอก (d) มม.", keyboard_type=ft.KeyboardType.NUMBER)
    poly_h = ft.TextField(label="ความสูงรวม (h) มม.", keyboard_type=ft.KeyboardType.NUMBER)

    box_view = ft.Column([box_w, box_d, box_h], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=True)
    cyl_view = ft.Column([cyl_dia, cyl_h], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)
    poly_view = ft.Column([
        ft.Text("📌 ตั้งค่าหักลบ", color="blue", weight=ft.FontWeight.BOLD),
        poly_edges, poly_deduct,
        ft.Divider(height=5, color="transparent"),
        ft.Text("📌 ขนาดพื้นที่ภายนอก (W x D x H)", color="blue", weight=ft.FontWeight.BOLD),
        poly_w, poly_d, poly_h
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)

    current_cap_tab = 0

    def set_cap_tab(index):
        nonlocal current_cap_tab
        current_cap_tab = index
        box_view.visible = (index == 0)
        cyl_view.visible = (index == 1)
        poly_view.visible = (index == 2)
        btn_box.style = ft.ButtonStyle(bgcolor="blue" if index == 0 else "transparent", color="white" if index == 0 else "blue")
        btn_cyl.style = ft.ButtonStyle(bgcolor="blue" if index == 1 else "transparent", color="white" if index == 1 else "blue")
        btn_poly.style = ft.ButtonStyle(bgcolor="blue" if index == 2 else "transparent", color="white" if index == 2 else "blue")
        cap_result_text.value = "พร้อมคำนวณ"
        cap_result_text.color = "grey"
        page.update()

    btn_box = ft.TextButton("🟦 สี่เหลี่ยม", on_click=lambda e: set_cap_tab(0), style=ft.ButtonStyle(bgcolor="blue", color="white"))
    btn_cyl = ft.TextButton("⭕ วงกลม", on_click=lambda e: set_cap_tab(1), style=ft.ButtonStyle(color="blue"))
    btn_poly = ft.TextButton("💠 หลายเหลี่ยม", on_click=lambda e: set_cap_tab(2), style=ft.ButtonStyle(color="blue"))
    cap_tab_menu = ft.Row([btn_box, btn_cyl, btn_poly], alignment=ft.MainAxisAlignment.CENTER)

    def calculate_capacity(e):
        try:
            vol_mm3 = 0.0
            if current_cap_tab == 0:
                vol_mm3 = ShapeCalculator.box_volume(float(box_w.value), float(box_d.value), float(box_h.value))
            elif current_cap_tab == 1:
                r = float(cyl_dia.value) / 2
                vol_mm3 = ShapeCalculator.cylinder_volume(r, float(cyl_h.value))
            elif current_cap_tab == 2:
                deduct = float(poly_deduct.value)
                vol_mm3 = ShapeCalculator.polygon_deduction_volume(float(poly_w.value), float(poly_d.value), float(poly_h.value), deduct)

            liters = CapacityConverter.mm3_to_liters(vol_mm3)
            cap_result_text.value = f"✅ ความจุ: {liters:,.2f} ลิตร"
            cap_result_text.color = "green"
        except Exception as ex:
            cap_result_text.value = "❌ ข้อมูลไม่ครบหรือผิดพลาด"
            cap_result_text.color = "red"
        page.update()

    calc_cap_btn = ft.ElevatedButton("คำนวณผลลัพธ์", on_click=calculate_capacity, width=300, height=45)

    view_capacity = ft.Column([
        cap_header, cap_tab_menu, ft.Divider(height=5, color="transparent"),
        box_view, cyl_view, poly_view, ft.Divider(height=5, color="transparent"),
        calc_cap_btn, ft.Divider(height=5, color="transparent"), cap_result_text
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=True)


    # =====================================================================
    # 📌 ส่วนที่ 2: แอปคำนวณไฟฟ้า (Electrical App)
    # =====================================================================
    elec_header = ft.Text("⚡ คำนวณไฟฟ้า", size=24, weight=ft.FontWeight.BOLD)
    elec_result_text = ft.Text("พร้อมคำนวณ", size=20, weight=ft.FontWeight.BOLD, color="grey")

    elec_w = ft.TextField(label="กำลังไฟฟ้า (วัตต์ - W)", keyboard_type=ft.KeyboardType.NUMBER)
    elec_v1 = ft.TextField(label="แรงดัน (V) *ไฟบ้านปกติ 220", value="220", keyboard_type=ft.KeyboardType.NUMBER)
    
    elec_a = ft.TextField(label="กระแสไฟฟ้า (แอมป์ - A)", keyboard_type=ft.KeyboardType.NUMBER)
    elec_v2 = ft.TextField(label="แรงดัน (V) *ไฟบ้านปกติ 220", value="220", keyboard_type=ft.KeyboardType.NUMBER)

    view_find_a = ft.Column([elec_w, elec_v1], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=True)
    view_find_w = ft.Column([elec_a, elec_v2], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)

    current_elec_tab = 0

    def set_elec_tab(index):
        nonlocal current_elec_tab
        current_elec_tab = index
        view_find_a.visible = (index == 0)
        view_find_w.visible = (index == 1)
        btn_find_a.style = ft.ButtonStyle(bgcolor="blue" if index == 0 else "transparent", color="white" if index == 0 else "blue")
        btn_find_w.style = ft.ButtonStyle(bgcolor="blue" if index == 1 else "transparent", color="white" if index == 1 else "blue")
        elec_result_text.value = "พร้อมคำนวณ"
        elec_result_text.color = "grey"
        page.update()

    btn_find_a = ft.TextButton("🔍 หาแอมป์ (A)", on_click=lambda e: set_elec_tab(0), style=ft.ButtonStyle(bgcolor="blue", color="white"))
    btn_find_w = ft.TextButton("🔍 หาวัตต์ (W)", on_click=lambda e: set_elec_tab(1), style=ft.ButtonStyle(color="blue"))
    elec_tab_menu = ft.Row([btn_find_a, btn_find_w], alignment=ft.MainAxisAlignment.CENTER)

    def calculate_electrical(e):
        try:
            if current_elec_tab == 0:
                w = float(elec_w.value)
                v = float(elec_v1.value)
                amps = w / v
                elec_result_text.value = f"✅ ใช้กระแส: {amps:,.2f} แอมป์ (A)"
            else:
                a = float(elec_a.value)
                v = float(elec_v2.value)
                watts = a * v
                kw = watts / 1000
                elec_result_text.value = f"✅ กำลังไฟ: {watts:,.0f} W ({kw:,.2f} kW)"
            elec_result_text.color = "green"
        except Exception as ex:
            elec_result_text.value = "❌ ข้อมูลไม่ครบหรือผิดพลาด"
            elec_result_text.color = "red"
        page.update()

    calc_elec_btn = ft.ElevatedButton("คำนวณไฟฟ้า", on_click=calculate_electrical, width=300, height=45)

    view_electrical = ft.Column([
        elec_header, elec_tab_menu, ft.Divider(height=5, color="transparent"),
        view_find_a, view_find_w, ft.Divider(height=5, color="transparent"),
        calc_elec_btn, ft.Divider(height=5, color="transparent"), elec_result_text
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)


    # =====================================================================
    # 📌 ส่วนที่ 3: แอปคำนวณฮู้ด & มอเตอร์ (ใช้สูตรมาตรฐานความยาวฮู้ด ASHRAE)
    # =====================================================================
    hood_header = ft.Text("💨 คำนวณฮู้ด & มอเตอร์", size=24, weight=ft.FontWeight.BOLD)
    hood_result_text = ft.Text("พร้อมคำนวณ", size=16, weight=ft.FontWeight.BOLD, color="grey")

    hood_w = ft.TextField(label="ความกว้างฮู้ด (มม.)", keyboard_type=ft.KeyboardType.NUMBER)
    hood_d = ft.TextField(label="ความลึกฮู้ด (มม.)", keyboard_type=ft.KeyboardType.NUMBER)
    hood_h_back = ft.TextField(label="ความสูงด้านหลัง (มม.)", value="500", keyboard_type=ft.KeyboardType.NUMBER)
    hood_h_front = ft.TextField(label="ความสูงด้านหน้า (มม.)", value="150", keyboard_type=ft.KeyboardType.NUMBER)
    duct_dist = ft.TextField(label="ระยะทางท่อลมไปภายนอก (เมตร)", value="10", keyboard_type=ft.KeyboardType.NUMBER)

    def calculate_hood(e):
        try:
            w_m = float(hood_w.value) / 1000  # แปลงเป็นเมตร
            d_m = float(hood_d.value) / 1000
            h_back_m = float(hood_h_back.value) / 1000
            h_front_m = float(hood_h_front.value) / 1000
            dist = float(duct_dist.value)

            if w_m <= 0 or d_m <= 0:
                raise ValueError("ขนาดฮู้ดต้องมากกว่า 0")

            # 1. คำนวณตามมาตรฐาน ASHRAE (Linear Meter Method)
            # อัตราลมพื้นฐาน ~350 CFM ต่อความยาวฮู้ด 1 เมตร (สำหรับความลึกมาตรฐาน 0.9 ม.)
            base_cfm_per_meter = 350
            standard_depth = 0.9
            
            # ปรับสัดส่วนตามความลึกจริงและความลาดเอียงของฮู้ด
            depth_factor = d_m / standard_depth
            slope_bonus = 1 + (((h_back_m + h_front_m) / 2) * 0.1)
            
            base_cfm = w_m * base_cfm_per_meter * depth_factor * slope_bonus

            # 2. ชดเชยแรงต้านทานตามระยะทางท่อลม (เพิ่ม 2.5% ต่อระยะทาง 1 เมตร)
            friction_multiplier = 1 + (dist * 0.025)
            required_cfm = base_cfm * friction_multiplier

            if required_cfm <= 0:
                hood_result_text.value = "✅ ปริมาณลมดูด: 0 CFM (ไม่ต้องใช้มอเตอร์)"
                hood_result_text.color = "orange"
                page.update()
                return

            # 3. เทียบขนาดมอเตอร์จริงตามสเปกโบลเวอร์ตลาด (พัดลม 1 HP รองรับได้ราว 700-800 CFM ที่แรงดันปานกลาง)
            # ทำให้ฮู้ด 3 เมตร (~1,100 CFM) ลงตัวพอดีที่ 1.5 หรือ 2 แรงม้า
            exhaust_hp = required_cfm / 750

            if exhaust_hp <= 0.5:
                recommended_exhaust = "1/2 แรง (0.5 HP)"
            elif exhaust_hp <= 1.0:
                recommended_exhaust = "1 แรง (1.0 HP)"
            elif exhaust_hp <= 1.5:
                recommended_exhaust = "1.5 แรง (1.5 HP)"
            elif exhaust_hp <= 2.0:
                recommended_exhaust = "2 แรง (2.0 HP)"
            elif exhaust_hp <= 3.0:
                recommended_exhaust = "3 แรง (3.0 HP)"
            else:
                recommended_exhaust = f"{exhaust_hp:,.1f} แรง (HP)"

            # 4. ลม Fresh Air (เติมอากาศ) คิดเป็น 75% ของลมดูดออกเพื่อให้เกิดแรงดันลบพอดี
            fresh_cfm = required_cfm * 0.75
            fresh_hp = fresh_cfm / 750
            
            if fresh_hp <= 0.5:
                recommended_fresh = "1/2 แรง (0.5 HP)"
            elif fresh_hp <= 1.0:
                recommended_fresh = "1 แรง (1.0 HP)"
            elif fresh_hp <= 1.5:
                recommended_fresh = "1.5 แรง (1.5 HP)"
            elif fresh_hp <= 2.0:
                recommended_fresh = "2 แรง (2.0 HP)"
            else:
                recommended_fresh = f"{fresh_hp:,.1f} แรง (HP)"

            hood_result_text.value = (
                f"✅ ปริมาณลมดูด: {required_cfm:,.0f} CFM\n"
                f"🌀 มอเตอร์ดูดควัน: แนะนำใช้ขนาด {recommended_exhaust}\n\n"
                f"🍃 ลมเติมอากาศ (Fresh Air): {fresh_cfm:,.0f} CFM\n"
                f"🍃 มอเตอร์เติมลม: แนะนำใช้ขนาด {recommended_fresh}"
            )
            hood_result_text.color = "green"
        except Exception as ex:
            hood_result_text.value = "❌ กรุณากรอกตัวเลขให้ถูกต้องครบถ้วน"
            hood_result_text.color = "red"
        page.update()

    calc_hood_btn = ft.ElevatedButton("คำนวณฮู้ด & มอเตอร์", on_click=calculate_hood, width=300, height=45)

    view_air = ft.Column([
        hood_header, 
        ft.Divider(height=5, color="transparent"),
        hood_w, hood_d, hood_h_back, hood_h_front, duct_dist,
        ft.Divider(height=5, color="transparent"),
        calc_hood_btn, 
        ft.Divider(height=5, color="transparent"), 
        hood_result_text
    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, visible=False)


    # =====================================================================
    # นำทุกอย่างมารวมลงหน้าจอหลัก
    # =====================================================================
    page.add(
        ft.SafeArea(
            ft.Column([
                main_app_menu,
                view_capacity, 
                view_electrical,
                view_air
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )

ft.run(main)