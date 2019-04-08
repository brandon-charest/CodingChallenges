#include "LinkedList.h"

int main()
{
	LinkedList<int> list;

	list.insertBack(1);
	list.insertBack(20);
	list.insertBack(11);
	list.insertBack(4);
	list.insertBack(8);
	list.insertBack(2);
	list.insertBack(5);
	list.insertBack(3);

	std::cout << "Before remove head." << std::endl;
	std::cout << "size: " << list.size() << std::endl;
	list.print();

	std::cout << "After remove head." << std::endl;
	list.removeHead();
	std::cout << "size: " << list.size() << std::endl;
	list.print();

	std::cout << "Remove tail." << std::endl;
	list.removeTail();
	std::cout << "size: " << list.size() << std::endl;
	list.print();

	std::cout << "Remove node 2." << std::endl;
	list.removeNode(2);
	std::cout << "size: " << list.size() << std::endl;
	list.print();

	std::cout << "Sort LinkedList." << std::endl;
	list.sort();
	list.print();


	std::cout << "Reverse LinkedList." << std::endl;
	list.reverse();
	list.print();

	return 0;
}