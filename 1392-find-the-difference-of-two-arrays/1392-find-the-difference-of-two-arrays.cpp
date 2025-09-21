class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        set<int> set1(nums1.begin(), nums1.end());
        set<int> set2(nums2.begin(), nums2.end());

        nums1.assign(set1.begin(), set1.end());
        nums2.assign(set2.begin(), set2.end());
        
        vector<int> intersection;
        set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), back_inserter(intersection));

        for (int x : intersection) {
            nums1.erase(remove(nums1.begin(), nums1.end(), x), nums1.end());
            nums2.erase(remove(nums2.begin(), nums2.end(), x), nums2.end());
        }

        vector<vector<int>> result;
        result.push_back(nums1);
        result.push_back(nums2);
        return result;
    }
};