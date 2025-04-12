class Solution {
public:
    long long maxScore(vector<int>& a, vector<int>& b) {  
        long long dp0 = -1e18, dp1 = -1e18, dp2 = -1e18, dp3 = -1e18;
        long long a0 = a[0], a1 = a[1], a2 = a[2], a3 = a[3];

        for (int b_element : b) {
            dp3 = max(dp3, dp2 + a3 * 1LL * b_element);
            dp2 = max(dp2, dp1 + a2 * 1LL * b_element);
            dp1 = max(dp1, dp0 + a1 * 1LL * b_element);
            dp0 = max(dp0, a0 * 1LL * b_element); }

        return dp3;  } };