# difflib — Compare Sequences

URL: https://pymotw.com/3/difflib/

The `difflib` module contains tools for computing and working with **differences** between **sequences**. It is **especially useful for comparing text**, and includes functions that produce reports using several common **difference formats**.

> 这段话掌握三个重点：
> （1）`difflib`用于比较sequence之间的差异differences
> （2）特别适用于比较文本text
> （3）比较的结果可以输出成不同的格式difference format


## Comparing Bodies of Text

The `Differ` class works on sequences of text lines and produces human-readable deltas, or change instructions, including differences within individual lines. The default output produced by `Differ` is similar to the `diff` command-line tool under Unix. It includes the original input values from both lists, including common values, and **markup data** to indicate which changes were made.

- Lines prefixed with `-` were in **the first sequence**, but not the second.
- Lines prefixed with `+` were in **the second sequence**, but not the first.
- If a line has **an incremental difference** between versions, an extra line prefixed with `?` is used to highlight the change within the new version.
- If a line has not changed, it is printed with **an extra blank space** on the left column so that it is aligned with the other output that may have differences.

Breaking the text up into a sequence of individual lines before passing it to `compare()` produces more readable output than passing in large strings.

```python
text1 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor.  In nec mauris eget magna consequat
convalis. Nam sed sem vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate
tristique enim. Donec quis lectus a justo imperdiet tempus."""

text1_lines = text1.splitlines()

text2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar, porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor. In nec mauris eget magna consequat
convalis. Nam cras vitae mi vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Duis vulputate tristique enim. Donec quis lectus a
justo imperdiet tempus.  Suspendisse eu lectus. In nunc."""

text2_lines = text2.splitlines()

```

```python
import difflib

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print("\n".join(diff))

```

Or

```python
import difflib

diff = difflib.ndiff(text1_lines, text2_lines)
print("\n".join(diff))
```

在markup上，两者有细微的差别，我喜欢后者。