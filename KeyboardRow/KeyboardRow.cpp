/* 500. Keyboard Row
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
*/

#include <vector>
#include <string>
#include <unordered_set>
#include <iostream>

typedef std::vector<std::string> vs;

char toLower(char letter)
{	
	if (letter >= 'A' && letter <= 'Z')
	{
		letter += 32;
	}
	return letter;
}


vs findWords(vs words)
{
	vs result;
	std::unordered_set<char> row1 = { 'q','w','e','r','t','y','u','i','o','p' };
	std::unordered_set<char> row2 = { 'a','s','d','f','g','h','j','k','l' };
	std::unordered_set<char> row3 = { 'z','x','c','v','b','n','m' };


	for (auto const &word : words)
	{
		bool containedInRow1 = true;
		bool containedInRow2 = true;
		bool containedInRow3 = true;
		std::unordered_set<char>::iterator it;

		for (auto const &letter : word)
		{
			char temp = toLower(letter);

			if (containedInRow1)
			{
				it = row1.find(temp);
				if (it == row1.end())
				{
					containedInRow1 = false;
				}
				
			}

			if (containedInRow2)
			{
				it = row2.find(temp);
				if (it == row2.end())
				{
					containedInRow2 = false;
				}
			}

			if (containedInRow3)
			{
				it = row3.find(temp);
				if (it == row3.end())
				{
					containedInRow3 = false;
				}
			}
		}

		if (containedInRow1 || containedInRow2 || containedInRow3)
		{
			result.push_back(word);
		}

	}
	return result;
}

int main()
{

	vs test = { "Hello", "Alaska", "Dad", "Peace" };

	vs res = findWords(test);

	for (auto const &word : res)
	{
		std::cout << word << "\n";
	}

	return 0;
}