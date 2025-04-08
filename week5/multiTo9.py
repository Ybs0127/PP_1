# 단 제목 출력
for dan in range(2, 10):
    print(f"#   {dan}단  #", end='\t')
print()

# 곱셈 결과 출력
for i in range(1, 10):  # 1부터 9까지
    for dan in range(2, 10):  # 2단부터 9단까지
        print(f"{dan} x {i} = {dan * i:2}", end='\t')
    print()
