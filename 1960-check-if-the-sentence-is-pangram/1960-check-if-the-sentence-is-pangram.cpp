class Solution {
public:
    bool checkIfPangram(string sentence) {
        set<char> myset;

        for (char c : sentence) {
            myset.insert(c);
        }

        return (myset.size() == 26);
    } 
};