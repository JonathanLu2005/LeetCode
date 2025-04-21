class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        // volumne = length * width * height

        // bulky iff
        // dimension >= 10^4 or volumne >= 10^9

        // heavy iff
        // mass >= 100
        bool b = false;
        bool h = false;

        long long volumne = (long long)length * width * height;
        
        if (mass >= 100) {
            h = true;
        }

        if ((volumne >= pow(10,9)) || (length >= pow(10,4)) || (width >= pow(10,4)) || (height >= pow(10,4))) {
            b = true;
        }

        if (h && b) {
            return "Both";
        } else if (h) {
            return "Heavy";
        } else if (b) {
            return "Bulky";
        }
        return "Neither";
    }
};