/*739. Daily Temperatures
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].*/

#include <iostream>
#include <vector>
#include <stack>

std::vector<int> dailyTemperatures(std::vector<int>& T) 
{
	std::vector<int> result(T.size(), 0);
	std::stack<std::pair<int, int>> stack;

	for (int i = 0; i < T.size(); i++)
	{
		
		while (!stack.empty() && stack.top().first < T[i])
		{			
			result[stack.top().second] = i - stack.top().second;
			stack.pop();
		}
		stack.push({ T[i],i });
	}

	return result;
}


int main()
{
	std::vector<int> temp = { 73, 74, 75, 71, 69, 72, 76, 73 };

	std::vector<int> result = dailyTemperatures(temp);

	for each (auto x in result)
	{
		std::cout << x;
	}

	return 0;
}