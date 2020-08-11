# k번째수

def solution(array, commands):
    answer= []

    for command in commands:
        n_array = array[command[0]-1: command[1]]
        n_array.sort()
        answer.append(command[2]-1)
    return answer

def solution(array, commands):
    answer =[]
    for command in commands:
        i, j, k=command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

#같은 숫자는 싫어
def solution(arr):
    # answer배열에 arr 배열의 첫번째 원소 저장
    # answer와 arr 배열 비교
    answer = arr[:1]
    for i in arr:
        if answer[-1] == i:
            continue
        answer.append(i)

    return answer
