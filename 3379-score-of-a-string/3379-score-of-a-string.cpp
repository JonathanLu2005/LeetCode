class Solution {
public:
    int scoreOfString(string s) {
        int ptr1 = 0;
        int ptr2 = 1;
        int result = 0;
        
        while (ptr2 < s.length()) {
            char first = s[ptr1];
            char second = s[ptr2];

            int firstValue = static_cast<int>(first);
            int secondValue = static_cast<int>(second);

            result += abs(firstValue - secondValue);

            ptr1 += 1;
            ptr2 += 1;
        }

        return result;
    }
};