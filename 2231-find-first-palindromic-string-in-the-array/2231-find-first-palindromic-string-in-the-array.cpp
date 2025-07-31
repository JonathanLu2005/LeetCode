class Solution {
public:
    bool palindrome(string word) {
        int l = 0;
        int r = word.size() - 1;

        while (l < r) {
            if (word[l] != word[r]) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    string firstPalindrome(vector<string>& words) {
        for (string word : words) {
            if (palindrome(word)) {
                return word;
            }
        }
        return "";
    }
};