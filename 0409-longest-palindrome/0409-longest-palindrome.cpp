class Solution {
public:
    int longestPalindrome(string s) {
        // get biggest odd number + all evens
        map<char,int> hashmap;

        for (char c : s) {
            hashmap[c]++;
        }

        int res = 0;
        bool odd = false;

        for (const auto& [key, value] : hashmap) {
            if (value % 2 == 0) {
                res += value;
            } else {
                res += value - 1;
                odd = true;
            }
        }
        if (odd) {
            res++;
        }

        return res;
    }
};