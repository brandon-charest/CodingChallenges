#include "spiral.h"
#include <iostream>
int main()
{
	Spiral s;
	Spiral::Direction direction = Spiral::Direction::ClockWise; //default

	std::cout << "Enter a direction. [1] for clockwise, [-1] for counter clockwise.\n";
	int x;
	std::cin >> x;

	if (x == 1)
	{
		direction = Spiral::Direction::ClockWise;
	}
	else if (x == -1)
	{
		direction = Spiral::Direction::CounterClockWise;
	}

	s.spiral(5, direction);
	

	

	return 0;
}




