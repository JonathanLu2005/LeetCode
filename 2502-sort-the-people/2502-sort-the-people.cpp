class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        // hashmap height = name
        // sort height then index hashmap

        unordered_map<int, string> map;

        for (int i = 0; i < names.size(); i++) {
            map[heights[i]] = names[i];
        }

        sort(heights.begin(), heights.end());

        vector<string> result;

        for (int i = heights.size() -1; i >= 0; i--) {
            result.push_back(map[heights[i]]);
        }

        return result;
    }
};