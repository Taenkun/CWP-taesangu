#!/usr/bin/env python3
import sys

if len(sys.argv) <= 1:
    print("none")
else:
    # ดึงเฉพาะพารามิเตอร์มาเก็บไว้
    params = sys.argv[1:]
    # แสดงจำนวนพารามิเตอร์ทั้งหมด
    print(f"parameters: {len(params)}")
    # for loop แสดงพารามิเตอร์ทีละตัวพร้อมความยาวตัวอักษร
    for param in params:
        print(f"{param}: {len(param)}")