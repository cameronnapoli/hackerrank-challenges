# https://leetcode.com/problems/frog-jump/description/

# Initial solution which failed because frog can jump over stones
#  class Solution:
#     def canCross(self, stones):
#         """
#         :type stones: List[int]
#         :rtype: bool
#         """
#
#         # O(n) solution is just loop through and see if  next value is k, k+1, or k-1 away
#         # NOTE: Doesn't work because you can skip stones
#         for i in range(len(stones)-2):
#             curr_k = stones[i+1] - stones[i]
#             next_k = stones[i+2] - stones[i+1]
#             if abs(curr_k - next_k) > 1:
#                 return False
#         return True

class Solution:
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # Need dynamic solution (backwards dynamic solution)
        if len(stones) < 2:
            return False
        if stones[1] - stones[0] != 1:
            return False

        mem = {}
        return self.canCrossSubProblem(stones, 0, 1, mem)

    def canCrossSubProblem(self, stones, jump_index, jump_size, mem):
        """
        :type stones: List[int]
        :rtype: bool
        """
        result = False
        if (jump_index, jump_size) in mem:
            return mem[(jump_index, jump_size)]

        # last stone reached
        if jump_index == len(stones) - 1:
            result = True

        for i in range(jump_index + 1, len(stones)):

            curr_jump_size = stones[i] - stones[jump_index]

            if abs(curr_jump_size - jump_size) <= 1:
                result = result or self.canCrossSubProblem(stones, i, curr_jump_size, mem)
                mem[(jump_index, jump_size)] = result

            if curr_jump_size - jump_size > 1:
                break

        return result

s = Solution()

stones1 = [0, 1, 3, 5, 6, 8, 12, 17]
r = s.canCross(stones1)
print("%s\n\n" % str(r))

stones2 = [0, 2]
r = s.canCross(stones2)
print("%s\n\n" % str(r))
