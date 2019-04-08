/*
709. To Lower Case
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
*/

#include <string>
#include <iostream>

std::string toLowerCase(std::string str)
{
	if (str.empty())
	{
		return str;
	}

	for(char &c : str)
	{
		if (c >= 'A' && c <= 'Z')
		{
			c += 32;
		}
	}
	return str;
}


int main()
{
	std::cout << toLowerCase("Hello") << std::endl;
	std::cout << toLowerCase("TEST") << std::endl;
	std::cout << toLowerCase("dog") << std::endl;
	std::cout << toLowerCase("TEST1") << std::endl;

	return 0;
}