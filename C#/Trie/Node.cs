using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trie
{
    public class Node<T> : NodeBase<T>
    {
        private readonly Dictionary<char, Node<T>> _childrenDictionary;
        private readonly Queue<T> _valuesQueue;

        protected Node()
        {
            _childrenDictionary = new Dictionary<char, Node<T>>();
            _valuesQueue = new Queue<T>();
        }


        protected override int KeyLength => 1;

        protected override IEnumerable<T> Values()
        {
            return _valuesQueue;
        }

        protected override IEnumerable<NodeBase<T>> Children()
        {
            return _childrenDictionary.Values;
        }

        protected override void AddValue(T value)
        {
            _valuesQueue.Enqueue(value);
        }

        protected override NodeBase<T> GetOrCreateChild(char key)
        {
            Node<T> result;
            if (_childrenDictionary.TryGetValue(key, out result))
            {
                return result;
            }

            result = new Node<T>();
            _childrenDictionary.Add(key, result);

            return result;
        }

        protected override NodeBase<T> GetChildOrNull(string query, int position)
        {
            if (query == null)
            {
                throw  new ArgumentNullException(nameof(query));
            }

            Node<T> childNode;
            return _childrenDictionary.TryGetValue(query[position], out childNode) 
                ? childNode 
                : null;
        }
    }
}
