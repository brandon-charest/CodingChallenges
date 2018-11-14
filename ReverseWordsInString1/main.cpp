/* 151. Reverse Words in a String
Given an input string, reverse the string word by word.

Example:  

Input: "the sky is blue",
Output: "blue is sky the".
 */
#include  <iostream>
#include <string>
#include <sstream>
#include <vector>


void reverseWords(std::string &tempString)
{
	std::istringstream iss(tempString);
	std::vector <std::string> words;

	for(std::string word; iss >> word;)
	{
		words.push_back(word);
	}
	
	std::reverse(words.begin(), words.end());

	tempString = "";
	for (auto const &word : words)
	{
		tempString += word;
		if(word != words.back())
		{
			tempString += " ";
		}
	}
}


int main()
{
	
	std::string testString = "the sky is blue";

	reverseWords(testString);

	std::cout << testString << std::endl;
	return 0;
}