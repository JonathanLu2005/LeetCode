class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        vector<string> words;
        istringstream stream1(s1);
        string word;

        while (stream1 >> word) {
            words.push_back(word);
        }

        istringstream stream2(s2);

        while (stream2 >> word) {
            words.push_back(word);
        }

        unordered_map<string, int> hashmap;
        vector<string> result;

        for (const auto& w : words) {
            hashmap[w]++;
        }

        for (const auto& [key, value] : hashmap) {
            if (value == 1) {
                result.push_back(key);
            }
        }

        return result;
    }
};