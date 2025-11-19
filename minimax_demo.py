#!/usr/bin/env python3.11
"""Browser Use 最简洁使用案例 - 使用MiniMax API"""

import asyncio
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

async def demo():
    """演示browser_use基本用法"""
    # 检查API密钥
    api_key = os.getenv('MINIMAX_API_KEY')
    if not api_key:
        print("请设置环境变量: MINIMAX_API_KEY")
        return
    
    print("🚀 开始使用MiniMax API进行browser_use演示...")
    print(f"🔑 API Key已配置: {api_key[:20]}...")
    
    # 导入browser_use并创建Agent
    try:
        from browser_use import Agent
        
        task = "访问 https://github.com 获取页面标题"
        
        agent = Agent(
            task=task,
            llm_provider="minimax"
        )
        
        result = await agent.run()
        print(f"✅ 完成: {result}")
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    asyncio.run(demo())
