/* 921. Minimum Add to Make Parentheses Valid
Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4

 */

#include <string>
#include <stack>
#include <iostream>
int minAddToMakeValid(std::string S) {
	std::stack<char> stack;
	int result = 0;

	for(char c : S)
	{
		switch (c)
		{
		case '(':
			stack.push(c);
			break;
		case ')':
			stack.empty() ? result++ : stack.pop();
			break;
		}
	}
	return result + stack.size();
}

int main()
{
	std::string test1 = "())";


	std::cout << minAddToMakeValid(test1);

	return 0;
}