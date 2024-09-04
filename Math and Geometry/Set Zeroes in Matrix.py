class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # keep a tracker variable for the first row
        row_zero = 1

        # go through every row and column
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                
                # set the top of the column to be 0
                # set the left most column to be 0
                if matrix[row][col] == 0:
                    
                    matrix[0][col] = 0

                    # special case: 0,0 is 0 so we need the tracker variable to make the entire row 0
                    if row == 0:
                        row_zero = 0
                    else:
                        matrix[row][0] = 0

        # go through the rows and columns and set the current index to 0 if the 
        # top most number is a 0 or the left most number is a 0
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):

                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        
        # if the first column is a 0 then set the first column to be 0
        if matrix[0][0] == 0:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        # if the tracker variable is a 0 then set the first row to be 0
        if row_zero == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

        # return nothing because this is in place
        return