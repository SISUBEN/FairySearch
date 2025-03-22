<div align="center">
<h1 size="300%">Fairy Search Engine</h1>
<div align="center">
<img alt="" src="./app/assets/images/H.D.D.png" width="30%" height="30%" />  
</div>
<img alt="" src="https://img.shields.io/pypi/pyversions/Pyside6" />
<img alt="" src="https://img.shields.io/github/commit-activity/y/SISUBEN/FairySearch" />
<img alt="" src="https://img.shields.io/github/last-commit/SISUBEN/FairySearch" />
<img alt="" src="https://img.shields.io/github/contributors-anon/SISUBEN/FairySearch" />
<img alt="" src="https://img.shields.io/github/issues/SISUBEN/FairySearch">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/SISUBEN/FairySearch">
<img alt="GitHub repo file or directory count" src="https://img.shields.io/github/directory-file-count/SISUBEN/FairySearch">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/SISUBEN/FairySearch">
<p>FairySearch 是一个免费的视频搜索引擎，它通过分析用户的浏览数据和喜欢推荐视频。  </p> 

</div>  

<div align="center">  
  
[简体中文](https://github.com/SISUBEN/FairySearch/blob/main/README.md) |
[English](https://github.com/SISUBEN/FairySearch/blob/main/README_en_US.md) |
[繁體中文](https://github.com/SISUBEN/FairySearch/blob/main/README_zh_TW.md)  

</div>       

## 注意事项
> ⚠️使用本程序前请确保本地环境是完整版Python 3.8+  

## 如何使用
- **从源码构建**  
1. 首先使用git克隆本项目`git clone https://github.com/SISUBEN/FairySearch.git`  
2. 切换目录`cd ./FairySearch-main/`  
3. 运行构建脚本（暂时没写好） 

## 使用方法
- **从源码运行**
1. 首先使用git克隆本项目`git clone https://github.com/SISUBEN/FairySearch.git`  
2. 切换目录`cd ./FairySearch-main/`
3. 安装依赖`pip install -r ./requirements.txt`
4. 启动应用`python3 ./fs.py`
   
- **从Release版本运行**
1. 下载Release版本
2. 打开`fs.exe`

## 功能
- [x] 登入
- [x] 注册
- [x] 个人资料
- [x] 视频播放
- [ ] 历史记录
- [ ] 搜索
- [ ] 分析用户喜好

## TODO
- [ ] 视频添加功能
- [ ] 搜索历史
- [ ] 机器学习用户喜好
- [ ] 接入OpenAI/Deepseek等LLM模型

## 技术栈  
|  模块   | 用途  | 引用 |
|  ----  | ----  | ----  |
| PySide6  | 绘制图形界面 | https://doc.qt.io/qtforpython-6/ |
| hashlib  | 加密用户敏感信息 | https://docs.python.org/3/library/hashlib.html |
| sqlite3  | 数据库 | https://docs.python.org/3/library/sqlite3.html |
| Python-vlc | 播放视频 | https://pypi.org/project/python-vlc/ |
| rich | 用於重写部分logging方法，实现多样化日志 | https://pypi.org/project/rich/ | 
| logging | 提供日志 | https://pypi.org/project/logging/ |
| PyQt-Fluent-Widgets | 实现Config类 | https://pypi.org/project/PyQt-Fluent-Widgets/ |

## 免责声明
版权所有 © 2025 SISUBENY。保留所有权利。

FairySearch 是一款用于提交 2026 年香港中学文凭考试 *[HKDSE](https://en.wikipedia.org/wiki/Hong_Kong_Diploma_of_Secondary_Education)* 和资讯及通讯科技 *
(ICT)[https://www.hkeaa.edu.hk/en/hkdse/hkdse_subj.html?A2&2&16]* 校本评估 *
(SBA)[https://www.hkeaa.edu.hk/en/sba/introduction]* 的应用程序。有关此应用程序的更多详细信息，请参阅报告。

Copyright 2025 SISUBENY. license under *
(GPL v3)[https://www.gnu.org/licenses/gpl-3.0.en.html]*
