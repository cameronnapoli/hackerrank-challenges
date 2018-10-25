DEBUG = False

class Solution:
    def search_grid(self, board, word, r, c, searched_cells):
        """
        :type board: List[List[str]]
        :type word: str
        :type int: r
        :type int: c
        :type set: searched_cells (set of point tuples (r, c))
        :rtype: bool
        """
        print("search_grid(... word: %s, r: %s, c: %s, ...)" %
                    (str(word), str(r), str(c)))
        print("\t%s" % str(searched_cells))

        # Change to BFS for bettor memory usage

        found = False
        if board[r][c] != word[0]: # fail case
            print("\t\tFALL THROUGH MISS")
            return False
        if len(word) == 1: # base case
            print("\t\BASE CASE HIT")
            return True

        searched_cells.add((r, c))
        if (r-1) >= 0 and (r-1, c) not in searched_cells:
            print("*** Moving up (r-1)")
            found = self.search_grid(board, word[1:], r-1, c, set(searched_cells))
            if found:
                return True
        if (r+1) < len(board) and (r+1, c) not in searched_cells:
            print("*** Moving down (r+1)")
            found = self.search_grid(board, word[1:], r+1, c, set(searched_cells))
            if found:
                return True
        if (c-1) >= 0 and (r, c-1) not in searched_cells:
            print("*** Moving left (c-1)")
            found = self.search_grid(board, word[1:], r, c-1, set(searched_cells))
            if found:
                return True
        if (c+1) < len(board[r]) and (r, c+1) not in searched_cells:
            print("*** Moving right (c+1)")
            found = self.search_grid(board, word[1:], r, c+1, set(searched_cells))
            if found:
                return True
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        # perform grid path search starting at each cell
        for r in range(len(board)):
            for c in range(len(board[r])):
                found = self.search_grid(board, word, r, c, set())
                if found:
                    return True
                print("\n")
        return False


s = Solution()
board = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
word = "ABCESEEEFS"
print(s.exist(board, word))
