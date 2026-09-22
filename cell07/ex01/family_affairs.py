#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # ใช้ filter ร่วมกับ lambda เพื่อกรองเอาเฉพาะชื่อ name ที่มีค่า value เป็น red
    # family_dict.keys() จะดึงรายชื่อทั้งหมดมาให้ filter ตรวจทีละคน
    redheads = filter(lambda name: family_dict[name] == "red", family_dict.keys())
    
    # แปลงผลลัพธ์ที่ได้จากการ filter ให้กลายเป็น List แล้วส่งค่ากลับ
    return list(redheads)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))