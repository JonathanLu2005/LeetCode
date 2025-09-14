class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int r = image.size();
        int c = image[0].size();

        for (int i = 0; i < r; i++) {
            reverse(image[i].begin(), image[i].end());
        } 

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int v = image[i][j];

                if (v == 1) {
                    image[i][j] = 0;
                } else {
                    image[i][j] = 1;
                }
            }
        }

        return image;
    }
};