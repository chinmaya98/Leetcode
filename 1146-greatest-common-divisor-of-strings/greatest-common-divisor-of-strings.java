class Solution {
    public boolean valid(String str1, String str2, int k) {
        int i = str1.length();
        int j = str1.length();
        if( i % k > 0 || j % k > 0){
            return false;
        } else {
            String base = str1.substring(0,k);
            return str1.replace(base,"").isEmpty() && str2.replace(base,"").isEmpty();
        }
      
    }

    public String gcdOfStrings(String str1, String str2){
        int i = str1.length();
        int j = str2.length();
        for(int m = Math.min(1,j); i>=1; --i){
            if(valid(str1,str2,i)){
                return str1.substring(0,i);
            }
        }
        return "";
    }
}