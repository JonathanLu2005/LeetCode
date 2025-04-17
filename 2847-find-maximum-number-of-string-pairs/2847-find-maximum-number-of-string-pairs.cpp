class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        unordered_map<string,int> map;
        int res = 0;

        for (string word : words) {
            string key = word;
            reverse(key.begin(), key.end());

            if (map.find(key) != map.end()) {
                res++;
            }
            map[word]++;
        }

        return res;
    }
};