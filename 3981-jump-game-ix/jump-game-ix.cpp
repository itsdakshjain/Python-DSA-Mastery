#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    struct Component {
        int value;
        int left;
        int right;
    };

    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n);
        vector<Component> stack;

        for (int i = 0; i < n; i++) {
            Component curr{nums[i], i, i};

            while (!stack.empty() && stack.back().value > nums[i]) {
                Component top = stack.back();
                stack.pop_back();
                curr = {max(curr.value, top.value), top.left, curr.right};
            }

            stack.push_back(curr);
        }

        for (const Component& component : stack) {
            for (int i = component.left; i <= component.right; i++) {
                ans[i] = component.value;
            }
        }

        return ans;
    }
};