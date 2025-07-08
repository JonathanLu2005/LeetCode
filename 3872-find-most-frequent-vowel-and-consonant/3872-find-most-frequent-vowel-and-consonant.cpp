class Solution {
public:
    int maxFreqSum(string s) {
        set<char> vowel = {'a', 'e', 'i', 'o', 'u'};
        map<char,int> vowels;
        map<char,int> consonants;

        for (char c : s) {
            if (vowel.count(c)) {
                vowels[c]++;
            } else {
                consonants[c]++;
            }
        }

        int v1 = 0;
        int c1 = 0;

        for (const auto& [key, value] : vowels) {
            if (value > v1) {
                v1 = value;
            }
        }
        for (const auto& [key, value] : consonants) {
            if (value > c1) {
                c1 = value;
            }
        }

        return c1 + v1;
    }
};