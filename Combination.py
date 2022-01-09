# Combination 수동 구현
import math
n, r = map(int, input().split())

select = [1] * r + [0] * (n - r)
cnt = 0
for i in range(math.factorial(n) // (math.factorial(n - r) * math.factorial(r))):
    cnt += 1
    print(select, cnt)
    for j in range(n - 2, -1, -1):  # n-2는 끝에서 두 번째 자리부터 시작한다는 뜻.
        if select[j]:               # 현재 칸에 1이 있을 경우 다음 칸에 1이 없으면 시프트. 마지막 칸은 가지 않으니 괜찮음(이래서 n-2에서 시작)
            if select[j + 1] == 0:  # 시프트
                select[j] = 0
                select[j + 1] = 1
                if j + 2 <= n - 1 and 1 in select[j+2:]:    # 리스트 길이 검사, 길이 넘는다 해도 두 번째 조건은 건너뜀.
                    l = select[j+2:].count(1)               # 초기화 전 저장
                    select[j+2:] = [0] * len(select[j+2:])  # 뒷 자리 초기화(시프트 한 자리 바로 앞으로 이동시킴)
                    for k in range(l):                      # 뒤에 있는 1의 개수만큼 1 넣어줌
                        select[j+2+k] = 1
                break