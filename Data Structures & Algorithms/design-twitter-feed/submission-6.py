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
        for uid in id_set:
            tweets = self.feed_map[uid]
            if tweets:
                i = len(tweets) - 1
                timestamp, tweetId = tweets[i]
                heapq.heappush(
                    result_heap, (-timestamp, tweetId, uid, i)
                )
        
        result = []
        while result_heap and len(result) < 10:
            _, tweetId, uid, i = heapq.heappop(result_heap)
            result.append(tweetId)

            # Add the next older tweet from this user.
            i -= 1
            if i >= 0:
                timestamp, nextTweetId = self.feed_map[uid][i]
                heapq.heappush(
                    result_heap, (-timestamp, nextTweetId, uid, i)
                )
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)