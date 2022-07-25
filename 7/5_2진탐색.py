N = 5  # 기계부품
nums = [8, 3, 7, 9, 2]  # 부품번호
M = 3  # 확인개수
chks = [5, 7, 9]  # 부품번호
nums.sort()
chks.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in chks:
    result = binary_search(nums, i , 0, N-1)
    if result != None:
        print('yes')
    else:
        print('no')