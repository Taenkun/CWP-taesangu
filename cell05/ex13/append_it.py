#!/usr/bin/env python3
import sys

if len(sys.argv) <= 1:
    print("none")
else:
    # ตัดเอาเฉพาะพารามิเตอร์มาใช้งาน (ข้ามชื่อไฟล์)
    params = sys.argv[1:]
    
    for param in params:
        # คำนั้นลงท้ายด้วย "ism" อยู่แล้วหรือไม่
        if not param.endswith("ism"):
            # ถ้าไม่ได้ลงท้ายด้วย "ism" ให้เติมเข้าไป
            print(f"{param}ism")