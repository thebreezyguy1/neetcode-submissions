import heapq
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        posts = []
        self.users[userId].add(userId)
        for followeeId in self.users[userId]:
            posts.extend(self.tweets[followeeId])
        
        heapq.heapify(posts)

        while posts and len(newsFeed) < 10:
            post = heapq.heappop(posts)
            newsFeed.append(post[1])
        
        return newsFeed
            

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].discard(followeeId)