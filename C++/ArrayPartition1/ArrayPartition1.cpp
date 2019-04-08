/* 561. Array Partition I

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
*/
#include <array>
#include <vector>
#include <iostream>

typedef std::vector<int> vi;

int arrayPairSum(vi &nums) 
{
	int res = 0;
	std::sort(nums.begin(), nums.end());

	for (int i = 0; i < nums.size(); i += 2)
	{
		res += nums[i];
	}

	return res;
}

int main()
{
	vi test = { 1,4,3,2 };

	std::cout << arrayPairSum(test);


	return 0;
}

