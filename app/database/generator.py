import sqlite
import random
# sh_db = sqlite.Database.SearchHistorydb()
video_db = sqlite.Database.Videodb()
# user_db = sqlite.Database.Userdb()
video_db.init_videodb()
name_list = [
    "《崩坏：星穹铁道》飞霄角色PV——「君莫笑」",
    "全网首发！揭秘狐人英雄的真面目——《崩坏：星穹铁道》星间纪实",
    "《崩坏：星穹铁道》动画短片：「清闲自在身」",
    "《崩坏：星穹铁道》走近星穹——「貊泽：千里不留行」",
    "《崩坏：星穹铁道》走近星穹——「飞霄：如何练就西瓜般的腱子肉」",
    "《崩坏：星穹铁道》千星纪游PV：「飞镝追星」",
]
video_type = [
    "游戏",
    "手机游戏",
    "崩坏：星穹铁道",
    "崩坏星穹铁道",
    "飞霄",
    "崩坏星穹铁道飞霄",
    "碧羽飞黄射天狼",
    "米哈游",
    "miHoYo",
]

for i in range(6):
    video_db.video_add(
        name=name_list[random.randint(0, len(name_list) - 1)],
        type=video_type[random.randint(0, len(video_type) - 1)],
        url="",
        author="米哈游",
    )