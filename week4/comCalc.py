import math

n = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계: "))

if n == 1:
    expr = input("*** 수식을 입력하세요: ")
    result = eval(expr)
    print(expr+" 결과는 "+ str(result)+ " 입니다.")

elif n == 2:
    num1= int(input("*** 첫 번째 숫자를 입력하세요: "))
    num2= int(input("*** 두 번째 숫자를 입력하세요: "))


    if num1>num2:
        a=num2
        b=num1
    elif num1<num2:
        a=num1
        b=num2

    n = (b-a+1)
    s = (n*(a+b))//2

    print(str(a)+" +...+ "+str(b)+"는 "+ str(s)+"입니다.")