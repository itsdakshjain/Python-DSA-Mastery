class Solution {
public:
    int minMirrorPairDistance(vector<int>& nums) {
        unordered_map<int, int> previous;
        int answer = nums.size() + 1;

        for (int i = 0; i < nums.size(); i++) {
            int value = nums[i];

            if (previous.count(value)) {
                answer = min(answer, i - previous[value]);
            }

            previous[reverse(value)] = i;
        }

        return answer == nums.size() + 1 ? -1 : answer;
    }

private:
    int reverse(int value) {
        int reversed = 0;

        while (value > 0) {
            reversed = reversed * 10 + value % 10;
            value /= 10;
        }

        return reversed;
    }
};