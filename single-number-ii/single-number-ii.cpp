class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> dp(33, 0);
        for(auto &x : nums){
            for(int i = 0; i < 32; ++i){
                if(x&(1 << i))
                        dp[i]++;
            }
        }
        int ans = 0;
        for(int i = 0; i < 32; i++){
            if(dp[i] %3 != 0)
                    ans |= (1 << i);
        }
        for(auto x : dp) cout << x << " "; cout << '\n';
        return ans;
    }
};