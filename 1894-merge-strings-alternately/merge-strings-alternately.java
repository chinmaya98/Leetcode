class Solution {
    public String mergeAlternately(String word1, String word2) {
       if (word1 == null && word2 == null) {
            return "";
        } else if (word1 == null) {
            return word2;
        } else if (word2 == null) {
            return word1;
        }

        int m = word1.length(), n = word2.length();
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < Math.max(m, n); i++) {
            if (i < m) {
                result.append(word1.charAt(i));
            }
            if (i < n) {
                result.append(word2.charAt(i));
            }
        } 
        return result.toString();
    }

}

