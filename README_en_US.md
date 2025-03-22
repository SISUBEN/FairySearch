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
<p>FairySearch is a free video search engine that recommends videos by analyzing users' browsing data and likes. </p>

</div>

<div align="center">

[简体中文](https://github.com/SISUBEN/FairySearch/blob/main/README.md) |
[English](https://github.com/SISUBEN/FairySearch/blob/main/README_en_US.md) |
[繁體中文](https://github.com/SISUBEN/FairySearch/blob/main/README_zh_TW.md)  

</div>

## Notes
> ⚠️ Before using this program, please make sure that your local environment is the full version of Python 3.8+

## How to use
- **Build from source**
1. First use git to clone this project `git clone https://github.com/SISUBEN/FairySearch.git`
2. Switch directory `cd ./FairySearch-main/`
3. Run the build script (not yet written)

## How to use
- **Run from source code**
1. First use git to clone this project `git clone https://github.com/SISUBEN/FairySearch.git`
2. Switch directory `cd ./FairySearch-main/`
3. Install dependencies `pip install -r ./requirements.txt`
4. Start the application `python3 ./fs.py`

- **Run from Release version**
1. Download Release version
2. Open `fs.exe`

## Functions
- [x] Login
- [x] Register
- [x] Profile
- [x] Video playback
- [ ] History
- [ ] Search
- [ ] Analyze user preferences

## TODO
- [ ] Video add function
- [ ] Search history
- [ ] Machine learning user preferences
- [ ] Connect to OpenAI/Deepseek and other LLM models

## Technology stack
| Module | Purpose | Reference |
| ---- | ---- | ---- |
| PySide6 | Draw graphical interface | https://doc.qt.io/qtforpython-6/ |
| hashlib | Encrypt user sensitive information | https://docs.python.org/3/library/hashlib.html |
| sqlite3 | Database | https://docs.python.org/3/library/sqlite3.html |
| Python-vlc | Play video | https://pypi.org/project/python-vlc/ |
| rich | Used to rewrite some logging methods and implement diversified logging | https://pypi.org/project/rich/ |
| logging | Provide logs | https://pypi.org/project/logging/ |
| PyQt-Fluent-Widgets | Implement Config class | https://pypi.org/project/PyQt-Fluent-Widgets/ |

## Disclaimer
Copyright © 2025 SISUBENY. All rights reserved.

FairySearch is an application for submission of 2026 Hong Kong Diploma of Secondary Education Examination *[HKDSE](https://en.wikipedia.org/wiki/Hong_Kong_Diploma_of_Secondary_Education)* and Information and Communications Technology *
(ICT)[https://www.hkeaa.edu.hk/en/hkdse/hkdse_subj.html?A2&2&16]* School-Based Assessment *
(SBA)[https://www.hkeaa.edu.hk/en/sba/introduction]*. For more details on this application, please refer to the report.

Copyright 2025 SISUBENY. license under *
(GPL v3)[https://www.gnu.org/licenses/gpl-3.0.en.html]*

This file is part of FairySearch.
FairySearch is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
FairySearch is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with FairySearch. 
If not, see <https://www.gnu.org/licenses/>.
