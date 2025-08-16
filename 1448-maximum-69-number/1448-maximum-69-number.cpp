class Solution {
public:
    int maximum69Number (int num) {
        string result = "";
        bool added = false;
        string number = to_string(num);

        for (char c : number) {
            if (!added && c == '6') {
                result += '9';
                added = true;
            } else {
                result += c;
            }
        }

        return stoi(result);

    }
};