class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int result = 0;
        int n = pref.size();

        for (string word : words) {
            if (word.size() < n) {
                continue;
            }

            string prefix = "";

            int i = 0;

            while (i < n) {
                prefix += word[i];
                i++;
            }

            if (prefix == pref) {
                result++;
            }
        }

        return result;
    }
};