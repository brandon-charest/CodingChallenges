/*442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]*/

#include <iostream>
#include <vector>
#include <unordered_map>

std::vector<int> findDuplicates(std::vector<int>& nums);
void printVec(std::vector<int> vec);

int main()
{

	std::vector<int> test = { 4,3,2,7,8,2,3,1 };

	std::vector<int> result = findDuplicates(test);

	printVec(result);


	return 0;
}


std::vector<int> findDuplicates(std::vector<int>& nums) 
{
	std::vector<int> res;
	std::unordered_map<int, int> map;

	for (int i = 0; i <nums.size(); i++)
	{
		if (map.count(nums[i]))
		{
			res.push_back(nums[i]);
		}
		else
		{
			map[nums[i]] += 1;
		}
	}
	return res;
}

void printVec(std::vector<int> vec)
{	
	for each (auto x in vec)
	{
		std::cout << x ;
	}	
}