class Solution {
public:
    int countCompleteDayPairs(vector<int>& hours) {
        int cnt = 0;
        int n = hours.size();
        map<int, int> mp;
        for(int i=0;i<n;i++){
            int hash = (24 - hours[i]%24)%24;
            if(mp.find(hash) != mp.end()) cnt+=mp[hash];
            mp[hours[i]%24]++;
        }
        return cnt;        
    }
};