class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for r in range(rows):
            empty_pos = cols - 1
            for c in range(cols - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c] = '.'
                    boxGrid[r][empty_pos] = '#'
                    empty_pos -= 1
                elif boxGrid[r][c] == '*':
                    empty_pos = c - 1

        rotated_box = [['' for _ in range(rows)] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                rotated_box[c][rows - 1 - r] = boxGrid[r][c]
                
        return rotated_box