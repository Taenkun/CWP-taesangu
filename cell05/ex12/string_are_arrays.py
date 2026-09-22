#!/usr/bin/env python3
import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    z_result = ""
    
    # มองข้อความเหมือนเป็น array แล้ววนลูปดึงตัวอักษรทีละตัว
    for char in text:
        if char == 'z':
            z_result += "z"
            
    # ถ้าหาเจอ (z_result ไม่ว่าง)
    if z_result != "":
        print(z_result)
    else:
        print("none")
else:
    print("none")