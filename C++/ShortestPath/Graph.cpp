#include "Graph.h"
#include <limits> // numeric_limits
#include <algorithm> // push_heap, pop_heap, make_heap


Graph::Graph()
{
}


Graph::~Graph()
{
}

void Graph::addVertex(const char &letter, const std::unordered_map<char, int> &edges)
{
	verticies.insert(std::unordered_map<char, const std::unordered_map<char, int>>::value_type(letter, edges));
}

std::vector<char> Graph::shortestPath(const char &start, const char &finish)
{
	if (start == NULL || finish == NULL)
	{
		return{};
	}

	std::unordered_map<char, int> distance;
	std::unordered_map<char, char> previous;
	std::vector<char> nodes;
	std::vector<char> path;

	// [&] capture all variables within the lambda function scope by reference
	auto comparator = [&](char left, char right) {return distance[left] > distance[right]; };

	for (auto const &vertex : verticies)
	{
		if (vertex.first == start)
		{
			distance[vertex.first] = 0;
		}
		else
		{
			// Returns the maximum finite value
			distance[vertex.first] = std::numeric_limits<int>::max();
		}

		nodes.push_back(vertex.first);
		std::push_heap(std::begin(nodes), std::end(nodes), comparator);
	}

	while (!nodes.empty())
	{
		std::pop_heap(std::begin(nodes), std::end(nodes), comparator);

		char smallest = nodes.back();
		nodes.pop_back();

		if (smallest == finish)
		{
			while (previous.find(smallest) != std::end(previous))
			{
				path.push_back(smallest);
				smallest = previous[smallest];
			}

			break;
		}

		if (distance[smallest] == std::numeric_limits<int>::max())
		{
			break;
		}

		for (auto &neighbor : verticies[smallest])
		{
			int alt = distance[smallest] + neighbor.second;

			if (alt < distance[neighbor.first])
			{
				distance[neighbor.first] = alt;
				previous[neighbor.first] = smallest;

				std::make_heap(std::begin(nodes), std::end(nodes), comparator);
			}
		}

	}
	std::reverse(path.begin(), path.end());

	return path;
}
