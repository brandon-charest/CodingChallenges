/*
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
*/

#include <iostream>
#include <vector>

typedef std::vector<int> vi;

vi sortColors(vi vec);
void printVector(vi vec);

int main()
{
	vi vec = { 0,1,2,2,1,0,0,2,0,1,1,0 };

	std::cout << "Vector before sort: ";
	printVector(vec);

	vec = sortColors(vec);

	std::cout << "Vector after sort:  ";
	printVector(vec);
	return 0;
}


vi sortColors(vi vec)
{
	if (vec.empty())
	{
		return{};
	}

	int index = 0;
	int low = 0;
	int high = vec.size()-1;


	while (index <= high)
	{
		if (vec[index] < 1)
		{
			std::swap(vec[index++], vec[low++]);
		}
		else if (vec[index] > 1)
		{
			std::swap(vec[index], vec[high--]);
		}
		else
		{
			index++;
		}
	}
	return vec;
}

void printVector(vi vec)
{
	for (auto const &i : vec)
	{
		std::cout << i;
	}
	std::cout << std::endl;
}