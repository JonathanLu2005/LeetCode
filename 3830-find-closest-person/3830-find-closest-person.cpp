class Solution {
public:
    int findClosest(int x, int y, int z) {
        int l = abs(x-z);
        int r = abs(y-z);

        if (l > r) {
            return 2;
        } else if (r > l) {
            return 1;
        }
        return 0;
    }
};