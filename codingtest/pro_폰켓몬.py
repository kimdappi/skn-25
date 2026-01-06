"""
최대한 다양한 종류의 폰켓몬 포함하여 n/2마리
폰켓몬 종류 번호 담긴 배열
output => 폰켓몬 종류 번호의 수
"""
def solution(nums):
    poket_counts={}
    for poket in nums:
        if poket in poket_counts:
            poket_counts[poket]+=1
        else:
            poket_counts[poket]=1   
    answer = poket_counts
    
    if len(poket_counts)>len(nums)//2:
        return len(nums)//2
    else:
        return len(poket_counts)
        
