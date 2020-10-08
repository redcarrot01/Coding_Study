def solution(n, times):
    low =1
    high = max(times)*n
    answer = 0
    
    while low <= high:
        # 한 심사관에게 주어진 시간
        mid = (low+high) //2
        people = 0
        for i in times:
            # 각 심사관 마다 몇명 가능한지
            people += mid//i
            # 모든 사람이 심사 가능 하다면 벗어나기
            if people >= n:
                break
        # 시간 줄여보기        
        if people >=n:
            answer = mid
            high = mid -1
        # 모든 사람이 심사 할 수 없는 경우 시간 늘리기    
        else:
            low = mid + 1
    
    
    return answer
