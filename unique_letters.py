def unique(s):
    seen = set()
    for i in s:
        if i in seen:
            return False
        seen.add(i)
    return True
print(uniqe(hello))
