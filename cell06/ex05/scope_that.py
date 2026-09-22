#!/usr/bin/env python3

def add_one(num):
    num += 1
my_var = 99
print(my_var)
add_one(my_var)
print(my_var) #(ค่าจะยังคงเท่าเดิม เพราะ num เป็นแค่ตัวแปร local)