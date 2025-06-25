class Solution {
public:
    vector<string> splitWordsBySeparator(vector<string>& words, char separator) {
        vector<string> result;
        string current = "";

        for (string word : words) {
            for (char c : word) {
                if (c == separator && current != "") {
                    result.push_back(current);
                    current = "";
                } else if (c != separator) {
                    current += c;
                }
            }

            if (current != "") {
                result.push_back(current);
                current = "";
            }
        }

        return result;
    }
};