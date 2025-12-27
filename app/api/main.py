from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import time

app = FastAPI(title="FairySearch API", version="1.0.0")

# --- 配置 CORS (解决跨域问题) ---
# 允许前端 (http://localhost:5173) 访问后端
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 数据模型 (Pydantic) ---
class LoginRequest(BaseModel):
    username: str
    password: str

class Video(BaseModel):
    id: str
    title: str
    score: float # AI 推荐分数

# --- 接口定义 ---

@app.get("/")
def read_root():
    return {"status": "online", "system": "FairySearch Backend"}

# 1. 登录接口 (对应前端 authService.js)
@app.post("/api/login")
async def login(data: LoginRequest):
    print(f"收到登录请求: {data.username}")
    
    # 模拟验证逻辑 (实际项目中请查数据库 + Hash密码)
    if data.username == "admin" and data.password == "123456":
        return {
            "token": "fs-token-xyz-123",
            "user": {
                "id": 1,
                "name": "Admin Proxy",
                "role": "admin"
            }
        }
    else:
        # 返回 401 错误，前端会捕获并显示错误信息
        raise HTTPException(status_code=401, detail="身份验证失败 / ACCESS DENIED")

# 2. AI 推荐接口 (模拟)
@app.get("/api/recommend", response_model=List[Video])
async def get_recommendations(user_id: str):
    # 假装在运行复杂的 AI 模型...
    time.sleep(0.5) 
    
    # 模拟 AI 返回的结果
    return [
        {"id": "v-001", "title": "深空引力波观测", "score": 0.98},
        {"id": "v-003", "title": "量子节点 3.0", "score": 0.85},
        {"id": "v-005", "title": "开源信号海", "score": 0.72},
    ]

# 启动命令: uvicorn main:app --reload