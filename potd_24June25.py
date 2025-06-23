class Solution {
  public:
    string maxSubseq(string& s, int k) {
        int n = s.size();
        int keep = n - k; // number of characters to keep
        string result;
        
        for (int i = 0; i < n; ++i) {
            // while there's still characters in result,
            // and we can still delete some characters (k > 0),
            // and current character is greater than the last one in result
            while (!result.empty() && k > 0 && result.back() < s[i]) {
                result.pop_back();
                k--;
            }
            result.push_back(s[i]);
        }

        // Trim result to required size in case not enough deletions happened
        result.resize(keep);

        return result;
    }
};
