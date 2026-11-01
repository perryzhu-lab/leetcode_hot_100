class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,m = len(s),len(p)
        if n<m :
            return []
        p_count=[0]*26
        win_count=[0]*26
        res=[]

        for i in p:
            p_count[ord(i)-ord('a')]+=1

        for i in range(m):
            win_count[ord(s[i])-ord('a')]+=1
        if win_count==p_count:
            res.append(0)

        for i in range(m,n):
            win_count[ord(s[i])-ord('a')]+=1
            win_count[ord(s[i-m])-ord('a')]-=1

            if win_count==p_count:
                res.append(i-m+1)
        return res