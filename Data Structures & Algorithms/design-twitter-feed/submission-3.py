class Twitter:

    def __init__(self):
        self.posts = []
        self.users = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.posts, (-self.time, userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        recentPosts = []
        while self.posts and len(newsFeed) < 10:
            post = heapq.heappop(self.posts)
            
            if post[1] == userId or post[1] in self.users[userId]:
                newsFeed.append(post[2])
            recentPosts.append(post)
        
        for post in recentPosts:
            heapq.heappush(self.posts, post)
        
        return newsFeed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)
