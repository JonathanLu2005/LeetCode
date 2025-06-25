class Solution {
public:
    string clearDigits(string s) {
        vector<char> array;

        for (char c : s) {
            if (isdigit(c)) {
                array.pop_back();
            } else {
                array.push_back(c);
            }
        }

        string result(array.begin(), array.end());
        return result;
    }
};