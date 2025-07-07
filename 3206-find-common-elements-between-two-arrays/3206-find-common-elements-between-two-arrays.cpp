class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        int res1 = 0;
        int res2 = 0;

        std::set<int> set1(nums1.begin(), nums1.end());
        std::set<int> set2(nums2.begin(), nums2.end());

        for (int x : nums1) {
            if (set2.count(x)) {
                res1++;
            }
        }

        for (int x : nums2) {
            if (set1.count(x)) {
                res2++;
            }
        }

        return {res1, res2};
    }
};