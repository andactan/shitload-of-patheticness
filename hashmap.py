from dataclasses import dataclass


@dataclass
class Item:
    key: ...
    value: ...


class HashMap:
    def __init__(self, size=16) -> None:
        self.size = size
        self.len = 0
        self.buckets = [[] for _ in range(self.size)]

    def __len__(self):
        return self.len

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __repr__(self):
        items = []
        for bucket in self.buckets:
            for item in bucket:
                items.append(
                    f'{item.key}: {item.value}'
                )

        joined = '\n'.join(items)
        return f"{{\n {joined} \n}}"

    def _hash(self, key):
        if isinstance(key, int):
            hash = key % self.size

        elif isinstance(key, str):
            hash = 11
            for c in key:
                hash = hash * 11 + ord(c)

            hash = hash % self.size

        else:
            raise TypeError('Only integers and strings are allowed')

        return hash

    def put(self, key, value):
        idx = self._hash(key)
        for item in self.buckets[idx]:
            if item.key == key:
                item.value = value
                return

        item = Item(key, value)
        self.buckets[idx].append(item) 
        self.len += 1

    def get(self, key):
        idx = self._hash(key)
        for item in self.buckets[idx]:
            if item.key == key:
                return item.value

        raise KeyError('key not found')

    def remove(self, key):
        idx = self._hash(key)
        for i, item in enumerate(self.buckets[idx]):
            if item.key == key:
                self.buckets[idx].pop(i)
                self.len -= 1
                return

        raise KeyError('key not found')


h = HashMap()
h[5] = 'anan'

print(h[5])
print(len(h))
print(h)