class Solution {
public:
    int strStr(string haystack, string needle) {
        // go htrough every index, if rest same then cool
        int l = needle.size();
        int n = haystack.size();

        for (int i = 0; i < n; i++) {
            if (haystack.substr(i,l) == needle) {
                return i;
            }
        }

        return -1;
    }
};