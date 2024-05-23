class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        counter =0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check if left, right plots are empty:
                empty_left_plot = (i ==0) or (flowerbed[i-1]==0)
                empty_right_plot = (i == len(flowerbed)-1) or (flowerbed[i+1]==0)
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] =1
                    counter +=1
                    if counter >= n:
                        return True
        
        return counter>=n
