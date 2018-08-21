#pragma once
#include <vector>

typedef std::vector<std::vector<int>> vvi;

class IslandPerimeter
{
public:
	int findPerimeter(vvi &island);

private:
	int perimeterHelper(vvi &island, int const row, int const col, int perimeter);
};

