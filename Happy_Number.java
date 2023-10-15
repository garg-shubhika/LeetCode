/*
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
  */

class Solution {
    public boolean isHappy(int n) {
        int temp = 0;
        int digit = 0;
        int s = 0;

        if (n == 1) {
            return true; // 1 is a happy number
        } else if (n > 1 && n < 10 && n!=7) {
            return false; // Numbers between 2 and 9 are not happy numbers
        } else {
            while (s != 1 && s != 4) {
                s = 0;
                while (n != 0) {
                    digit = n % 10;
                    n = n / 10;
                    s = s + (digit * digit);
                }
                n = s;
            }
            if (s == 1) {
                temp = 1;
            }
        }

        return temp == 1;
    }
}
