class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        stack = [(0, target, [])]

        while stack:
            current_index, current_target, current_combination = stack.pop()

            while current_index < len(candidates):
                current_candidate = candidates[current_index]

                if current_candidate == current_target:
                    result.append(current_combination + [current_candidate])
                elif current_candidate < current_target:
                    stack.append((current_index, current_target - current_candidate, current_combination + [current_candidate]))

                current_index += 1

        return result