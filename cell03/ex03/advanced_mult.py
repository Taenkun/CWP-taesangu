#!/usr/bin/env python3
import sys

# เช็คว่ามีการใส่ข้อความต่อท้ายคำสั่งรันโปรแกรมหรือไม่
if len(sys.argv) > 1:
    print("none")
else:
    # while loop ตัวที่ 1 (ตัวตั้ง)
    i = 0
    while i <= 10:
        print(f"Table de {i}:", end="")
        
        # while loop ตัวที่ 2 (ตัวคูณ)
        j = 0
        while j <= 10:
            print(f" {i * j}", end="")
            j += 1
            
        print() # ขึ้นบรรทัดใหม่เมื่อจบสูตรคูณแต่ละแม่
        i += 1