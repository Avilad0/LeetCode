from typing import List

import heapq
from collections import deque

# n = total number of followeeIds associated with the userId
# m = maximum number of tweets by any user,
# N = total number of userIds
# M = maximum number of followees for any user.

# tc=O(nlog10) = O(n) - for getNewsFeed - using maxheap - addition to below to keep len(maxheap)<=10 using minHeap for len(following)>10 
# tc=O(1) - for postTweet, follow, unfollow - same as below except restrict len of postList[u] to 10
# total sc=O(N*M + N*m + n)
class Twitter:

    def __init__(self):
        self.following = {} # userId: set(ids)
        self.postList = {}  #userId: [(time, tweetId)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.postList:
            self.postList[userId]= deque([(self.time, tweetId)])
        else:
            if len(self.postList[userId])==10:   #keep only 10 latest tweet of user
                self.postList[userId].popleft()
            self.postList[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
        self.following[userId].add(userId)

        feed = []

        maxHeap = []

        if len(self.following[userId])<=10:  # keep old code of populating maxHeap for following users <= 10, so len(maxHeap)<10
            for u in self.following[userId]:
                if u in self.postList:
                    index = len(self.postList[u])-1
                    heapq.heappush(maxHeap, (-self.postList[u][index][0], index, u))
            
        else: # for following>10, create minHeap with len always less than 10 and use the last remaining to populate maxHeap 
            minHeap = []
            for u in self.following[userId]:
                if u in self.postList:
                    index = len(self.postList[u])-1
                    heapq.heappush(minHeap, (self.postList[u][index][0], index, u))
                    if len(minHeap)>10:
                        heapq.heappop(minHeap)
            
            while minHeap:
                item = heapq.heappop(minHeap)
                heapq.heappush(maxHeap, (-item[0], item[1], item[2]))
            
            
        # extract 10 most recent from maxHeap as before
        for _ in range(10):
            if not maxHeap:
                break
            (_, index, u) = heapq.heappop(maxHeap)
            feed.append(self.postList[u][index][1])
            if index>0:
                heapq.heappush(maxHeap, (-self.postList[u][index-1][0], index-1, u))

        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following or followeeId not in self.following[followerId]:
            return
        
        self.following[followerId].remove(followeeId)




# # tc=O(nlogn + 10*logn) = O(nlogn) - for getNewsFeed - using maxheap -
# # tc=O(1) - for postTweet, follow, unfollow
# # total sc=O(N*M + N*m + n)
# class Twitter:

#     def __init__(self):
#         self.following = {} # userId: set(ids)
#         self.postList = {}  #userId: [(time, tweetId)]
#         self.time = 0

#     def postTweet(self, userId: int, tweetId: int) -> None:
#         self.time+=1
#         if userId not in self.postList:
#             self.postList[userId]= [(self.time, tweetId)]
#         else:    
#             self.postList[userId].append((self.time, tweetId))

#     def getNewsFeed(self, userId: int) -> List[int]:
#         if userId not in self.following:
#             self.following[userId] = set()
#         self.following[userId].add(userId)

#         maxHeap = []
#         for u in self.following[userId]:
#             if u in self.postList:
#                 index = len(self.postList[u])-1
#                 heapq.heappush(maxHeap, (-self.postList[u][index][0], index, u))
        
#         feed = []
#         for _ in range(10):
#             if not maxHeap:
#                 break
#             (_, index, u) = heapq.heappop(maxHeap)
#             feed.append(self.postList[u][index][1])
#             if index>0:
#                 heapq.heappush(maxHeap, (-self.postList[u][index-1][0], index-1, u))
        
#         return feed
        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         if followerId not in self.following:
#             self.following[followerId] = set()
        
#         self.following[followerId].add(followeeId)

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         if followerId not in self.following or followeeId not in self.following[followerId]:
#             return
        
#         self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)