########## Problem Number 299 ######
################ Solution 1 ########

s, g = Counter(secret), Counter(guess)
a = sum(i == j for i, j in zip(secret, guess))
return '%sA%sB' % (a, sum((s & g).values()) - a)

########## Solution 2 ##################
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        s=defaultdict(int)
        g=defaultdict(int)
        print(s,g)
        for i,j in zip(secret,guess):
            if i==j:
                bulls +=1
            else:
                s[i] +=1
                g[j] +=1
        cows=0
        for k in s:
            cows += min(s[k],g[k])
        return "{}A{}B".format(bulls,cows)
                
                    
