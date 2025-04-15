class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
       List<Boolean> result = new ArrayList<>();

        // Input validation
        if (candies == null || extraCandies == 0) {
            return result;
        }

        // Find the current maximum number of candies any kid has
        int maxCandies = 0;
        for (int candy : candies) {
            if (candy < 0) {
                return new ArrayList<>();
            }
            maxCandies = Math.max(maxCandies, candy);
        }

        for (int candy : candies) {
            result.add(candy + extraCandies >= maxCandies);
        }

        return result;
    }
}