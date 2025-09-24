class Solution {
public:
    bool halvesAreAlike(string s) {
        // split in half then check if have equal amount of vowels
        set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int length = s.size() / 2;
        int a = 0;
        int b = 0;

        for (int i = 0; i < length; i++) {
            if (vowels.find(s[i]) != vowels.end()) {
                a++;
            }
        }

        for (int i = length; i < s.size(); i++) {
            if (vowels.find(s[i]) != vowels.end()) {
                b++;
            }
        }

        return (a == b);
    }
};