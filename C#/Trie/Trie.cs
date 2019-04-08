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
            throw new NotImplementedException();
        }

        public void add(string key, T value)
        {
            throw new NotImplementedException();
        }
    }
}
