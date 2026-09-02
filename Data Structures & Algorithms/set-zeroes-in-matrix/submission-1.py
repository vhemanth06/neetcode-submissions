from typing import List


class Solution:

  def setZeroes(self, matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])

    # 1. Check if the first row or first column originally have any zeros
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_column_zero = any(matrix[i][0] == 0 for i in range(rows))

    # 2. Use first row and column as markers for the rest of the matrix
    for i in range(1, rows):
      for j in range(1, cols):
        if matrix[i][j] == 0:
          matrix[i][0] = 0
          matrix[0][j] = 0

    # 3. Update inner cells based on the markers
    for i in range(1, rows):
      for j in range(1, cols):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
          matrix[i][j] = 0

    # 4. Finally, zero out the first row if it originally had a zero
    if first_row_zero:
      for j in range(cols):
        matrix[0][j] = 0

    # 5. Zero out the first column if it originally had a zero
    if first_column_zero:
      for i in range(rows):
        matrix[i][0] = 0