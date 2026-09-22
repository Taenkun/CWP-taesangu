#!/usr/bin/env python3

old_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = [x + 2 for x in original_array if x > 5]

print(old_array)
# ทำให้เป็น set เพื่อตัดค่าที่ซ้ำกันออก
print(set(new_array))