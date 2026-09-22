#!/usr/bin/env python3

user_input = input("What you gotta say? : ")

# สร้าง infinite loop
while True:
    # ถ้าข้อความที่รับมาคือ "STOP" ให้หยุดทำงาน (break)
    if user_input == "STOP":
        break
    # ถ้าไม่ใช่ "STOP" ให้ถามต่อแล้วเก็บค่าทับตัวแปรเดิม
    user_input = input("I got that! Anything else? : ")