class Solution {
public:
    string decodeMessage(string key, string message) {
        map<char, char> hashmap;

        char c = 'a';

        for (char t : key) {
            if (t != ' ') {
                if (hashmap.find(t) == hashmap.end()) {
                    hashmap[t] = c;
                    c++;             
                }
            }
        }
        string result = "";

        for (char c : message) {
            if (c != ' ') {
                result += hashmap[c];
            } else {
                result += ' ';
            }
        }

        return result;
    }
};