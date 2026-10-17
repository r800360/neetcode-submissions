class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.feed_map = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed_map[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # posts by user themself or user's followers
        # returns Tweet IDs from most recent to least recent
        id_set = self.follow_map[userId]
        id_set.add(userId)
        result_heap = []
        for uId in id_set:
            for timestamp, tId in self.feed_map[uId]:
                heapq.heappush(result_heap, (-timestamp, tId))
        
        result = []
        for i in range(min(len(result_heap), 10)):
            result.append(heapq.heappop(result_heap)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)