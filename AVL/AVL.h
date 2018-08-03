#pragma once
#include "Tree.h"


class AVL : public Tree
{
public:
	AVL();
	~AVL();

	void getHeight() const;
	void insert(int const &value);

private:	

	int getHeight(pNode const &root) const;
	int difference(pNode const &node) const;

	pNode balance(pNode node);
	pNode rrRotate(pNode &root);
	pNode llRotate(pNode &root);
	pNode lrRotate(pNode &root);
	pNode rlRotate(pNode &root);
};

