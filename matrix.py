

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    @staticmethod
    def to_matrix(lst):
        m = Matrix(len(lst), 1)
        for i in len(lst):
            m.data[i][0] = lst[i]
        return m

    def to_list(self):
        lst = []
        for i in range(self.rows):
            for j in range(self.cols):
                lst.append(self.data[i][j])
        return lst

    # this one add a number to all element in matrix
    # or add a matrix to a matrix
    # depend on what type of input is
    def add(self, _input):
        if type(_input) is Matrix:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += _input[i][j]
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] += _input

    @staticmethod
    def subtract(a, b):
        result = Matrix(a.rows, b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                result.data[i][j] = a.data[i][j] - b.data[i][j]
        return result

    # multiply 2 same dimension matrix <= this is important
    # or multiply each element of matrix to a number
    # depend on the input type of course
    def multiply(self, _input):

        # same dimension only
        if type(_input) is Matrix:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= _input.data[i][j]

        # a number
        else:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.data[i][j] *= _input

    @staticmethod
    def matrix_multiply(a, b):
        if a.cols != b.rows:
            return None

        result = Matrix(a.rows, b.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                val = 0
                for k in range(a.cols):
                    val += a.data[i][k] * b.data[k][j]
                result.data[i][j] = val

        return result

