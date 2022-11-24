class Solution {
public:
    int climbStairs(int n) {
        if(n == 1) return 1;
        int x = 0, y = 1;
        for(int i = 0; i <= n-1; i++){
            int temp = y;
            y += x;
            x = temp;
        }
        
        return y;
    }
};