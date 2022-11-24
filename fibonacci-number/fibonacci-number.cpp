class Solution {
public:
    int fib(int n) {
        int x =0, y = 1;
        if(n == 0) return 0;
        for(int i = 0; i <= n - 2; i++){
            int temp = y;
            y += x;
            x = temp;
        }
        return y;
    }
};