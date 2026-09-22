#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # .count() นับจำนวน keyword ใน text
    count = text.count(keyword)
    
    if count > 0:
        print(count)
    else:
        print("none")
else:
    # ถ้าพารามิเตอร์ไม่ครบ 2 ตัว ให้แสดง none
    print("none")