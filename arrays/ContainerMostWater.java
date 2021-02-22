// https://leetcode.com/problems/container-with-most-water/

import java.lang.Math;
import java.util.Arrays;

class ContainerMostWater {
    public static int maxAreaBruteForce(int[] height) {
        int maxArea = 0;
        int currArea = 0;
        int firstSide, secondSide, smallerSide;
        for (int i = 0 ; i < height.length ; i++) {

            firstSide = height[i];
            for (int j = i+1 ; j < height.length ; j++) {
                secondSide = height[j];
                smallerSide = Math.min(firstSide, secondSide);
                currArea = smallerSide * (j - i);
                if (currArea > maxArea) {
                    maxArea = currArea;
                }
            }
        }
        return maxArea;
    }
    public static int maxAreaOptimal(int[] height) {
        int maxArea = 0;
        int left = 0;
        int right = height.length-1;
        int smallerSide = 0;
        while (left < right) {
            smallerSide = Math.min(height[left], height[right]);
            maxArea = Math.max(maxArea, smallerSide * (right - left));
            if (height[right] > height[left]) {
                left += 1;
            }
            else {
                right -= 1;
            }
        }
        return maxArea;
    }
    public static void main(String args[]) {
        int[] example = new int[]{1,8,6,2,5,4,8,3,7};
        System.out.println(maxAreaOptimal(example));
    }
}