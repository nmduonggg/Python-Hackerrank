"""There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .

Input Format

The first line contains a single integer , the number of test cases.
For each test case, there are  lines.
The first line of each test case contains , the number of cubes.
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

Output Format

For each test case, output a single line containing either Yes or No.

Sample Input

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]
Sample Output

Yes
No
"""

from collections import deque
cases = int(input())

for case in range(cases):
    N = int(input())
    nums = deque([int(x) for x in input().split()])
    
    for cube in sorted(nums, reverse = True):
        if cube == nums[-1]:
            nums.pop()
        elif cube == nums[0]:
            nums.popleft()
        else:
            print("No")
            break
            
    if len(nums) == 0:
        print('Yes')
    
    
    