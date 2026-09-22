#!/usr/bin/env python3
import sys

# จำนวนพารามิเตอร์ = จำนวนข้อมูลทั้งหมดใน sys.argv ลบด้วย 1 (ชื่อไฟล์)
num_params = len(sys.argv) - 1

print(f"Number of parameters: {num_params}.")