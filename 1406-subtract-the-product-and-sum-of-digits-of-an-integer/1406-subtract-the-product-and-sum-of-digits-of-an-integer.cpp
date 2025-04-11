class Solution {
public:
    int subtractProductAndSum(int n) {
        int product = 1;
        int sum = 0;

        string num = to_string(n);

        for (char c : num) {
            int digit = c - '0';

            sum += digit;
            product *= digit;
        }

        return product - sum;
    }
};