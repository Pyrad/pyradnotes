# Read the Doc Related



RTD的官方网址：[https://readthedocs.org/](https://readthedocs.org/)



## 在RTD上使用markdown tables

目前，似乎RTD不能自己下载对应的`sphinx_markdown_tables`这个package，需要手动在目录中添加它以及它的依赖包`markdown`。



在repository [pyradnotes](https://gitee.com/pyrad/pyradnotes) 中，构造文档需要手动上传的package是`sphinx_markdown_tables`和它的一个依赖package `Markdown`。

只需要使用`pip`下载`sphinx_markdown_tables`这个package即可，它会下载它本身以及需要的依赖包。

```shell
pip download sphinx_markdown_tables -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -d "D:\Programs\MyPyPackages\sphinx_markdown_tables_221007"
```

下载之后，目录中会有四个文件

```shell
importlib_metadata-5.0.0-py3-none-any.whl
Markdown-3.4.1-py3-none-any.whl
sphinx_markdown_tables-0.0.17-py3-none-any.whl
zipp-3.8.1-py3-none-any.whl
```

这里有用的是以下两个

```shell
Markdown-3.4.1-py3-none-any.whl
sphinx_markdown_tables-0.0.17-py3-none-any.whl
```

把它们的后缀修改为`.zip`，然后分别：

- 从`Markdown-3.4.1-py3-none-any.zip`解压出来`markdown`目录
- 从`sphinx_markdown_tables-0.0.17-py3-none-any.zip`解压出来`sphinx_markdown_tables`目录

然后把这两个目录放入repo中对应的目录即可。



在repository [pyradnotes](https://gitee.com/pyrad/pyradnotes) 中，[source/pyextensions](https://gitee.com/pyrad/pyradnotes.git) 是我用来放置手动上传的package的目录。

放置完成之后，需要在`source/conf.py`中添加对应的命令，以便python解释器可以找到这个手动上传的包的路径。

```python
if os.environ.get('READTHEDOCS', None) == 'True':
    sys.path.insert(0, os.path.abspath(os.path.join('.', 'pyextensions')))
    sys.path.insert(0, os.path.abspath('.'))
    import sphinx_markdown_tables
```



