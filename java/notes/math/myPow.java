/*
Basically, the idea is to instead of multiplying by
the initial number each time, we square the number
each time. That's it. This way we can move much faster.
*/
public class Solution {
    public double pow(double x, int n) {
        if(n == 0)
            return 1;
        if(n < 0){
            n = -n;
            x = 1/x;
        }
        return (n%2 == 0) ? pow(x*x, n/2) : x*pow(x*x, n/2);
    }
}