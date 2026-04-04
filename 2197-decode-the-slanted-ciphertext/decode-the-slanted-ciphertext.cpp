class Solution {
public:
    string decodeCiphertext(string encodedText, int rows) {
        string result;
      
        // Calculate number of columns in the matrix
        int columns = encodedText.size() / rows;
      
        // Traverse each diagonal starting from the first row
        // Each diagonal starts at position (0, j) where j is the starting column
        for (int startCol = 0; startCol < columns; ++startCol) {
            // Traverse the diagonal from (0, startCol) going down-right
            // row increases by 1, column increases by 1 for each step
            int row = 0;
            int col = startCol;
          
            while (row < rows && col < columns) {
                // Convert 2D coordinates (row, col) to 1D index in the string
                // Index formula: row * columns + col
                int index = row * columns + col;
                result += encodedText[index];
              
                // Move to next position in the diagonal
                row++;
                col++;
            }
        }
      
        // Remove trailing spaces from the decoded message
        while (!result.empty() && result.back() == ' ') {
            result.pop_back();
        }
      
        return result;
    }
};