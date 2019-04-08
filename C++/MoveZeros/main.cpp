/* 283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]*/
#include <iostream>
#include <vector>

void printVec(std::vector<int> vec)
{
	
	for each (auto x in vec)
	{
		std::cout << x << " ";
	}
}

void moveZeros(std::vector<int> nums)
{
	int counter = 0;
	for (int i = 0; i < nums.size(); i++)
	{
		if (nums[i] != 0)
		{	
			std::swap(nums[counter++], nums[i]);
		}
	}

	printVec(nums);
}



int main()
{
	std::vector<int> numbers = { 0,1,0,3,12 };

	moveZeros(numbers);

	return 0;
}