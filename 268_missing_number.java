import java.util.Arrays;

class missing_number_268 {
    public int missingNumber(int[] nums) {
        int actualSum = Arrays.stream(nums).sum();
        int expectedSum = (nums.length * (nums.length + 1))/2;
        return expectedSum - actualSum;
    }
}