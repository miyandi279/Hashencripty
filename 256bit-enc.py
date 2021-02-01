#code : @Miyandi279
#youtube : Miyandi279
#Team : Bengkulu cyber team
#web team : http://bcset.rf.gd

import time as t
import timeit as tt 

def bit8t():
    bit8 = 255
    a = 0
    while a != bit8:
        print(a)
        a = a+1

def bit16t():
    bit16 = 65536
    a = 0
    while a != bit16:
        print(a)
        a = a+1

def bit32t():
    bit32 = 2147483647
    a = 0
    while a != bit32:
        print(a)
        a = a+1

def bit64t():
    bit64 = 9223372036854775807
    a = 0
    while a != bit64:
        print(a)
        a = a+1

def bit128t():
    bit128 = 340282366920938463463374607431770000000
    a = 0
    while a != bit128:
        print(a)
        a = a+1

def bit256t():
    bit256 = 115792089237316195423570985008687907853269984665640564039457584007913129639936
    a = 0
    while a != bit256:
        print(a)
        a = a+1


print("enter 1 to select 8 bit encoding")
t.sleep(1)
print("enter 2 to select 16 bit encoding")
t.sleep(1)
print("enter 3 to select 32 bit encoding")
t.sleep(1)
print("enter 4 to select 64 bit encoding")
t.sleep(1)
print("enter 5 to select 128 bit encoding")
t.sleep(1)
print("enter 6 to select 256 bit encoding")
t.sleep(1)
print("3 to 6 not recommended")

value = int(input("Enter the encoding you want to crack: "))

if value == 1:
    bit8t()
    timetaken = (tt.timeit(bit8t,number=1))
    print("the time taken to crack a 8bit encoding is {:1.2f} seconds".format(timetaken))

elif value == 2:
    bit16t()
    timetaken = (tt.timeit(bit16t,number=1))
    print("the time taken to crack a 16bit encoding is {:1.2f} seconds".format(timetaken))

elif value == 3:
    bit32t()
    timetaken = (tt.timeit(bit32t,number=1))
    print("the time taken to crack a 32bit encoding is {:1.2f} seconds".format(timetaken))

elif value == 4:
    bit64t()
    timetaken = (tt.timeit(bit64t,number=1))
    print("the time taken to crack a 64bit encoding is {:1.2f} seconds".format(timetaken))

elif value == 5:
    bit128t()
    timetaken = (tt.timeit(bit128t,number=1))
    print("the time taken to crack a 128bit encoding is {:1.2f} seconds".format(timetaken))

elif value == 6:
    bit256t()
    timetaken = (tt.timeit(bit16t,number=1))
    print("the time taken to crack a 256bit encoding is {:1.2f} seconds".format(timetaken))
else:
    print("Enter a valid number between 1 - 6")
