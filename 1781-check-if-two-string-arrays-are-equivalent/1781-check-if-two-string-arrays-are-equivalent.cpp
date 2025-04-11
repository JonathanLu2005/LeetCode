class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string array1;
        string array2;

        for (string s1 : word1) {
            array1 += s1;
        }

        for (string s2 : word2) {
            array2 += s2;
        }

        return (array1 == array2);
    }
};