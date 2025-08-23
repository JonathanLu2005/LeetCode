class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        // n by n cargo deck
        // cell hold 1 container wight weight w
        // however cant exceed maxweight
        // return max containers
        int container = n * n;
        int res = maxWeight / w;

        return min(res,container);
    }
};