class Solution {
public:
    string interpret(string command) {
        // if read G, concat G
        // if read ( and next is ), concat o, else al
        int n = command.size();
        string res = "";
        int i = 0;

        while (i<n) {
            char letter = command[i];

            if (letter == 'G') {
                res += 'G';
                i++;
            } else {
                // must be open bracket
                i++;

                letter = command[i];

                if (letter == ')') {
                    res += 'o';
                    i++;
                } else {
                    i += 3;
                    res += "al";
                }
            }
        }

        return res;
    }
};