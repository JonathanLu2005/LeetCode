class Solution {
public:
    int countLargestGroup(int n) {
        map<int,int> myMap;

        for (int i = 1; i <= n; i++) {
            string val = to_string(i);
            int res = 0;

            for (char c : val) {
                res += c - '0';
            }
            myMap[res]++;
        }
        
        int result = 0;
        int max = 0;

        for (const auto& [key, value] : myMap) {
            if (value > max) {
                max = value;
                result = 1;
            } else if (value == max) {
                result++;
            }
        }

        return result;
    }
};