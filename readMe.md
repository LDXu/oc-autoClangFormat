
项目格式化脚本

适用场景
1.老项目或者需要格式化的项目
2.提交时格式下统一下格式

使用说明
1.使用brew安装clang-format
brew install clang-format
比较卡的话，可以开个全局代理，命令行代理export https_proxy="http://127.0.0.1:1087"

2.三个文件放到项目目录下，使用py3运行py文件
python ClangFormat.py 或者 python3 ClangFormat.py

3.自定义部分
#可修改 需要过滤的目录，注意不要和项目主目录同名
Filter_DIRS = []
#可修改 需要过滤的文件
Filter_FILES = []

4.可在Xcode script 添加python脚本运行,编译慢的话，添加单独的一个targets autoClangFormat


Xcode插件（单个文件格式化）
https://github.com/mapbox/XcodeClangFormat
规则文件参考压缩包里的文件.clang-format
