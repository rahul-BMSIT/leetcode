class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = []
        for i in range(1,numRows+1):
            if i == 1:
                final.append([1])
            elif i == 2:
                final.append([1,1])
            else:
                print(len(final[-1]))
                new_list = []
                for current in range(len(final[-1]) + 1):
                    print(current)
                    if current in (0,len(final[-1])):
                        new_list.append(1)
                    else:
                        new_list.append(final[-1][current-1]+final[-1][current])
                final.append(new_list)
        return final