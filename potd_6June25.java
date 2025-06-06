class Solution {
    public ArrayList<Integer> search(String pat, String txt) {
        ArrayList<Integer> result = new ArrayList<>();
        int d = 256; // number of characters in the input alphabet
        int q = 101; // a prime number (used to mod hash values to avoid overflow)
        int M = pat.length();
        int N = txt.length();

        int p = 0; // hash value for pattern
        int t = 0; // hash value for text
        int h = 1;

        // The value of h would be "pow(d, M-1)%q"
        for (int i = 0; i < M - 1; i++)
            h = (h * d) % q;

        // Calculate hash value for pattern and first window of text
        for (int i = 0; i < M; i++) {
            p = (d * p + pat.charAt(i)) % q;
            t = (d * t + txt.charAt(i)) % q;
        }

        // Slide the pattern over text one by one
        for (int i = 0; i <= N - M; i++) {
            // If the hash values match then only check for characters one by one
            if (p == t) {
                boolean match = true;
                for (int j = 0; j < M; j++) {
                    if (txt.charAt(i + j) != pat.charAt(j)) {
                        match = false;
                        break;
                    }
                }
                if (match)
                    result.add(i + 1); // 1-based index
            }

            // Calculate hash value for next window of text
            if (i < N - M) {
                t = (d * (t - txt.charAt(i) * h) + txt.charAt(i + M)) % q;
                // We might get negative value of t, converting it to positive
                if (t < 0)
                    t = (t + q);
            }
        }

        return result;
    }
}
