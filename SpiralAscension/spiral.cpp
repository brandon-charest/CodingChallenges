#include "spiral.h"
#include <iostream>

vvi Spiral::generateMatrix(int num)
{
	return vvi(num, std::vector<int>(num, 0));
}

void Spiral::clockwiseSpiral(vvi)
{

	while (top <= bottom && left <= right && current <= max)
	{
		// left -> right			
		leftToRight();

		// top -> bottom
		topToBottom();

		// right -> left
		rightToLeft();

		// bottom -> top	
		bottomToTop();
	}
}

void Spiral::counterSpiral(vvi)
{
	//
}

void Spiral::spiral(int num, Direction direction)
{
	matrix = generateMatrix(num);

	max = num*num;
	current = 1;
	top = 0;
	bottom = matrix.size() - 1;
	left = 0;
	right = matrix[0].size() - 1;

	switch (direction)
	{
	case Spiral::ClockWise:
		clockwiseSpiral(matrix);
		break;
	case Spiral::CounterClockWise:
		break;
	default:
		break;
	}	
	
	Spiral::print(matrix);

}


void Spiral::leftToRight()
{
	for (int i = left; i <= right; i++)
	{
		matrix[top][i] = current++;
	}
	top++;
}

void Spiral::rightToLeft()
{
	for (int k = right; k >= left; k--)
	{
		matrix[bottom][k] = current++;
	}
	bottom--;
}

void Spiral::topToBottom()
{
	for (int j = top; j <= bottom; j++)
	{
		matrix[j][right] = current++;
	}
	right--;
}

void Spiral::bottomToTop()
{
	for (int l = bottom; l >= top; l--)
	{
		matrix[l][left] = current++;
	}
	left++;
}

void Spiral::print(vvi matrix)
{
	for (auto const &row : matrix)
	{
		for (auto const &col : row)
		{
			std::cout << col << " ";
		}

		std::cout << '\n';
	}
}

