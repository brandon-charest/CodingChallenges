#include "Tree.h"

int main()
{

	Tree t;	

	t.insert(3);
	t.insert(5);
	t.insert(1);
	t.insert(7);
	t.insert(6);
	t.preOrder();	
	t.findMin();
	t.findMax();
	t.contains(1);
	t.isTreeEmpty();
	t.remove(7);
	t.insert(-3);
	t.insert(-2);
	t.insert(-1);
	t.preOrder();
	t.remove(-3);
	t.findMax();
	t.preOrder();

	t.~Tree();

	t.isTreeEmpty();

	return 0;
}