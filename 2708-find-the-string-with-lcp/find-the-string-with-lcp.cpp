class Solution {
 public:
  string findTheString(vector<vector<int>>& lcp) {
    const int n = lcp.size();
    constexpr char nonLetter = 'a' - 1;
    char c = nonLetter;
    vector<char> word(n, nonLetter);
    for (int i = 0; i < n; ++i) {
      if (word[i] != nonLetter)  
        continue;
      if (++c > 'z')  
        return "";
      for (int j = i; j < n; ++j)
        if (lcp[i][j] > 0)
          word[j] = c; }
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        const int nextLcp = i + 1 < n && j + 1 < n ? lcp[i + 1][j + 1] : 0;
        const int currLcp = word[i] == word[j] ? 1 + nextLcp : 0;
        if (lcp[i][j] != currLcp)
          return ""; }
    string ans;
    for (const char c : word)
      ans += c;
    return ans;} };
