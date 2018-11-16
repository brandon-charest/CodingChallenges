/*654. Maximum Binary Tree

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

	6
  /   \
 3     5
  \    /
   2  0
    \
     1
*/

//Definition for a binary tree node.
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	
};

void printTree(TreeNode const *node)
{
	if(node != nullptr)
	{
		std::cout << node->val << " ";
		printTree(node->left);
		printTree(node->right);
	}
}
// First attempt. Start

/*void add_node(TreeNode *&node, int val)
{
	if(node == nullptr)
	{
		node = new TreeNode(val);
	}
	else if(val < node->val)
	{
		add_node(node->left, val);
	}
	else
	{
		add_node(node->right, val);
	}
}


TreeNode* constructMaximumBinaryTree(std::vector<int>& nums)
{
	if (nums.empty())
	{
		return nullptr;
	}

	auto const maxNum = std::distance(nums.begin(), std::max_element(nums.begin(), nums.end()));

	auto *maxTree = new TreeNode(nums[maxNum]);

	std::vector<int> leftSide = {};
	std::vector<int> rightSide = {};

	for (auto i = 0; i < nums.size(); i++)
	{
		if (i < maxNum)
		{
			leftSide.push_back(nums[i]);
		}
		else if (i > maxNum)
		{
			rightSide.push_back(nums[i]);
		}
	}

	std::sort(leftSide.begin(), leftSide.end(), std::greater<>());
	std::sort(rightSide.begin(), rightSide.end(), std::greater<>());


	for (auto value : leftSide)
	{
		add_node(maxTree->left, value);
	}

	for (auto value : rightSide)
	{
		add_node(maxTree->right, value);
	}
	return maxTree;
}*/

//First attempt end


TreeNode* constructTree(std::vector<int> &nums, int start, int end)
{
	if(start > end)
	{
		return nullptr;
	}

	const auto maxNumberIndex = std::distance(nums.begin(), std::max_element(nums.begin() + start, nums.begin() + end + 1));

	TreeNode *root = new TreeNode(nums[maxNumberIndex]);
	root->left = constructTree(nums, start, maxNumberIndex - 1);
	root->right = constructTree(nums, maxNumberIndex + 1, end);

	return root;

}

TreeNode* constructMaximumBinaryTree(std::vector<int>& nums)
{
	return constructTree(nums, 0, nums.size() - 1);
}


int main()
{
	std::vector<int> numbers = { 3,2,1,6,0,5 };

	

	TreeNode *tree = constructMaximumBinaryTree(numbers);

	printTree(tree);

	return 0;
}