#include "AVL.h"
#include <algorithm>


AVL::AVL()
{
	Tree();
}


AVL::~AVL()
{
}



void AVL::getHeight() const
{
	std::cout << "Height of tree: " << getHeight(root) << std::endl;
}

void AVL::insert(int const & value) 
{
	Tree::insert(value);
	//root = balance(std::move(root));
}

int AVL::getHeight(pNode const &node) const
{
	if (isNodeEmpty(node))
	{
		return 0;
	}	

	int height = std::max(getHeight(node->left), getHeight(node->right));

	return height +1 ;
}

int AVL::difference(pNode const &node) const
{	
	return getHeight(node->left) - getHeight(node->right);;
}

Tree::pNode AVL::balance(pNode node)
{

	int balanceFactor = difference(node);

	if (balanceFactor > 1)
	{
		if (difference(node->left) > 0)
		{
			node = std::move(llRotate(node));
		}
		else
		{
			node = std::move(lrRotate(node));
		}
	}
	else if (balanceFactor < -1)
	{
		if (difference(node->right) > 0)
		{
			node = std::move(rlRotate(node));
		}
		else
		{
			node = std::move(rrRotate(node));
		}
	}

	return node;
}

Tree::pNode AVL::rrRotate(pNode &node)
{
	auto temp = std::move(node);
	temp = std::move(node->right);
	node->right = std::move(temp->left);
	temp->left = std::move(node);

	return temp;
}

Tree::pNode AVL::llRotate(pNode &node)
{
	auto temp = std::move(node);
	temp = std::move(node->left);
	node->left = std::move(temp->right);
	temp->right = std::move(node);

	return temp;
}

Tree::pNode AVL::lrRotate(pNode &node)
{
	auto temp = std::move(node->left);
	node->left = rrRotate(temp);
	
	return llRotate(node);
}

Tree::pNode AVL::rlRotate(pNode &node)
{
	auto temp = std::move(node->right);
	node->right = llRotate(temp);

	return rrRotate(node);
}
