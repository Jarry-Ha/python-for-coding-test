N = 5  # 기계부품
nums = [8, 3, 7, 9, 2]  # 부품번호
M = 3  # 확인개수
chks = [3, 7, 9]  # 부품번호

for i in chks:
    if i in nums:
        print('yes')
    else: 
        print('no')
