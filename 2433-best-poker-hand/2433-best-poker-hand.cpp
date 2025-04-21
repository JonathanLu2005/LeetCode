class Solution {
public:
    string bestHand(vector<int>& ranks, vector<char>& suits) {
        unordered_map<int,int> rankMap;
        unordered_map<char,int> suitMap;

        for (int r : ranks) {
            rankMap[r]++;
        }

        for (char c : suits) {
            suitMap[c]++;
        }

        for (const auto& [key, value] : suitMap) {
            if (value == 5) {
                return "Flush";
            }
        }

        int maxInt = 0;

        for (const auto& [key, value] : rankMap) {
            maxInt = max(maxInt, value);
        }

        if (maxInt >= 3) {
            return "Three of a Kind";
        } else if (maxInt >= 2) {
            return "Pair";
        }

        return "High Card";
    }
};