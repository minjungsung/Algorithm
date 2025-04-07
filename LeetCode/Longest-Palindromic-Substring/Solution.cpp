class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) {
            return "";
        }

        int start = 0;
        int end = 0;

