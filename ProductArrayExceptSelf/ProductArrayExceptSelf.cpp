/* 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).
 */

#include <iostream>
#include <vector>


void print(std::vector<int> vec)
{
	for (auto const &v : vec)
	{		
		std::cout << v << ' ';		
		
	}
	std::cout << std::endl;
}

std::vector<int> productExceptSelf(std::vector<int> &nums)
{
	std::vector<int> result;

	for(int i=0; i<nums.size(); i++)
	{
		
	}

	return result;
}

int main()
{

	std::vector<int> test = { 1,2,3,4 };

	productExceptSelf(test);

	//print(test);

	return 0;
}

