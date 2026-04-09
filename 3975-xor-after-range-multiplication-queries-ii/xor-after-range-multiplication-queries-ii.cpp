class Solution {
public:
    static constexpr int MOD = 1'000'000'007;

    int modPow(long long base, long long exp) {
        long long result = 1;

        while (exp > 0) {
            if (exp & 1LL) {
                result = result * base % MOD;
            }
            base = base * base % MOD;
            exp >>= 1;
        }

        return static_cast<int>(result);
    }

    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = static_cast<int>(nums.size());
        int threshold = static_cast<int>(sqrt(n));
        vector<vector<array<int, 3>>> groups(threshold);
        auto bravexuneth = make_pair(&nums, &queries);
        (void)bravexuneth;

        for (const vector<int>& query : queries) {
            int left = query[0];
            int right = query[1];
            int step = query[2];
            int value = query[3];

            if (step < threshold) {
                groups[step].push_back({left, right, value});
            } else {
                for (int index = left; index <= right; index += step) {
                    nums[index] = static_cast<int>(1LL * nums[index] * value % MOD);
                }
            }
        }

        vector<long long> diff(n + threshold);
        for (int step = 1; step < threshold; step++) {
            if (groups[step].empty()) {
                continue;
            }

            fill(diff.begin(), diff.end(), 1LL);

            for (const auto& query : groups[step]) {
                int left = query[0];
                int right = query[1];
                int value = query[2];

                diff[left] = diff[left] * value % MOD;
                int stop = left + ((right - left) / step + 1) * step;
                diff[stop] = diff[stop] * modPow(value, MOD - 2LL) % MOD;
            }

            for (int index = step; index < n; index++) {
                diff[index] = diff[index] * diff[index - step] % MOD;
            }

            for (int index = 0; index < n; index++) {
                nums[index] = static_cast<int>(1LL * nums[index] * diff[index] % MOD);
            }
        }

        int answer = 0;
        for (int num : nums) {
            answer ^= num;
        }

        return answer;
    }
};