#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ต่อท้ายหรือไม่ (len มากกว่า 1)
if len(sys.argv) > 1:
    # พิมพ์พารามิเตอร์ตัวแรก ซึ่งอยู่ในตำแหน่ง index ที่ 1
    print(sys.argv[1])
else:
    # ถ้าไม่มีพารามิเตอร์ = none
    print("none")