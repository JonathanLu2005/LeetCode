class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        // given n we need produce 2 numbers s.t. has no 0 and add together
        // i mean if add together always 1 1 at least
        // cant have 1 0
        // so if given n, the other number can be 1 and n - 1
        // if n - 1 is mod by 10, then increment other 1
        // else return

        for (int i = 1; i < n; i++) {
            int c = n - i;

            string a = to_string(i);
            string b = to_string(c);
            bool good = true;

            for (char c : a) {
                if (c == '0') {
                    good = false;
                }
            }
            for (char c : b) {
                if (c == '0') {
                    good = false;
                }
            }

            if (good) {
                return {i,c};
            }
        }
        return {};
    }
};