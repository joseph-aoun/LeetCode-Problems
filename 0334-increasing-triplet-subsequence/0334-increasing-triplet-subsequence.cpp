class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        vector<int>L;
        
        for (auto &x : nums){
            if (L.empty() || L[L.size() - 1] < x){
                L.push_back(x);
            }
            else if(L[0] >= x){
                L[0] = x;
            }
            else{
                L[1] = x;
            }
            if(L.size() > 2) return true;
        }
        return L.size() > 2;
    }
};