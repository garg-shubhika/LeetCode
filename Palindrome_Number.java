/*Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
*/

class Solution {
    public boolean isPalindrome(int x) 
    {
        if (x < 0) 
        {
            return false; // Negative numbers can't be palindromes
        }
        
        int y = 0;
        int z = x;
        
        while (x > 0) 
        {
            int digit = x % 10;
            y = y * 10 + digit;
            x /= 10;
        }

        return z == y;
    }
}
