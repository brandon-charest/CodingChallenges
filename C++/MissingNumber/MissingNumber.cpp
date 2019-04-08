/*
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
*/

#include <vector>
#include <iostream>

int missingNumber(std::vector<int> &nums)
{
	if (nums.empty() || nums.size() < 2)
	{
		return 0;
	}

	
	int size = nums.size();
	int total = size * (size + 1) / 2;

	for (auto const &i : nums)
	{
		total -= i;
	}

	return total;
}


int main()
{
	std::vector<int> test1 = { 3, 0, 1 };
	std::vector<int> test2 = { 0, 2, 1, 3, 6, 4 };

	std::cout << missingNumber(test1) << std::endl;
	std::cout << missingNumber(test2) << std::endl;


    return 0;
}

