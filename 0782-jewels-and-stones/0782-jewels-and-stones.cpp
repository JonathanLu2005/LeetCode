class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        int result = 0;
        unordered_set<char> jewelSet(jewels.begin(), jewels.end());

        for (char stone : stones) {
            if (jewelSet.count(stone)) {
                result += 1;
            }
        }

        return result;
    }
};