class Solution:
    def ladderLength(self, startword: str, endword: str, wordlist: List[str]) -> int:
        adj=defaultdict(list)
        n=len(wordlist)
        def count(s1,s2):
            m,n=len(s1),len(s2)
            if m!=n:
                return 0
            else:
                res=1
                for i in range(m):
                    if s1[i]!=s2[i]:
                        res-=1
                    if res<0:
                        return 0
                return 1
        for i in range(n):
            for j in range(i+1,n):
                if count(wordlist[i],wordlist[j])==1:
                    adj[wordlist[i]].append(wordlist[j])
                    adj[wordlist[j]].append(wordlist[i])
        if endword not in adj:
            return 0
        if startword not in adj:
            for i in range(n):
                if count(startword,wordlist[i])==1:
                    adj[startword].append(wordlist[i])
                    adj[wordlist[i]].append(startword)
        # print(adj)
        q=deque()
        q.append(startword)
        res=1
        visited=set()
        visited.add(startword)
        while q:
            l=len(q)
            # print(q)
            for _ in range(l):
                word=q.popleft()
                for nei in adj[word]:
                    if nei ==endword:
                        return res+1
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            res+=1
        return 0
