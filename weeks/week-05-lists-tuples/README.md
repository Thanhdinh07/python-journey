# Python Practice Exercises

A set of short, focused exercises for practicing core Python fundamentals, organized by week.

## Week 5 — Lists, Slicing & Tuples

| File | Topic |
|---|---|
| `ex01_lists.py` | List CRUD — append, insert, update, remove, pop, slicing |
| `ex02_slicing.py` | Slicing, mutability, alias vs. shallow copy |
| `ex03_tuples.py` | Tuple packing/unpacking, multiple assignment, swap idiom |


## How to run

Each file is standalone. Run any of them directly with Python 3.10+:

```bash
python ex01_lists.py
```

## Notes

### Week 5

**Lists (`ex01_lists.py`)**
- `insert(i, x)` places an item at a specific index.
- `remove(x)` deletes by value (first match found).
- `pop()` / `pop(i)` deletes by index and returns the removed item.

**Slicing & mutability (`ex02_slicing.py`)**
- `alias = numbers` does **not** copy — both names reference the same list, so mutating one affects the other.
- `numbers[:]` (or `.copy()`) creates an independent shallow copy.
- Slices like `numbers[:3]` always produce a brand-new list.

**Tuples (`ex03_tuples.py`)**
- `x, y = coordinate` unpacks a tuple in one line.
- The swap idiom `left, right = right, left` works because the right-hand side is fully evaluated into a temporary tuple before assignment happens.

