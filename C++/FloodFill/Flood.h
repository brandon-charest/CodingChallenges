#pragma once
#include <vector>

typedef std::vector<std::vector<int>> vvi;

class Flood
{
public:
	void print(vvi &image);
	vvi floodFill(vvi &image, int const startRow, int const startCol, int const newColor);

private:
	void fill(vvi &image, int const startRow, int const startCol, int const oldColor, int const newColor);
};

