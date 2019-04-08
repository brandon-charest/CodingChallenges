#pragma once
#include <unordered_map>

class Graph
{
public:
	Graph();
	~Graph();

	void addVertex(const char &letter, const std::unordered_map<char, int> &edges);
	std::vector<char> shortestPath(const char &start, const char &end);

private:
	std::unordered_map<char, const std::unordered_map<char, int>> verticies;
};

