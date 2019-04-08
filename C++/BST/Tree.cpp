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

void Tree::remove(int const &value)
{
	std::cout << "Removing " << value << std::endl;
	remove(value, root);
}

void Tree::isTreeEmpty() const
{
	std::cout << "Tree empty? " << isNodeEmpty(root) << std::endl;
}

void Tree::contains(int const &value) const
{
	
	std::cout << "Contain " << value << "? " << contains(value, root) << std::endl;
}

void Tree::findMin() const
{	
	int result = findMin(root);

	std::cout << "Min is " << result << std::endl;
}

void Tree::findMax() const
{
	int result = findMax(root);

	std::cout << "Max is " << result << std::endl;
}

void Tree::insert(int const &value)
{
	std::cout << "Inserting " << value << std::endl;
	insert(value, root);
}

void Tree::preOrder() const
{
	std::cout << "PreOrder: ";
	preOrder(root);
	std::cout << std::endl;
}

void Tree::inOrder() const
{
	std::cout << "InOrder: ";
	inOrder(root);
	std::cout << std::endl;
}

void Tree::postOrder() const
{
	std::cout << "PostOrder: ";
	postOrder(root);
	std::cout << std::endl;
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

	if (!isNodeEmpty(temp))
	{
		while (!isNodeEmpty(temp->left))
		{
			temp = temp->left.get();
		}
	}

	return temp->data;
}

int &Tree::findMax(pNode const &node) const
{
	auto temp = node.get();

	if (!isNodeEmpty(temp))
	{
		while (!isNodeEmpty(temp->right))
		{
			temp = temp->right.get();
		}
	}

	return temp->data;
}

void Tree::remove(int const &value, pNode &node)
{
	if (isNodeEmpty(node))
	{
		return;
	}

	if (value < node->data)
	{
		remove(value, node->left);
	}
	else if (value > node->data)
	{
		remove(value, node->right);
	}
	else
	{
		// no children
		if (isNodeEmpty(node->left) && isNodeEmpty(node->right))
		{
			node.reset();
		}
		// two children 
		else if (!isNodeEmpty(node->left) && !isNodeEmpty(node->right))
		{			
			node->data = findMin(node->right);
			remove(node->data, node->right);
		}
		// one child
		else
		{
			auto tempNode = node.get();
			node = (isNodeEmpty(tempNode->left)) ? std::move(tempNode->right) : std::move(tempNode->left);
		}
	}
	
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
