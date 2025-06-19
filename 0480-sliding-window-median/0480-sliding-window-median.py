class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # bruh theres a thing called a SortedList wtf
        window = SortedList(nums[:k])
        n = len(nums)
        result = []

        # check if even
        if k % 2 == 0:
            even = True
        else:
            even = False

        # calculate targets
        if even:
            target = int((k/2) - 1)
        else:
            target = int((k/2) - 0.5)

        # add res
        if even:
            median = window[target] + window[target+1]
            result.append(median/2)
        else:
            result.append(window[target])

        # then do for rest of values
        for i in range(k,n):
            old = nums[i-k]
            new = nums[i]

            window.remove(old)
            window.add(new)

            if even:
                median = window[target] + window[target+1]
                result.append(median/2)
            else:
                result.append(window[target])
        return result


        """
        # have window, sort it, return median
        # then remove whatever element must be removed, and when get next element
        # for loop it and add it in its correct place
        # O(nk) ??

        window = sorted(nums[0:k])
        result = []
        even = False
        if k % 2 == 0:
            even = True
        n = len(nums)
        
        if not even: 
            target = int((k/2) - 0.5)
        else:
            target = int((k/2) - 1)

        if even:
            median = window[target] + window[target+1]
            result.append(median/2)
        else:
            result.append(window[target])

        # in loop remove and add new value
        # then calculate median

        for i in range(k,n):
            v = nums[i-k]
            window.remove(v)
            nv = nums[i]
            
            # add it in properly
            add = False
            for j in range(0,k-1):
                if nv < window[j]:
                    window.insert(j,nv)
                    add = True
                    break
            if not add:
                window.append(nv)

            # add to result
            if even:
                median = window[target] + window[target+1]
                result.append(median/2)
            else:
                result.append(window[target])

        return result
        """
            