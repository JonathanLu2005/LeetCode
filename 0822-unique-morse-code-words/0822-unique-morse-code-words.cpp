class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        unordered_map<char, std::string> morseMap = {
        {'a', ".-"}, {'b', "-..."}, {'c', "-.-."}, {'d', "-.."}, {'e', "."},
        {'f', "..-."}, {'g', "--."}, {'h', "...."}, {'i', ".."}, {'j', ".---"},
        {'k', "-.-"}, {'l', ".-.."}, {'m', "--"}, {'n', "-."}, {'o', "---"},
        {'p', ".--."}, {'q', "--.-"}, {'r', ".-."}, {'s', "..."}, {'t', "-"},
        {'u', "..-"}, {'v', "...-"}, {'w', ".--"}, {'x', "-..-"}, {'y', "-.--"},
        {'z', "--.."}
        };

        unordered_set<string> result;

        for (string word : words) {
            string morse;

            for (char c : word) {
                morse += morseMap[c];
            }
            result.insert(morse);
        }

        return result.size();
    }
};