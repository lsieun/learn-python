# Mapping Types — dict

URL: https://docs.python.org/3/library/stdtypes.html#dict


## create dict

```python
>>> a = dict(one=1, two=2, three=3)
>>> b = {'one': 1, 'two': 2, 'three': 3}
```

## set

```python
d[key] = value
```
Set `d[key]` to value.

```python
setdefault(key[, default])
```

If `key` is in the dictionary, return **its value**. If not, insert `key` with a value of `default` and return `default`. `default` defaults to `None`.

## fetch

```python
get(key[, default])
```

Return the value for `key` if `key` is in the dictionary, else `default`. If `default` is not given, it defaults to `None`, so that this method never raises a `KeyError`.

## delete

```python
del d[key]
```

Remove `d[key]` from `d`. Raises a `KeyError` if `key` is not in the map.

```python
pop(key[, default])
```

If `key` is in the dictionary, remove it and return its value, else return `default`. If `default` is not given and `key` is not in the dictionary, a `KeyError` is raised.

```python
clear()
```
Remove all items from the dictionary.

## in

- `key in d`: Return `True` if `d` has a key `key`, else `False`.
- `key not in d`: Equivalent to `not key in d`.

## iter

- `iter(d)`: Return an iterator over the keys of the dictionary. This is a shortcut for `iter(d.keys())`.
- `items()`: Return a new view of the dictionary’s items (`(key, value)` pairs).
- `keys()`: Return a new view of the dictionary’s keys.
- `values()`: Return a new view of the dictionary’s values.


