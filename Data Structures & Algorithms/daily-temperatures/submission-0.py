class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        input-> temperatures = [ 30 , 38 , 30 , 36 , 35, 40 , 28]
        output-> result [ 1 ]
        approach - > track current max 
        """


        #first initialise the res array of zeroes 
        res = [0] * len(temperatures)
        # initialise a stack which will store pair of temp and index
        stack= [] # pair: (temp, index)

        #now lets go through the whole temp array
        for i , t in enumerate(temperatures):
            #first of all we check if stack is not null and the current > old
            while stack and t > stack[-1][0]: #stack[-1] will give (30 , 0) so i need only 30
            # sicne we found a high temp -> we pop from stack
                stacktemp ,stackindex = stack.pop()
                res[stackindex] =( i - stackindex)
            stack.append((t,i))
        return res




        