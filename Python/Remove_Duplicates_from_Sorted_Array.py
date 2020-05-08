def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    t = list(t)
    for ch in s:
        if ch in t:
            t.remove(ch)
    if len(t) > 0:
        return False
    return True

s = "anagram"
t = "nagaram"

print(isAnagram(s,t))