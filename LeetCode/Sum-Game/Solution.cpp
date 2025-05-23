class Solution {
public:
    bool sumGame(string s) {
        double res = 0, n = s.length();
        for (int i = 0; i < n; ++i)
            res += (i < n / 2 ? 1 : -1) * (s[i] == '?' ? 4.5 : s[i] - '0');
        return res != 0.0;
    }
};