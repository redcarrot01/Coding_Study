# 프로그래머스 1단계
#1.  가운데 글자 가져오기

def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2+1]

print(string_middle("power"))
print(string_middle("powr"))
#s[2:4] => 2, 3 까지


def string_middle(str):
    a=len(str)
    if a%2 == 0:
        a =(a-2)/2
    else:
        a= (a-1)/2
    return str[int(a) : -int(a)]


def solution(s):
    answer = ''
    if len(s) %2 ==0:
        answer += s[len(s)//2-1: len(s)//2+1]
    else:
        answer+= s[len(s)//2]
    return answer

#2. 모의고사
def solution(answers):
    answer = []

    n1 = [1, 2, 3, 4,5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1 = c2 = c3 = 0

    for i in range(len(answers)):
        if answers[i]== n1[i%5]:
            c1+=1
        if answers[i] == n2[i % 5]:
            c2 +=1
        if answers[i] == n3[i % 5]:
            c3 +=1
    maxed = max(c1, c2,c3)

    if maxed == c1: answer.append(1)
    if maxed == c2: answer.append(2)
    if maxed == c3: answer.append(3)

    return answer