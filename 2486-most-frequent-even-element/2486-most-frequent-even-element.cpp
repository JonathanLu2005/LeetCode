class Solution {
public:
    int mostFrequentEven(vector<int>& nums) {
        unordered_map<int,int> hashmap;

        for (int num : nums) {
            if (num % 2 == 0) {
                hashmap[num]++;
            }
        }

        int max = 0;
        int res = -1;

        for (int num : nums) {
            if (num % 2 == 0) {
                if (hashmap[num] >= max) {
                    if (hashmap[num] == max) {
                        res = min(res, num);
                    } else {
                        res = num;
                        max = hashmap[num];
                    }
                }
            }
        }

        return res;
    }
};