class Solution {
public:
    int getLucky(string s, int k) {
        string result = "";

        for (char c : s) {
            result += to_string(c - 'a' + 1);
        }

        while (k > 0) {
            int calc = 0;

            for (char c : result) {
                calc += c - '0';
            }

            result = to_string(calc);
            k--;
        }

        return stoi(result);
    }
};