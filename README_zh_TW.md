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
<p>FairySearch 是一個免費的影片搜尋引擎，它透過分析使用者的瀏覽資料和喜歡推薦影片。 </p>

</div>

<div align="center">

[简体中文](https://github.com/SISUBEN/FairySearch/blob/main/README.md) |
[English](https://github.com/SISUBEN/FairySearch/blob/main/README_en_US.md) |
[繁體中文](https://github.com/SISUBEN/FairySearch/blob/main/README_zh_TW.md)

</div>

## 注意事項

> ⚠️ 使用本程式前請確保本地環境是完整版 Python 3.8+

## 如何使用

- **從原始碼建構**

1. 先使用 git 克隆本專案`git clone https://github.com/SISUBEN/FairySearch.git`
2. 切換目錄`cd ./FairySearch-main/`
3. 執行建置腳本（暫時沒寫好）

## 使用方法

- **從原始碼運行**

1. 先使用 git 克隆本專案`git clone https://github.com/SISUBEN/FairySearch.git`
2. 切換目錄`cd ./FairySearch-main/`
3. 安裝依賴`pip install -r ./requirements.txt`
4. 啟動應用程式`python3 ./fs.py`

- **從 Release 版本運行**

1. 下載 Release 版本
2. 開啟`fs.exe`

## 功能

- [x] 登入
- [x] 註冊
- [x] 個人資料
- [x] 影片播放
- [ ] 歷史記錄
- [ ] 搜尋
- [ ] 分析使用者喜好

## TODO

- [ ] 影片新增功能
- [ ] 搜尋紀錄
- [ ] 機器學習使用者喜好
- [ ] 接入 OpenAI/Deepseek 等 LLM 模型

## 技術棧

| 模組                | 用途                                      | 引用                                           |
| ------------------- | ----------------------------------------- | ---------------------------------------------- |
| PySide6             | 繪製圖形介面                              | https://doc.qt.io/qtforpython-6/               |
| hashlib             | 加密使用者敏感資訊                        | https://docs.python.org/3/library/hashlib.html |
| sqlite3             | 資料庫                                    | https://docs.python.org/3/library/sqlite3.html |
| Python-vlc          | 播放影片                                  | https://pypi.org/project/python-vlc/           |
| rich                | 用於重寫部分 logging 方法，實現多樣化日誌 | https://pypi.org/project/rich/                 |
| logging             | 提供日誌                                  | https://pypi.org/project/logging/              |
| PyQt-Fluent-Widgets | 實作 Config 類別                          | https://pypi.org/project/PyQt-Fluent-Widgets/  |

## 免責聲明

版權所有 © 2025 SISUBENY。保留所有權利。

FairySearch 是一款用於提交 2026 年香港中學文憑考試 [HKDSE](https://en.wikipedia.org/wiki/Hong_Kong_Diploma_of_Secondary_Education) 和資訊及通訊科技校本評估的應用程式。有關此應用程式的更多詳細信息，請參閱報告。

本文件是 FairySearch 的一部分。

FairySearch 是自由軟體：你可以再分發之和/或依照由自由軟體基金會發布的 GNU 通用公共許可證修改之，無論是版本 3 許可證，還是（按你的決定）任何以後版都可以。

發布 Fa​​irySearch 是希望它能有用，但是並無保障;甚至連可銷售和符合某個特定的目的都不保證。請參閱 GNU 通用公共許可證，了解詳情。

你應該隨程式取得一份 GNU 通用公共授權的複本。如果沒有，請看 https://www.gnu.org/licenses/。
