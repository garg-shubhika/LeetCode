class Solution {
    public int searchInsert(int[] nums, int target) 
    {
        int k = 0,x=0;
        for(int i=0;i<nums.length;i++)
        {
            //System.out.println(nums[i]);
            if(nums[i]==target)
            k = i;
            else if (nums[i]!=target)
            x = x+1;
        }
    System.out.println(x);
    if(x==nums.length)
    {
        k = 0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i]<target)
            k = i+1;

        }
    }    
    return k;
    }
}
