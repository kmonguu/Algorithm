# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 할 때, 무지가 개발하려는 시스템은 다음과 같다.

# 각 유저는 한 번에 한 명의 유저를 신고할 수 있다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.
# 다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

# 신고 예시
# 유저 ID	        유저가 신고한 ID	        정지된 ID
# "muzi"  	     ["frodo", "neo"]	   ["frodo", "neo"]
# "frodo"	     ["neo"]	           ["neo"]
# "apeach"	     ["muzi", "frodo"]	   ["frodo"]
# "neo"	                 없음	                없음

# 따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

# 이용자의 ID가 담긴 문자열 배열 id_list, 
# 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report, 
# 정지 기준이 되는 신고 횟수 k가 매개변수로 주어질 때, 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 반환

# 인터넷을 참고하여 푼 코드
# collections모듈의 defaultdict을 활용하여 
# 신고자의 id와 신고 대상이 받은 신고 횟수를 저장하기 위해 user, report_count를 딕셔너리로 선언

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    reports = list(set(report))
    user = defaultdict(set)
    report_count = defaultdict(int)


    for report in reports:
        reporter, target = report.split() 

        user[reporter].add(target)          # 신고자가 신고한 대상을 저장 : defaultdict(<class 'set'>, {'muzi': {'frodo', 'neo'}, 'frodo': {'neo'}, 'apeach': {'frodo', 'muzi'}})
        report_count[target] += 1           # 신고 당한 대상의 신고 받은 횟수 저장 : defaultdict(<class 'int'>, {'frodo': 2, 'neo': 2, 'muzi': 1}) 

        
    for id in id_list:
        result = 0

        for u in user[id]:
            if report_count[u] >= k:        # 신고 대상의 신고 받은 횟수가 k번이 넘는다면
                result += 1                 # 신고자가 받을 메일 횟수를 증가시킴

        answer.append(result)
    return answer
  
    
    
# 다른 사람 풀이

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
