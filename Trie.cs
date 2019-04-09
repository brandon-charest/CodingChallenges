using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace Trie
{
    public class Trie<T> : Node<T>, ITrie<T>
    {
        public IEnumerable<T> Retrieve(string query)
        {
            return Retrieve(query, 0);
        }

        public void Add(string key, T value)
        {
            Add(key, 0, value);
        }
    }
}
