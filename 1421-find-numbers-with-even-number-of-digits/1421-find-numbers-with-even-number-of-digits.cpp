class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int res = 0;

        for (int num : nums) {
            string n = to_string(num);
            int l = n.size();

            if (l % 2 == 0) {
                res++;
            }
        }

        return res;
    }
};