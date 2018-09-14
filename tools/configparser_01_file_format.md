# configparser: Work with Configuration Files
Use the `configparser` module to manage user-editable configuration files for an application using a format similar to Windows INI files. 

**The contents of the configuration files** can be organized into **groups** and several **option value types** are supported, including integers, floating-point values, and booleans. **Option values** can be combined using **Python formatting strings** to build longer values such as `URLs` from shorter values such as `hostnames` and `port` numbers.

## Configuration File Format 配置文件的格式

The file format used by `configparser` is similar to the format used by older versions of Microsoft Windows. It consists of one or more named `sections`, each of which can contain individual `options` with `names` and `values`.

> 这段意思：  
> （1）配置文件由多个section组成。  
> （2）一个section由多个option组成。  
> （3）一个option由name和value组成。  

The parser identifies **config file sections** by looking for lines starting with `[` and ending with `]`. The value between the square brackets is the **section name**, and can contain any characters except square brackets.

> section的分隔符

**Options** are listed **one per line** within a section. The line starts with the `name` of the `option`, which is separated from the value by a **colon** (`:`) or **equal sign** (`=`). **Whitespace** around the separator is ignored when the file is parsed.

> option的分隔符

Lines starting with a **semicolon** (`;`) or an **octothorpe** (`#`) are treated as comments. They are ignored when the contents of the configuration file are accessed programmatically.

> 注释

The following sample configuration file contains a `section` named `bug_tracker` with three `options`: `url` , `username` , and `password`.

```txt
# This is a simple example with comments.
[bug_tracker]
url = http://localhost:8080/bugs/
username = admin
; You should not store passwords in plain text
; configuration files.
password = SECRET
```

