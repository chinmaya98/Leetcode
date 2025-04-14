class Solution {
    public String mergeAlternately(String word1, String word2) {
       int m = word1.length(), n= word2.length();
       StringBuilder result = new StringBuilder();
       if(word1 != null || word2!= null){
       for(int i=0; i<Math.max(m,n); i++){
        if(i<m){
            result.append(word1.charAt(i));
        }
        if(i<n){
            result.append(word2.charAt(i));
        }
       } 
        return result.toString();

       } else {
        if(word1!= null){
            return word1;
        } else {
            return word2;
        }
       }
    }
}