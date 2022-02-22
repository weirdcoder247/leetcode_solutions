class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle


    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        # # Approach 1
        # # Import Dependencies
        # import numpy as np

        # # Create numpy array
        # arr = np.array(self.rectangle)
        # arr[row1: row2 + 1, col1: col2 + 1] = newValue
        # self.rectangle = arr.tolist()

        # Approach 2
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                self.rectangle[i][j] = newValue


    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.rectangle[row][col]



# Your SubrectangleQueries object will be instantiated and called as such:
if __name__ == '__main__':
    # Test Case
    row1 = 0
    col1 = 0
    row2 = 1
    col2 = 1
    newValue = -1
    row = 0
    col = 0

    # Define rectangle variable used for initialization of user-defined object
    rectangle = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

    # Create an object of the new class & call the respective methods with the
    # test case values
    obj = SubrectangleQueries(rectangle)
    obj.updateSubrectangle(row1,col1,row2,col2,newValue)
    param_2 = obj.getValue(row,col)
