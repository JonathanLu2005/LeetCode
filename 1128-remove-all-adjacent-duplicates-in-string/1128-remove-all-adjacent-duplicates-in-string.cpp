class Solution {
public:
    string removeDuplicates(string s) {
        vector<char> result;

        for (char c : s) {
            if ((result.size() > 0) && (result.back() == c)) {
                while ((result.size() > 0) && (result.back() == c)) {
                    result.pop_back();
                }
            } else {
                result.push_back(c);
            }
        }

        return string(result.begin(), result.end());
    }
};