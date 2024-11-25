class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    temp = board[i][j]
                    for m in range(9):
                        if board[m][j] == temp and m!=i :
                            print(1)
                            return False
                    for n in range(9):
                        if board[i][n] == temp and n!=j:
                            print(2)
                            return False
                    x1 = i // 3
                    y1 = j // 3
                    if x1 == 0:
                        list1 = [0,1,2]
                    if x1 == 1:
                        list1 = [3,4,5]
                    if x1 == 2:
                        list1 = [6,7,8]
                    if y1 == 0:
                        list2 = [0,1,2]
                    if y1 == 1:
                        list2 = [3,4,5]
                    if y1 == 2:
                        list2 = [6,7,8]
                    for m in list1:
                        for n in list2:
                            if board[m][n] == board[i][j] and m!=i and n!=j:
                                print(i,'i',j,'j')
                                print(m, "m", n, "n")
                                print(3)
                                return False
        return True

        