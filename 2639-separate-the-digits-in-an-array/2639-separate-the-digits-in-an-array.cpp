class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> result;

        for (int num : nums) {
            string word = to_string(num);

            for (char c : word) {
                result.push_back(c - '0');
            }
        }

        return result;
    }
};