conCalc=int(input("입력할 진수 결정(16/10/8/2): "))
n = input("값 입력: ")

if conCalc == 16:
    n = int(n, 16)
elif conCalc == 10:
    n = int(n)
elif conCalc == 8:
    n = int(n, 8)
elif conCalc == 2:
    n = int(n, 2)

print("16진수 ==> ", hex(n))
print("10진수 ==>", n)
print("8진수 ==> ", oct(n))
print("2진수 ==> ", bin(n))


