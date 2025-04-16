class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        // count sum of single and sum of double
        // then compare
        int single = 0;
        int doublea = 0;

        for (int x : nums) {
            if (to_string(x).size() == 1) {
                single += x;
            } else {
                doublea += x;
            }
        }

        return !(doublea == single);
    }
};