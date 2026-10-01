class Twitter:

    def __init__(self):
        self.usertofollowers=defaultdict(set)
        self.usertotweet=defaultdict(list)
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.usertotweet[userId].append((self.time,tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.usertofollowers[userId])
        res=[]
        minheap=[]
        self.usertofollowers[userId].add(userId)
        for user in self.usertofollowers[userId]:
            index=len(self.usertotweet[user])-1
            if index>=0:
                count,tweetid=self.usertotweet[user][index]
                heapq.heappush(minheap,[count,tweetid,user,index-1])
        while minheap and len(res)<10:
            count,tweetid,user,index=heapq.heappop(minheap)
            res.append(tweetid)
            if index>=0:
                count,tweetid=self.usertotweet[user][index]
                heapq.heappush(minheap,[count,tweetid,user,index-1])
        self.usertofollowers[userId].remove(userId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowers[followerId].discard(followeeId)
