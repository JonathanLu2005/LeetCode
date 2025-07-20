class Solution {
public:
    int numberOfSteps(int num) {
        // if even div by 2, else subtract 1
        int steps = 0;

        while (num > 0) {
            if (num % 2 == 0) {
                num = num / 2;
            } else {
                num--;
            }

            steps++;
        }
        return steps;
    }
};