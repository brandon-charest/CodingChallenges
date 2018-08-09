#include "Flood.h"
#include <iostream>

void Flood::print(vvi &image)
{
	if (image.empty())
	{
		return;
	}

	for (auto const &vec : image)
	{
		for (auto const &x : vec)
		{
			std::cout << x << ' ';
		}
		std::cout << std::endl;
	}

}

vvi Flood::floodFill(vvi &image, int const row, int const col, int const newColor)
{
	if (row < 0 || col < 0 || row > image.size() || col > image[0].size())
	{
		return image;
	}
	
	fill(image, row, col, image[row][col], newColor);

	return image;
}

void Flood::fill(vvi &image, int const row, int const col, int const oldColor, int const newColor)
{
	if (row >= 0 && col >= 0 && row < image.size() && col < image[0].size() && image[row][col] == oldColor)
	{
		image[row][col] = newColor;
		fill(image, row + 1, col, oldColor, newColor);
		fill(image, row - 1, col, oldColor, newColor);
		fill(image, row, col + 1, oldColor, newColor);
		fill(image, row, col - 1, oldColor, newColor);
	}
}
