#include "IslandPerimeter.h"

int IslandPerimeter::findPerimeter(vvi &island)
{
	if (island.empty() || island.size() == 0)
	{
		return 0;
	}

	for (int row = 0; row < island.size(); row++)
	{
		for (int col = 0; col < island[0].size(); col++)
		{
			if (island[row][col] == 1)
			{
				return perimeterHelper(island, row, col, 0);
			}
		}
	}

}

int IslandPerimeter::perimeterHelper(vvi &island, int const row, int const col, int perimeter)
{
	if (row < 0 || col < 0 || row >= island.size() || col >= island[0].size() || island[row][col] != 1)
	{
		return perimeter;
	}
	// mark as visited
	island[row][col] = -1;

	//check up 
	if (row - 1 < 0 || island[row - 1][col] == 0 )
	{
		perimeter++;
	}	

	// check down
	if (row + 1 >= island.size() || island[row + 1][col] == 0)
	{
		perimeter++;
	}

	// check left
	if (col - 1 < 0 || island[row][col - 1] == 0)
	{
		perimeter++;
	}

	// check right
	if (col + 1 >= island[0].size() || island[row][col + 1] == 0)
	{
		perimeter++;
	}
		
	perimeter = perimeterHelper(island, row - 1, col, perimeter);
	perimeter = perimeterHelper(island, row + 1, col, perimeter);
	perimeter = perimeterHelper(island, row, col - 1, perimeter);
	perimeter = perimeterHelper(island, row, col + 1, perimeter);

	return perimeter;
}
