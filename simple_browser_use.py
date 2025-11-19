#!/usr/bin/env python3.11
"""极简browser_use案例"""

import asyncio
import os
from dotenv import load_dotenv
from browser_use.agent.service import Agent

async def simple_demo():
    """极简演示"""
    # 检查API密钥
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
    
    print("🚀 极简browser_use演示")
    
    # 创建一个非常简单的任务
    agent = Agent(
        task="说'Hello World'"
    )
    
    try:
        result = await agent.run()
        print(f"✅ 完成: {result}")
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    asyncio.run(simple_demo())
