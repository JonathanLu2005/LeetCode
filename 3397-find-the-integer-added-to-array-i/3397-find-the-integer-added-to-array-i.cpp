class Solution {
public:
    int addedInteger(vector<int>& nums1, vector<int>& nums2) {
        int m2 = *min_element(nums2.begin(), nums2.end());
        int m1 = *min_element(nums1.begin(), nums1.end());
        return m2 - m1;
    }
};