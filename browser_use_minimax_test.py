#!/usr/bin/env python3.11
"""使用MiniMax API的完整browser_use测试"""

import asyncio
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 导入我们的MiniMax适配器和browser_use
from minimax_llm_adapter import MinimaxChatModel
from browser_use.agent.service import Agent

async def test_browser_use_with_minimax():
    """使用MiniMax LLM测试browser_use"""
    
    # 检查API密钥
    api_key = os.getenv('MINIMAX_API_KEY')
    if not api_key:
        print("❌ 请设置MINIMAX_API_KEY环境变量")
        return
    
    print("🚀 开始browser_use + MiniMax测试...")
    
    # 创建MiniMax LLM实例
    llm = MinimaxChatModel(api_key=api_key)
    print("✅ MiniMax LLM初始化完成")
    
    try:
        # 创建Agent实例
        agent = Agent(
            task="访问 https://www.github.com 并获取页面标题",
            llm=llm
        )
        print("✅ Agent创建完成")
        
        # 执行任务
        print("🌐 开始浏览器任务...")
        result = await agent.run()
        
        print(f"✅ 任务完成!")
        print(f"📄 结果: {result}")
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_browser_use_with_minimax())
