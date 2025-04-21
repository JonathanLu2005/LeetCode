class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, bool> hashmap;

        for (string word : arr) {
            if (hashmap.find(word) != hashmap.end()) {
                hashmap[word] = false;
            } else {
                hashmap[word] = true;
            }
        }

        int count = 0;

        for (string word : arr) {
            if (hashmap[word]) {
                count++;

                if (count == k) {
                    return word;
                }
            }
        }

        return "";
    }
};