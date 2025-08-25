class Solution {
public:
    string digitSum(string s, int k) {
        // keep going till string is <= k
        // we divide string into sizes of k, and calcualte their total
        // then once we do that, we add it to a string
        // wich is string we keep perofmring on
        string result = "";
        int count = 0;
        int total = 0;

        while (s.length() > k) {
            for (char c : s) {
                total += c - '0';
                count++;

                if (count == k) {
                    result += to_string(total);
                    total = 0;
                    count = 0;
                    total = 0;
                }
            }

            if (count != 0) {
                result += to_string(total);
                total = 0;
                count = 0;
                total = 0;        
            }
            s = result;
            result = "";
        }

        return s;
    }
};