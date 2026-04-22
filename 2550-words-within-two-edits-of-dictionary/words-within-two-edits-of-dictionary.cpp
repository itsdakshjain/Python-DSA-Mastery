class Solution {
public:
    vector<string> twoEditWords(vector<string>& queries, vector<string>& dictionary) {
        vector<string> answer;

        for (const string& query : queries) {
            for (const string& word : dictionary) {
                int diff = 0;

                for (int i = 0; i < query.size(); i++) {
                    if (query[i] != word[i]) {
                        diff++;
                    }
                }

                if (diff <= 2) {
                    answer.push_back(query);
                    break;
                }
            }
        }

        return answer;
    }
};