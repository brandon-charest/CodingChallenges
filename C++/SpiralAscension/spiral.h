#pragma once
#include <vector>


typedef std::vector<std::vector<int>> vvi;

class Spiral
{
	
public:	

	enum Direction
	{
		ClockWise,
		CounterClockWise
	};


	void spiral(int num, Direction);
private:
	
	//create matrix
	vvi matrix;

	int max;
	int current ;
	int top ;
	int bottom;
	int left ;
	int right ;

	void leftToRight();
	void rightToLeft();
	void topToBottom();
	void bottomToTop();

	void leftToRightCounter();
	void rightToLeftCounter();
	void topToBottomCounter();
	void bottomToTopCounter();


	vvi generateMatrix(int);
	void clockwiseSpiral(vvi);
	void counterSpiral(vvi);
	void print(vvi matrix);
};

