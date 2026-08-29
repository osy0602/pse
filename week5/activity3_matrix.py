import numpy as np
class MatrixUsingFor:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def calculating(self):
        answer = [[0] * len(self.m2[0]) for _ in range(len(self.m1))]

        for i in range(len(self.m1)):
            for j in range(len(self.m2[0])):
                for k in range(len(self.m1[0])):
                    answer[i][j] += self.m1[i][k] * self.m2[k][j]

        return answer

class MatrixUsingNumpy:
    def __init__(self,m1,m2):
        self.m1 = np.array(m1)
        self.m2 = np.array(m2)

    def calculating(self):
        return self.m1 @ self.m2

def main():
    m1 = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]]

    m2 = [
        [1,2],
        [3,4],
        [5,6],
        [7,8],
        [9,10]]

    matrix_for = MatrixUsingFor(m1, m2)
    print(matrix_for.calculating())

    matrix_np = MatrixUsingNumpy(m1, m2)
    print(matrix_np.calculating())


if __name__ == "__main__":
    main()
