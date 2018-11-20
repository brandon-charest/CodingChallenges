/*867. Transpose Matrix
 
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]

Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:

Input: [[1,2,3],[4,5,6]]

Output: [[1,4],[2,5],[3,6]]
 */


#include <vector>
#include <iostream>

using vvi = std::vector<std::vector<int>>;
void printMatrix(vvi const &matrix)
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

vvi transpose(vvi& A)
{
	int colSize = A[0].size();
	int rowSize = A.size();
	vvi transposedMatrix(colSize, std::vector<int>(rowSize, 0));
	for(int i = 0; i<colSize; i++)
	{
		for(int j=0; j<rowSize; j++)
		{
			transposedMatrix[i][j] = A[j][i];
		}
	}
	return transposedMatrix;
}

int main()
{

	vvi test1 = { {1,2,3}, {4,5,6}, {7,8,9} };
	vvi test2 = { {1,2,3}, {4,5,6} };


	vvi result1 = transpose(test1);
	vvi result2 = transpose(test2);

	printMatrix(result1);
	printMatrix(result2);

	return 0;
}
