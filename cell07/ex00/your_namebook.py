#!/usr/bin/env python3

def array_of_names(name_dict):
    # ใช้ List เพื่อสร้าง list ของชื่อเต็ม
    # .capitalize() ตัวอักษรแรกของชื่อและนามสกุลเป็นตัวพิมพ์ใหญ่
    return [f"{first_name.capitalize()} {last_name.capitalize()}" for first_name, last_name in name_dict.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))