class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>array = nums1;
        array.insert(array.end(), nums2.begin(), nums2.end());
        sort(array.begin(),array.end());
        
        int n = array.size();
