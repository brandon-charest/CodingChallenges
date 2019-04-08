using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trie
{
    public class Node<T> : NodeBase<T>
    {
        protected override int KeyLength { get; }
        protected override IEnumerable<T> Values()
        {
            throw new NotImplementedException();
        }

        protected override IEnumerable<NodeBase<T>> Children()
        {
            throw new NotImplementedException();
        }

        protected override void AddValue(T value)
        {
            throw new NotImplementedException();
        }
    }
}
