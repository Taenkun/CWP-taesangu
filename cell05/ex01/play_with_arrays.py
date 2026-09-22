#!/usr/bin/env python3

old_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้าง array ใหม่นำแต่ละค่าใน old_array มาบวก 2
new_array = [x + 2 for x in old_array]
print(f"Original array: {old_array}")
print(f"New array: {new_array}")