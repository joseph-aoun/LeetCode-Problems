class Solution {
public:
    #define max(a, b) ((a) < (b) ? (b) : (a))
    int rob(vector<int>& nums) {
        
        if(nums.size() < 2) return nums[0];
        
        int previous = nums[0];
        int current = max(nums[0], nums[1]);
        
        
        for(int i = 2; i < nums.size(); i++){
            int temp = previous;
            previous = current;
            current = max(temp + nums[i], current);
        }
        
        return current;
    }
};