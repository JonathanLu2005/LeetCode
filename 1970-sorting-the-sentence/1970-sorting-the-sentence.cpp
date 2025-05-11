class Solution {
public:
    string sortSentence(string s) {
        istringstream stream(s);
        string word;
        unordered_map<int, string> map;
        int n = 0;

        while (stream >> word) {
            n++;
            int num = stoi(word.substr(word.find_first_of("0123456789")));
            word.pop_back();
            map[num] = word;
        }

        string res = "";

        for (int i = 1; i <= n; i++) {
            word = map[i];
            res = res + word + " ";
        }

        res.pop_back();
        return res;
    }
};