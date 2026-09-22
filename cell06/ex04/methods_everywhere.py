#!/usr/bin/env python3
import sys

# ฟังก์ชันตัดข้อความให้เหลือแค่ 8 ตัวแรก (Slicing)
def shrink(text):
    print(text[:8])

# ฟังก์ชันเติม 'Z' ต่อท้ายจนกว่าจะครบ 8 ตัว
def enlarge(text):
    # หาจำนวนตัว 'Z' ที่ต้องเติมเพิ่ม แล้วนำมาต่อท้ายข้อความเดิม
    missing_chars = 8 - len(text)
    print(text + ('Z' * missing_chars))

if len(sys.argv) < 2:
    print("none")
else:
    # นำพารามิเตอร์มาเช็คทีละตัว
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            # ความยาวเท่ากับ 8 พอดี
            print(arg)