#include "AVL.h"

int main()
{

	AVL t;
	
	t.insert(3);
	t.insert(5);
	t.insert(1);
	t.insert(7);
	t.insert(6);
	t.preOrder();
	t.getHeight();
	

	return 0;
}