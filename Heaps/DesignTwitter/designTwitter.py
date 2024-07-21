from collections import defaultdict

class Twitter:

    def __init__(self):
        #hashset for followers (userId -> set of followerId)
        self.followers = defaultdict(set)
        #hashmap for tweeets (userId -> list of (count, tweetIds))
        self.tweets = defaultdict(list)
        #global count of tweets for max heap to calculate time 
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        #decrememting count for max heap 
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] #ordered starting from recent 
        #min heap to get most recent 
        minHeap = []

        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            if len(self.tweets[followee]) > 0:
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                minHeap.append([count, tweetId, followee, index - 1])
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])
            
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        print(self.followers[followerId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

