class Solution {
public:
    string capitalizeTitle(string title) {
        transform(title.begin(), title.end(), title.begin(), ::tolower);
        int n = title.size();
        string res = "";
        string current = "";

        for (int i = 0; i < n; i++) {
            char c = title[i];

            if (c == ' ') {
                int l = current.size();

                if (l > 2) {
                    current[0] = toupper(current[0]);
                }

                res += current;
                res += c;                
                current = "";
            } else {
                current += c;
            }
        }

        int l = current.size();
        if (l > 2) {
            current[0] = toupper(current[0]);
        }

        res += current;
        return res;

    }
};