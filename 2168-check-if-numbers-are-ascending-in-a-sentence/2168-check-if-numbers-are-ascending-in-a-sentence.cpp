class Solution {
public:
    bool areNumbersAscending(string s) {
        // stritly inrease

        int n = -1;

        istringstream stream(s);

        string word;

        while (stream >> word) {
            try {
                int num = stoi(word);

                if (num <= n) {
                    return false;
                } 
                n = num;
            } catch (...) {
                continue;
            }
        }

        return true;
    }
};