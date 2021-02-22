class RunningSum {
    public static int[] runningSum(int[] nums) {
        int[] result = new int[nums.length];
        int sum = 0;
        for (int i = 0 ; i < nums.length ; i++) {
            sum += nums[i];
            result[i] = sum;
        }
        return result;
    }
    public static void main(String[] args) {
        int[] example = new int[]{1,2,3,4};
        int[] result = runningSum(example);
        for (int i = 0 ; i < example.length ; i++) {
            System.out.println(result[i]);
        }
    }
}