class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newtemp = []
        answer =[]
        for i in points:
            distance = i[0]**2 + i[1]**2
            newtemp.append([distance,i ])
        newtemp.sort()
        for j in range(k):
            answer.append(newtemp[j][1])
        return answer
