class Solution {
public:
    double myPow(double x, long long n) {
        if(n == 0) return 1;
        if (n < 0) return 1/myPow(x, -n);
        double y =  myPow(x, n/2);
        if(n%2 == 0) return y*y;
        else return x*y*y;
    }
};