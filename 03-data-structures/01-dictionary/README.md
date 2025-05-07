# Python Dictionaries

## Overview

Dictionaries are one of Python's most powerful data structures. They store data as key-value pairs, allowing you to quickly retrieve values using their associated keys. Dictionaries are mutable, dynamic, and extremely versatile for representing real-world relationships.

## Key Concepts

1. **Dictionary Basics** - Creation, access, modification and deletion
2. **Dictionary Methods** - Built-in functions for working with dictionaries
3. **Dictionary Comprehensions** - Concise way to create dictionaries
4. **Nested Dictionaries** - Dictionaries within dictionaries for complex data
5. **Common Dictionary Operations** - Iteration, merging, and more

## Detailed Explanation

### Dictionary Basics

Dictionaries are defined using curly braces `{}` with key-value pairs separated by colons:

```python
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Computer Science"]
}
```

Key characteristics:
- Keys must be hashable (immutable) types like strings, numbers, or tuples
- Values can be any Python object
- Order of insertion is preserved (Python 3.7+)
- Dictionary lookups are very fast, even for large datasets

### Dictionary Methods

Python provides many built-in methods for working with dictionaries:

| Method | Description | Example |
|--------|-------------|---------|
| `dict.get(key, default)` | Returns value for key, or default if key doesn't exist | `student.get("name", "Unknown")` |
| `dict.keys()` | Returns view of all keys | `student.keys()` |
| `dict.values()` | Returns view of all values | `student.values()` |
| `dict.items()` | Returns view of all key-value pairs | `student.items()` |
| `dict.update(other_dict)` | Updates dictionary with key-value pairs from another | `student.update({"year": "Junior"})` |
| `dict.pop(key)` | Removes key and returns its value | `student.pop("age")` |
| `dict.clear()` | Removes all items | `student.clear()` |

### Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries:

```python
# Create a dictionary of squares {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
squares = {x: x**2 for x in range(5)}

# Filtering with conditions
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
```

### Nested Dictionaries

Dictionaries can contain other dictionaries as values, allowing you to represent hierarchical data:

```python
university = {
    "Computer Science": {
        "Alice": {"grade": "A", "year": 3},
        "Bob": {"grade": "B", "year": 2}
    },
    "Mathematics": {
        "Charlie": {"grade": "A", "year": 4},
        "David": {"grade": "C", "year": 1}
    }
}

# Accessing nested values
alice_grade = university["Computer Science"]["Alice"]["grade"]  # "A"
```

## Common Pitfalls

- **KeyError**: Attempting to access a non-existent key without using `.get()` raises a KeyError
- **Unhashable keys**: Using mutable types like lists as keys will raise an error
- **Modifying during iteration**: Changing a dictionary while iterating over it can cause unexpected behavior

## Best Practices

- Use `.get()` method with a default value to avoid KeyError exceptions
- Choose meaningful and consistent keys
- For dictionaries storing object attributes, consider using a class instead
- Use the `collections.defaultdict` for dictionaries with default values
- When dealing with JSON data, use `json.loads()` to convert JSON to dictionaries

## Real-world Applications

- Configuration settings
- Caching results of expensive operations
- Counting occurrences (frequency counters)
- Representing JSON data
- Implementing complex data structures like graphs (adjacency lists)

## Further Reading

- [Python Dictionary Documentation](https://docs.python.org/3/library/stdtypes.html#dict)
- [Collections Module](https://docs.python.org/3/library/collections.html) for specialized dictionary types
- [Python Dictionary Design and Implementation](https://www.youtube.com/watch?v=npw4s1QTmPg) - PyCon talk by Raymond Hettinger 