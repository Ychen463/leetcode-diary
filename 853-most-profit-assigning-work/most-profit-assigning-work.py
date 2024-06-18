# # ============== Approach 1: Binary Search and Greedy (Sort by Job Difficulty)==========
# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
#         job_profile = [(0, 0)]
#         for i in range(len(difficulty)):
#             job_profile.append((difficulty[i],profit[i]))
#         job_profile.sort()
#         for i in range(len(job_profile)-1):
#             job_profile[i+1] = (job_profile[i+1][0], max(job_profile[i+1][1],job_profile[i][1])) 
#         net_profit = 0 
#         for i in range(len(worker)):
#             ability = worker[i]
#             l, r = 0, len(job_profile) -1
#             job_profit = 0
#             while l <= r:
#                 mid = l + (r-l)//2
#                 if job_profile[mid][0] <= ability:
#                     job_profit = max(job_profit, job_profile[mid][1])
#                     l = mid+1
#                 else:
#                     r = mid -1
#             net_profit += job_profit
#         return net_profit

# # ============== Approach 2: Binary Search and Greedy (Sort by profit) ==========
# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
#         job_profile = [(0, 0)]
#         for i in range(len(difficulty)):
#             job_profile.append((profit[i],difficulty[i]))
#         job_profile.sort(reverse = True)
#         for i in range(len(job_profile) - 1 ):
#             job_profile[i+1] = (job_profile[i+1][0], min(job_profile[i][1],job_profile[i+1][1]))
#         net_profit = 0
#         for ability in worker:
#             l, r = 0, len(job_profile) -1
#             job_profit = 0
#             while l <= r:
#                 mid = l+(r-l)//2
#                 if ability >= job_profile[mid][1]:
#                     job_profit = max(job_profit, job_profile[mid][0])
#                     r = mid -1
#                 else:
#                     l = mid +1
#             net_profit += job_profit
#         return net_profit


# ============== Approach 3: Greedy and Two-Pointers ==========
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profile = [(difficulty[i], profit[i]) for i in range(len(profit))]
        job_profile.sort()
        worker.sort()
        
        net_profit, max_profit, index = 0, 0, 0
        for ability in worker:
            while index < len(job_profile) and ability >= job_profile[index][0]:
                max_profit = max(job_profile[index][1], max_profit)
                index+=1
            net_profit += max_profit
        return net_profit