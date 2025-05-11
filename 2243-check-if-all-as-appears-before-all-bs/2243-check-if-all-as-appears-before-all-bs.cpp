class Solution {
public:
    bool checkString(string s) {
        int a = 0;
        int b = 0;

        // evreytime we do a, b must be 0

        for (char c : s) {
            if (c == 'a') {
                a++;

                if (b > 0) {
                    return false;
                }
            } else if (c == 'b') {
                b++;
            }
        }

        return true;
    }
};