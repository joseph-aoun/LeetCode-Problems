class Solution {
public:
    #define ll long long
    bool good(ll k, ll size, vector<int>&res){
        ll curr = 0;
        for(int i=0; i< res.size(); i++){
            if(res[i] > size) return false;
            if(curr + res[i]>size){
                curr = res[i]; k--;
            }
            else curr += res[i];
        }
        return k>=0;
    }
    int splitArray(vector<int>& res, int k) {
         ll l = 0LL, r = 1e18;
         if (res.size() == 1) return res[0];
        while(l < r - 1){
        ll mid = (l + r)/2;
        if(good(k-1, mid, res)) r = mid;
        else l = mid;
        }
        return r;
    }
};