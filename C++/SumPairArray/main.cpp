/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
*/

#include <unordered_map>
#include <iostream>
#include <iterator> //ostream_iterator

#define vi std::vector<int>
#define mii std::unordered_map<int,int>

vi SumPairArray(vi arr, int sum)
{
	if (arr.empty())
	{
		return {};
	}

	mii map;
	int size = arr.size();	

	for (int i = 0; i < arr.size(); i++)	
	{
		int numberNeeded = sum - arr[i];

		if (map.find(numberNeeded) != map.end())
		{			
			return{map[numberNeeded], i};
		}
		else
		{
			map[arr[i]] = i;
		}
	}
	
	std::cout << "Sum was not found in array" << std::endl;
	return {};
}

template <typename T>
std::ostream &operator << (std::ostream &out, const std::vector<T> &v)
{
	if (!v.empty())
	{
		out << '[';
		std::copy(v.begin(), v.end(), std::ostream_iterator<T>(out, ", "));
		out << "\b\b]";
	}

	return out;
}

int main()
{
	vi test1 = { 2, 7, 11, 15 };
	int sum1 = 9;

	vi test2 = { 1, 4, 45, 6, 10, 8 };
	int sum2 = 16;

	vi test3 = { 4, -2, 1, 8 };
	int sum3 = 7;

	std::cout << SumPairArray(test1, sum1) << std::endl;
	std::cout << SumPairArray(test2, sum2) << std::endl;
	std::cout << SumPairArray(test3, sum3) << std::endl;

	return 0;
}

