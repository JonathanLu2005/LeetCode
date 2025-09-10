class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        // simple really, we can only have odd binary when there's 1 1
        // then everything else is far left
        // so we get length as n
        // 1 2 4 8
        // so then for every 1 we've it'll be 2^3 + 2^2 whatever
        // as n trickles down
        int n = s.size() - 1;
        int ones = 0;

        for (char c : s) {
            if (c == '1') {
                ones++;
            }
        }

        string result = "";
        ones--;

        while (n > 0) {
            if (ones > 0) {
                result += '1';
                ones--;
            } else {
                result += '0';
            }
            n--;
        }
        result += '1';
        return result;

    }
};