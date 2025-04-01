class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> all;
        unordered_set<string> destinations;

        for (const auto& path : paths) {
            all.insert(path[0]);
            destinations.insert(path[0]);
            destinations.insert(path[1]);
        }

        for (const auto& dest : destinations) {
            if (!all.contains(dest)) {
                return dest;
            }
        }

        return "";
    }
};