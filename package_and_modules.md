# Python module Vs Python package

A **package** is a collection of **Python modules**: while a **module** is **a single Python file**, a **package** is a directory of **Python modules** containing an additional `__init__.py` file, to distinguish a **package** from a **directory** that just happens to contain a bunch of Python scripts. Packages can be nested to any depth, provided that the corresponding directories contain their own `__init__.py` file.

`__init__.py` makes a directory a Python package. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__` variable.

