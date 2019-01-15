// 0-1_Knapsack.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <vector>
#include <algorithm>

// Time complexity: 2^n
// Space complexity: O(1)
int knapSack(std::vector<int> itemValue, std::vector<int> itemWeight, int numberItems, int capacity)
{
	if (capacity < 0)
	{
		return INT_MIN;
	}

	if (numberItems < 0 || capacity == 0)
	{
		return 0;
	}

	int includeItem = itemValue[numberItems] + knapSack(itemValue, itemWeight, numberItems - 1, capacity - itemWeight[numberItems]);

	int excludeItem = knapSack(itemValue, itemWeight, numberItems - 1, capacity);


	return std::max(includeItem, excludeItem);
}

int main()
{
	std::vector<int> value = { 20, 5, 10, 40, 15, 25 };
	std::vector<int> weight = { 1, 2, 3, 8, 7, 4 };

	int knapSackCapacity = 10;
	int numberOfItems = value.size() -1;

	std::cout << "Knapsack value is " << knapSack(value, weight, numberOfItems, knapSackCapacity);

    return 0;
}

