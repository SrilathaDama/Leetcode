class Solution:
    def minimumLength(self, s: str) -> int:
        count=len(s)
        cnt=Counter(s)
        for key,value in cnt.items():
            
            if(value==3):
                count-=2
            if(value>3):
                if(value%2==0):
                    count-=(value-2)
                else:
                    count-=(value-1)    
            if(value<3):
                pass    
        return count        