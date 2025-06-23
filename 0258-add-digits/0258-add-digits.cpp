class Solution {
public:
    int addDigits(int num) {
        string result = to_string(num);

        while (result.size() > 1) {
            int temp = 0;

            for (char c : result) {
                temp += c - '0';
            }

            result = to_string(temp);
        }

        return stoi(result);
    }
};