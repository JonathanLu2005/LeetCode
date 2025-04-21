class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        // want number 2
        // in words1, we increment
        // if < 2, in words2 we decerment
        // should be 0

        unordered_map<string, int> hashmap;

        for (string word : words1) {
            hashmap[word]++;
        }

        for (string word : words2) {
            if ((hashmap.find(word) != hashmap.end()) && (hashmap[word] < 2)) {
                hashmap[word]--;
            }
        }

        int res = 0;

        for (const auto& [key, value] : hashmap) {
            if (value == 0) {
                res++;
            }
        }

        return res;
    }
};