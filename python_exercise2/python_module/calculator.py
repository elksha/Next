from module import *

def hello():
    a = input("""
  Menu
--------
 1: add
 2: sub
 3: multiply
 4: divide
 5: stop
: """)
    if type(a) != int:
        print("값을 제대로 입력해주세요.")
        hello()
    if int(a) == 5:
        exit()
    if int(a) != 1 and int(a) != 2 and int(a) != 3 and int(a) != 4 and int(a) != 5:
        print("값을 제대로 입력해주세요.")
        hello()
    b = FourCal(0, 0)
    b.first = int(input("num1:"))
    b.second = int(input("num2:"))
    if int(a) == 1:
        print(b.add())
        hello()
    elif int(a) == 2:
        print(b.sub())
        hello()
    elif int(a) == 3:
        print(b.mul())
        hello()
    elif int(a) == 4:
        print(b.div())
        hello()

hello()
