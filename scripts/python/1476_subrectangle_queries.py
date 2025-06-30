import ast

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

def main():
    rectangle = ast.literal_eval(input("Enter the rectangle as a 2D list (e.g. [[1,2,3],[4,5,6]]): "))
    row1 = int(input("Enter row1: "))
    col1 = int(input("Enter col1: "))
    row2 = int(input("Enter row2: "))
    col2 = int(input("Enter col2: "))
    newValue = int(input("Enter newValue: "))
    row = int(input("Enter row for getValue: "))
    col = int(input("Enter col for getValue: "))
    obj = SubrectangleQueries(rectangle)
    obj.updateSubrectangle(row1, col1, row2, col2, newValue)
    print("Updated rectangle:", obj.rectangle)
    print("Value at (row, col):", obj.getValue(row, col))

# Your SubrectangleQueries object will be instantiated and called as such:
if __name__ == '__main__':
    main()
