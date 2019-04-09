using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trie
{
    public abstract class NodeBase<T>
    {
        protected abstract int KeyLength { get; }
        protected abstract IEnumerable<T> Values();
        protected abstract IEnumerable<NodeBase<T>> Children();

        public void Add(string key, int position, T value)
        {
            if (key == null)
            {
                throw new ArgumentNullException(nameof(key));
            }

            if (EndOfString(position, key))
            {
                AddValue(value);
                return;
            }

            var child = GetOrCreateChild(key[position]);
            child.Add(key, position++, value);
        }

        protected abstract void AddValue(T value);
        protected abstract NodeBase<T> GetOrCreateChild(char key);
        protected abstract NodeBase<T> GetChildOrNull(string query, int position);
        protected virtual IEnumerable<T> Retrieve(string query, int position)
        {
            return EndOfString(position, query) 
                ? ValuesDeep() 
                : SearchDeep(query, position);
        }

        protected virtual IEnumerable<T> SearchDeep(string query, int position)
        {
            var nextNode = GetChildOrNull(query, position);

            return nextNode != null 
                ? nextNode.Retrieve(query, position + nextNode.KeyLength) 
                : Enumerable.Empty<T>();
        }

        private IEnumerable<T> ValuesDeep()
        {
            return SubTree().SelectMany(node => node.Values());
        }

        protected IEnumerable<NodeBase<T>> SubTree()
        {
            return Enumerable.Repeat(this, 1).Concat(Children().SelectMany(child => child.SubTree()));
        }

        private static bool EndOfString(int position, string text)
        {
            return position >= text.Length;
        }
    }
}
