class Solution {
public:
    vector<int> twoOutOfThree(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3) {
        // make all into sets
        // traverse do hashmap
        // then traverse hashmap and return those keys

        set<int> set1(nums1.begin(), nums1.end());
        set<int> set2(nums2.begin(), nums2.end());
        set<int> set3(nums3.begin(), nums3.end());
        unordered_map<int,int> hashmap;

        for (int x : set1) {
            hashmap[x]++;
        }
        for (int x : set2) {
            hashmap[x]++;
        }
        for (int x : set3) {
            hashmap[x]++;
        }

        vector<int> result;
        for (const auto& pair : hashmap) {
            if (pair.second >= 2) {
                result.push_back(pair.first);
            }
        }

        return result;
    }
};