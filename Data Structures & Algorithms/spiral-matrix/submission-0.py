from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        # 1. Initialize Pointers
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        result = []

        # 2. Loop until boundaries cross
        while top <= bottom and left <= right:

            # 1. Traverse Left to Right (Top row)
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            
            # Check if boundaries crossed after 'top' update
            if top > bottom: break

            # 2. Traverse Top to Bottom (Right column)
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # Check if boundaries crossed after 'right' update
            if left > right: break

            # 3. Traverse Right to Left (Bottom row)
            # This loop runs only if there is still a row to traverse
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

            # Check if boundaries crossed after 'bottom' update
            if top > bottom: break

            # 4. Traverse Bottom to Top (Left column)
            # This loop runs only if there is still a column to traverse
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
            
        return result