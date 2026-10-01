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
        x=list(self.usertotweet[userId])
        for y in self.usertofollowers[userId]:
            x+=self.usertotweet[y]
        x.sort()
        if len(x)>10:
            x=x[0:10]
        return [t for f,t in x]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.usertofollowers[followerId].discard(followeeId)
