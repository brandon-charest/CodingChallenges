using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trie
{
    public interface ITrie<T>
    {
        IEnumerable<T> Retrieve(string query);
        void Add(string key, T value);
    }
}
