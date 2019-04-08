using System;
using System.Collections.Generic;
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

        }

        protected abstract void AddValue(T value);
    }
}
