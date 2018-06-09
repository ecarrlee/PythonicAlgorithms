Class Stairs:
    def climbStairs(self, n):
        step_dict = {0:1,1:1}
        if n in step_dict:
            return step_dict[n]
        k = 2
        while True:
            step_dict[k] = step_dict[k-1] + step_dict[k-2]
            if k == n:
                return step_dict[k]
            k = k + 1
        
 
