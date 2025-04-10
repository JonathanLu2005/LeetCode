class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> frequency;

        for (int x : arr) {
            frequency[x]++;
        }

        unordered_map<int, int> counter;

        for (const auto& pair: frequency) {
            counter[pair.second]++;

            if (counter[pair.second] > 1) {
                return false;
            }
        }

        return true;
    }
};