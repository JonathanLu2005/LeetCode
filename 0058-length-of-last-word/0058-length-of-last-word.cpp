class Solution {
public:
    int lengthOfLastWord(string s) {
        istringstream iss(s);
        vector<string> result;
        string word;

        while (iss >> word) {
            result.push_back(word);
        }

        return result.back().size();
    }
};