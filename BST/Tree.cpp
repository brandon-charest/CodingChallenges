#include "Tree.h"
/*----------------------------------------------------------------------/
/                         Public functions                              /
/*---------------------------------------------------------------------*/

Tree::Tree()
{
	std::cout << std::boolalpha;
	root = NULL;
}

Tree::~Tree()
{
	root.reset();
}

void Tree::isTreeEmpty() const
{
	std::cout << isNodeEmpty(root) << std::endl;
}

void Tree::contains(int const & value) const
{
	
	std::cout << contains(value, root) << std::endl;
}

void Tree::findMin() const
{	
	int result = findMin(root);

	std::cout << "Min is " << result << std::endl;
}

void Tree::findMax() const
{
}

void Tree::insert(int const &value)
{
	insert(value, root);
}

void Tree::preOrder()
{
	preOrder(root);
	std::cout << std::endl;
}

void Tree::inOrder()
{
	inOrder(root);
}

void Tree::postOrder()
{
	postOrder(root);
}

/*----------------------------------------------------------------------/
/                         Private functions                             /
/*---------------------------------------------------------------------*/

bool Tree::contains(int const &value, pNode const &node) const
{
	if (isNodeEmpty(node))
	{
		return false;
	}

	if (value == node->data)
	{
		return true;
	}
	else if (value < node->data)
	{
		contains(value, node->left);
	}
	else
	{
		contains(value, node->right);
	}
}





int &Tree::findMin(pNode const &node) const
{
	auto temp = node.get();

	if (isNodeEmpty(temp))
	{
		while (temp->left != nullptr)
		{
			temp = temp->left.get();
		}
	}

	return temp->data;
}

int Tree::findMax(pNode const &node) const
{
	auto temp = node.get();

	if (isNodeEmpty(temp))
	{
		while (temp->right != nullptr)
		{
			temp = temp->right.get();
		}
	}

	return temp->data;
}

void Tree::insert(int const &value, pNode &node)
{
	if (isNodeEmpty(node))
	{
		node = std::move(node->from(value));
	}
	else if (value < node->data)
	{
		insert(value, node->left);
	}
	else
	{
		insert(value, node->right);
	}
}



void Tree::preOrder(pNode const &node) const
{
	if (!isNodeEmpty(node))
	{
		std::cout << node->data << " ";
		preOrder(node->left);
		preOrder(node->right);
	}	
}

void Tree::inOrder(pNode const & node) const
{
	if (!isNodeEmpty(node))
	{		
		preOrder(node->left);
		std::cout << node->data << " ";
		preOrder(node->right);
	}	
}

void Tree::postOrder(pNode const & node) const
{
	if (!isNodeEmpty(node))
	{		
		preOrder(node->left);
		preOrder(node->right);
		std::cout << node->data << " ";
	}	
}
