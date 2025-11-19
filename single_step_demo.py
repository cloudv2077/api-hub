#!/usr/bin/env python3.11
"""单步LLM决策演示"""

import asyncio
import os
from minimax_llm_adapter import MinimaxChatModel
from browser_use.llm.messages import UserMessage

async def show_multi_step_concept():
    """展示多步骤决策概念"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
    
    print("🎯 LLM多步骤决策概念演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    # 演示步骤1：分析问题
    print("\n🧠 步骤1：问题分析")
    print("🤖 让AI分析：如何提高在线商城的用户留存率？")
    
    analysis_prompt = """
请分析在线商城用户留存率低的问题：
1. 识别3个主要原因
2. 对每个原因给出可能的影响
3. 推荐2个立即可实施的改进措施
4. 预测效果和实施难度
"""

    result1 = await llm.ainvoke([UserMessage(content=analysis_prompt)])
    print(f"📊 AI分析结果：")
    print(f"{result1.completion}")
    print(f"📈 Token使用：{result1.usage.total_tokens if result1.usage else 'N/A'}")
    
    # 演示步骤2：制定策略
    print("\n💡 步骤2：策略制定")
    print("🤖 基于分析结果，让AI制定具体实施方案")
    
    strategy_prompt = f"""
基于前面的分析：
{result1.completion}

请制定详细的实施策略：
1. 第一周要做什么
2. 需要的资源和预算
3. 如何衡量成功
4. 风险控制措施
"""

    result2 = await llm.ainvoke([UserMessage(content=strategy_prompt)])
    print(f"📋 AI策略方案：")
    print(f"{result2.completion}")
    print(f"📈 Token使用：{result2.usage.total_tokens if result2.usage else 'N/A'}")

async def demonstrate_reasoning_flow():
    """演示推理流程"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
    
    print("\n🔄 推理流程演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    # 复杂推理问题
    reasoning_task = """
电商公司要考虑以下几个因素：
- 用户满意度下降15%
- 竞争对手价格更低
- 运营成本上升20%
- 新用户获取困难

请帮公司制定应对策略。
"""
    
    print(f"🎭 推理任务：{reasoning_task}")
    
    # 阶段1：信息整合
    print("\n📋 阶段1：信息整合分析")
    analysis_prompt = "请分析上述问题，识别最紧急需要解决的核心问题，并分析各因素之间的关联性"
    
    stage1 = await llm.ainvoke([UserMessage(content=analysis_prompt)])
    print(f"🧠 AI分析：{stage1.completion}")
    
    # 阶段2：策略制定
    print("\n🎯 阶段2：策略制定")
    strategy_prompt = f"基于问题分析：{stage1.completion}，请制定分阶段解决方案，包括短期和长期策略"
    
    stage2 = await llm.ainvoke([UserMessage(content=strategy_prompt)])
    print(f"💡 AI策略：{stage2.completion}")

if __name__ == "__main__":
    asyncio.run(show_multi_step_concept())
    asyncio.run(demonstrate_reasoning_flow())
