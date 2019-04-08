#include "Flood.h"
#include <iostream>


int main()
{
	Flood flood;

	vvi test = { { 1,1,1,1,1,0,1 },
				 { 0,1,1,1,0,1,1 },
				 { 0,1,1,1,0,0,1 },
				 { 0,1,0,1,0,1,0 } };

	int startRow = 1;
	int startCol = 2;
	int newColor = 3;

	flood.print(test);
	flood.floodFill(test, startRow, startCol, newColor);
	flood.print(test);

	return 0;
}