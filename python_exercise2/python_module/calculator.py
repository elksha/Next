from module import *

def hello():
    a = int(input("""
  Menu
--------
 1: add
 2: sub
 3: multiply
 4: divide
 5: stop
: """))
    b = FourCal(0, 0)
    b.first = int(input("num1:"))
    b.second = int(input("num2:"))
    if a == 1:
        print(b.add())
    elif a == 2:
        print(b.sub())
    elif a == 3:
        print(b.mul())
    elif a == 4:
        print(b.div())
    elif a == 5:
        pass
    else:
        print("값을 제대로 입력해주세요.")
        hello()

hello()