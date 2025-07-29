class Solution {
public:
    string makeGood(string s) {
        // if same letter but capital/non capital meet then cooked
        vector<char> stack;

        for (char c : s) {
            if (stack.size() >= 1) {
                char t = stack.back();

                if (isupper(c)) {
                    if (tolower(c) == t) {
                        stack.pop_back();
                    } else {
                        stack.push_back(c);
                    }
                } else {
                    if (toupper(c) == t) {
                        stack.pop_back();
                    } else {
                        stack.push_back(c);
                    }
                }
            } else {
                stack.push_back(c);
            }
        }

        string res;
        for (char c : stack) {
            res += c;
        }
        return res;
    } 
};