/* 496. Next Greater Element I
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. 
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.


The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.
Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
*/

#include <vector>
#include <unordered_map>
#include <stack>


typedef std::vector<int> vi;

vi nextGreaterElement(vi &findNums, vi &nums)
{
	vi result;
	std::unordered_map<int, int> map;
	std::stack<int> stack;

	for each (int const &num in nums)
	{
		while (stack.size() && stack.top() < num)
		{
			map[stack.top()] = num;
			stack.pop();
		}
		stack.push(num);
	}

	for each (int const &num in findNums)
	{
		// check if number exists in map, else return -1
		result.push_back(map.count(num) ? map[num] : -1);
	}

	return result;
}


int main()
{

	vi nums1 = { 4,1,2 };
	vi nums2 = { 1,3,4,2 };

	vi res = nextGreaterElement(nums1, nums2);


	return 0;
}