class Solution {
public:
    int numberOfMatches(int n) {
        // num team = even
        // team get paired with another team, so n/2 matches played, n/2 advance
        // if odd, 1 team randomly advance, then apply same logic as above
        // return num matches till winner decided

        int res = 0;

        while (n > 1) {
            int d = 0;
            if (n % 2 == 1) {
                d = (n - 1) / 2;
            } else {
                d = n / 2;
            }

            res += d;
            n -= d;
        }

        return res;
    }
};