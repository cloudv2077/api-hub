#!/usr/bin/env python3.11
"""快速多步骤LLM演示"""

import asyncio
import os

async def quick_demo():
    """快速演示"""
    
    print("🎯 多步骤LLM自动判断演示")
    print("=" * 50)
    
    # 检查API密钥
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY环境变量")
        return
    
    try:
        # 导入我们的适配器
        from minimax_llm_adapter import MinimaxChatModel
        from browser_use.llm.messages import UserMessage
        
        llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
        
        # 简单多步骤任务
        task = "分析一个移动应用的优化方向"
        
        print(f"📱 任务: {task}")
        print("\n🔄 步骤1: 初步分析")
        
        step1_prompt = "请分析移动应用优化的3个主要方向，并指出哪个最重要"
        
        result1 = await llm.ainvoke([UserMessage(content=step1_prompt)])
        print(f"✅ 步骤1完成: {result1.completion[:100]}...")
        
        print("\n🔄 步骤2: 深度分析")
        
        step2_prompt = f"基于分析: {result1.completion[:200]}，请深入分析最佳方向的具体实施方法"
        
        result2 = await llm.ainvoke([UserMessage(content=step2_prompt)])
        print(f"✅ 步骤2完成: {result2.completion[:100]}...")
        
        print("\n🎯 最终结论:")
        print(result2.completion)
        
        print(f"\n📊 Token使用: {result2.usage.total_tokens if result2.usage else 'N/A'}")
        
        print("\n🎉 多步骤分析完成！")
        
    except Exception as e:
        print(f"❌ 演示出错: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(quick_demo())
