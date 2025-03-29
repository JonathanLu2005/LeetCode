class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        unordered_map<int, int> hashmap;

        vector<int> sortedArray = arr;
        sort(sortedArray.begin(), sortedArray.end());
        
        int rank = 1;

        for (int num : sortedArray) {
            if (hashmap.find(num) == hashmap.end()) {
                hashmap[num] = rank;
                rank++;
            }
        }

        for (int i = 0; i < arr.size(); i++) {
            arr[i] = hashmap[arr[i]];
        }

        return arr;
    }
};