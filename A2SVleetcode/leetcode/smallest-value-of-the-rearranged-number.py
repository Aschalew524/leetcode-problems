class Solution:
    def smallestNumber(self, num: int) -> int:
        ans = 0
        if num < 0:
            list_s  =  list(str(num)[1:])
            list_s .sort(reverse=True)
           
            ans = -1 * int(''.join(list_s ))

        else:
            list_s  = list(str(num))
            list_s .sort()
            count = 0
            start = ''

            for i in range(len(list_s )):

                if list_s [i] != '0':
                    start = list_s [i]
                    break
                count += 1
            ans = int(''.join([start] + ['0']*count + list_s [count+1:]))

        return ans