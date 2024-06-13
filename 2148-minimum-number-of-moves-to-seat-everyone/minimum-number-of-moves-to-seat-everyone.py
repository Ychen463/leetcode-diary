# # ============ Approach 1: Sorting (Greedy) ============
# class Solution:
#     def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
#         seats.sort()
#         students.sort()
#         count =0 
#         for i in range(len(seats)):
#             ab = abs(seats[i] - students[i])
#             count += ab
#         return count

# ============ Approach 2: Counting Sort ============
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        maxValue = max(max(seats),max(students) )
        differences = [0] * maxValue

        for i in range(len(seats)):
            differences[seats[i] - 1] += 1
        for i in range(len(students)):
            differences[students[i] - 1] -= 1
        moves = 0
        unmatched = 0
        for difference in differences:
            moves += abs(unmatched)
            unmatched += difference
        return moves
        