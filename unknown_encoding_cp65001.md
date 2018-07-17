# "LookupError: unknown encoding: cp65001"及命令行无法输入中文问题 #

chcp 437

找到两个质量略好的——[stackoverflow1](http://stackoverflow.com/questions/878972/windows-cmd-encoding-change-causes-python-crash)和[stackoverflow2](http://stackoverflow.com/questions/35176270/python-2-7-lookuperror-unknown-encoding-cp65001)。总之是代码页(codepage)的问题，在cmd下chcp命令(大概是change codepage?)可查看当前代码页，chcp nnn可改变当前使用的代码页。 

常用有936-GBK编码，437-美国英语，还有这个出问题的65001-utf-8编码。 

所以解决报错可以每次打开命令行都用chcp 936来更换当前代码页，也可以在属性和默认值里修改。然而修改后重启cmd查看属性还是65001的代码页。


