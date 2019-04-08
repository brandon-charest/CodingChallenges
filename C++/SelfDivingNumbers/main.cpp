/*
728. Self Dividing Numbers

A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
Also, a self-dividing number is not allowed to contain the digit zero.
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
*/

#include <vector>
#include <iostream>
bool helperMethod(int &num)
{
	for (int i = num; i > 0; i /= 10)
	{		
		if (!(i % 10) || num % (i % 10))
		{
			return false;
		}
	}
	return true;
}

std::vector<int> selfDividingNumbers(int left, int right)
{
	std::vector<int> result;

	while (left <= right)
	{	
		if (helperMethod(left))
		{
			result.push_back(left);
		}
		left++;
	}


	return result;
}
template <class T>
void printVector(std::vector<T> vec)
{
	for (auto const &i : vec)
	{
		std::cout << i << " ";
	}
	std::cout << std::endl;
}

int main()
{
	
	printVector(selfDividingNumbers(10, 20));

	return 0;
}