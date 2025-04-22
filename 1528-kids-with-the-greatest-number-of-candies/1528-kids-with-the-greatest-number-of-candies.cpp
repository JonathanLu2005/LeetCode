class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> result;
        int n = sizeof(candies) / sizeof(candies[0]);

        int maxNum = 0;

        for (int c : candies) {
            maxNum = max(maxNum, c);
        }

        for (int c : candies) {
            c += extraCandies;

            result.push_back(c >= maxNum);
        }

        return result;
    }
};