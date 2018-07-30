/*
53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
*/

#include <iostream>
#include <vector>
#include <algorithm>

#define vi std::vector<int>

// Challenge answer
int MaxSubArray(vi arr)
{
	if (arr.empty())
	{
		return NULL;
	}

	int result = arr.front();
	int maxSoFar = arr.front();

	for (auto const &i : arr)
	{
		maxSoFar = std::max(i, maxSoFar + i);
		result = std::max(result, maxSoFar);
	}

	return result;
}

// template answer for any numeric type
template <typename T>
using vecT = std::vector<T>;

template <class T>
T MaxSubArray(vecT<T> arr)
{
	if (arr.empty())
	{
		return 0;
	}

	T result = arr.front();
	T maxSoFar = arr.front();

	for (auto const &i : arr)
	{
		maxSoFar = std::max(maxSoFar, maxSoFar + i);
		result = std::max(result, maxSoFar);
	}

	return result;
}


int main()
{

	vi test1 = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };

	vi test2 = { -1, 4, -2, 5, -5, 2, -20, 6 };

	std::cout << MaxSubArray(test1) << std::endl;
	std::cout << MaxSubArray(test2) << std::endl;

	// any type with template
	vecT<int> test3 = { 1,2,3 };
	vecT<int> test4 = { -1,-2,-3,-4 };

	vecT<float> fTest1 = { 1.1f, 2.2f, 3.3f };
	vecT<float> fTest2 = { -1.1f, -2.2f, -3.3f, -4.4f };

	std::cout << MaxSubArray<int>(test3) << std::endl;
	std::cout << MaxSubArray<int>(test4) << std::endl;

	std::cout << MaxSubArray<float>(fTest1) << std::endl;
	std::cout << MaxSubArray<float>(fTest2) << std::endl;


	return 0;
}