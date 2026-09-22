#!/usr/bin/env python3
import sys

# มีพารามิเตอร์น้อยกว่า 2 ตัวหรือไม่ (รวมชื่อไฟล์แล้วต้องไม่น้อยกว่า 3)
if len(sys.argv) < 3:
    print("none")
else:
    # ตัดเอาเฉพาะพารามิเตอร์ (ไม่เอาชื่อไฟล์ที่ index 0)
    params = sys.argv[1:]
    # reversed() เพื่อวนลูปถอยหลัง
    for param in reversed(params):
        print(param)