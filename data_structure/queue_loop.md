# How to iterate queue.Queue items in Python?

URL: https://stackoverflow.com/questions/8196254/how-to-iterate-queue-queue-items-in-python/8196904

You can loop over a copy of the underlying data store:

```python
for elem in list(q.queue)
```

Eventhough this bypasses the locks for `Queue` objects, the list copy is an atomic operation and it should work out fine.







