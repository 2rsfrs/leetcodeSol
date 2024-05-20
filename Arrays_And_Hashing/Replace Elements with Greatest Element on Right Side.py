class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:

        maxint = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = maxint
            maxint = max(maxint, temp)
        return arr

    # why does this not work?
    # it does, but it will take a long time since you are getting the max number
    # of the entire array each time which takes lots of time.
    def old_soln(self, arr):
        ans = list()
        temp = list()

        i = 0

        if len(arr) != 1:
            while i < len(arr)-1:
                x = max(arr[i+1:])
                y = arr.index(x)
                z = [x] * (y - i)
                temp.append(z)
                i = y

            for i in temp:
                ans.extend(i)
        ans.append(-1)
        # return ans list
        return ans