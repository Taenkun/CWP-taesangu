#!/usr/bin/env python3
import sys

# มีพารามิเตอร์ต่อท้ายแค่ 1 ตัวหรือไม่
if len(sys.argv) == 2:
    # แปลงพารามิเตอร์ตัวแรกเป็นตัวพิมพ์ใหญ่
    print(sys.argv[1].upper())
else:
    # ถ้าไม่มีหรือมีมากกว่า 1 ตัว = none
    print("none")