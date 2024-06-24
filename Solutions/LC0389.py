class Solution {
public:
    int minKBitFlips(vector<int>& nums, int k) {
        int flag = 0;
        int res = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            int cur = nums[i] ^ flag;
            if (cur == 0) {
                if (i + k > n) return -1;
                flag ^= 1;
                res++;
            }
            nums[i] = 1 - cur;
            if (i + 1 - k >= 0) flag ^= nums[i + 1 - k];
        }
        return res;
    }
};
