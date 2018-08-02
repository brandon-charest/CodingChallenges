#include "Tree.h"

int main()
{

	Tree t;

	t.insert(3);
	t.insert(5);
	t.insert(1);

	t.preOrder();

	t.findMin();
	t.contains(1);
	t.isTreeEmpty();

	t.~Tree();

	t.isTreeEmpty();

	return 0;
}