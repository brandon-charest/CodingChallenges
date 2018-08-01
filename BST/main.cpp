#include "Tree.h"

int main()
{

	Tree tree;

	tree.insert(3);
	tree.insert(5);
	tree.insert(1);

	std::cout << "Min is " << tree.getMin() << std::endl;

	return 0;
}