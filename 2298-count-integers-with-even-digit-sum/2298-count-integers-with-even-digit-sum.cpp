class Solution {
public:
    int countEven(int num) {
        int res = 0;

        for (int n = 1; n <= num; n++) {
            string word = to_string(n);

            int temp = 0;

            for (char c : word) {
                temp += c - '0';
            }

            if (temp % 2 == 0) {
                res++;
            }
        }
        return res;
    }
};