# lambda 사용해서 숫자의 가장 맨 앞자리 내림차순으로 정렬
# 문제점: 3과 30 중에 3이 먼저 와야 큰 숫자가 나오는데 첫 자리만 비교하면 안됨 (330, 303) 

def solution(numbers):
    answer = sorted(numbers, key=lambda x: str(x) * 3, reverse=True)
    return "0" if answer[0] == 0 else "".join(map(str, answer))