#!/usr/bin/env python3.11
"""简化版多步骤LLM决策演示"""

import asyncio
import json
import os
from typing import Dict, Any

# 导入MiniMax适配器
from minimax_llm_adapter import MinimaxChatModel
from browser_use.llm.messages import UserMessage, SystemMessage

async def demonstrate_multi_step_logic():
    """演示多步骤LLM决策逻辑"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
    
    print("🚀 多步骤LLM决策演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    # 任务：分析一个产品
    task = "分析iPhone 15 Pro的市场定位和竞争优势"
    
    # 步骤1：初始化分析
    print("\n📍 步骤1：初始化分析")
    step1_prompt = f"""
任务：{task}

请进行初步分析并识别需要深入研究的关键领域。
返回格式：
{
    "analysis": "你的初步分析",
    "key_areas": ["需要研究的重点1", "重点2", "重点3"],
    "next_step": "你建议的下一步行动"
}
"""
    
    messages = [UserMessage(content=step1_prompt)]
    result1 = await llm.ainvoke(messages)
    print(f"🤖 AI回复1：{result1.completion}")
    
    # 步骤2：深度分析
    print("\n📍 步骤2：深度市场分析") 
    step2_prompt = f"""
基于第一步的分析：{result1.completion}

请深入分析iPhone 15 Pro的：
1. 技术规格优势
2. 竞争对手分析  
3. 市场定位策略
4. 目标用户群体

返回格式：
{
    "technical_advantages": ["技术优势1", "优势2"],
    "competitor_analysis": "竞争对手对比",
    "positioning_strategy": "市场定位策略",
    "target_users": ["用户群体1", "用户群体2"],
    "recommendations": "营销建议"
}
"""
    
    messages = [UserMessage(content=step2_prompt)]
    result2 = await llm.ainvoke(messages)
    print(f"🤖 AI回复2：{result2.completion}")
    
    # 步骤3：综合评估
    print("\n📍 步骤3：综合评估与结论")
    step3_prompt = f"""
基于前面的分析：
初步分析：{result1.completion}
深度分析：{result2.completion}

请综合评估并给出最终结论：
{
    "strengths": ["主要优势1", "优势2", "优势3"],
    "challenges": ["面临挑战1", "挑战2"],
    "market_outlook": "市场前景预测",
    "final_recommendation": "最终建议",
    "confidence_score": "分析置信度(1-10)"
}
"""
    
    messages = [UserMessage(content=step3_prompt)]
    result3 = await llm.ainvoke(messages)
    print(f"🤖 AI回复3：{result3.completion}")
    
    # 总结
    print("\n" + "=" * 50)
    print("📊 多步骤分析总结")
    print("=" * 50)
    print(f"🎯 任务：{task}")
    print(f"📝 分析步骤：3步")
    print(f"🤖 AI输出：{result3.completion[:200]}...")

async def demonstrate_dynamic_decision():
    """演示动态决策过程"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
        
    print("\n🔄 动态决策过程演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    # 模拟一个复杂的推理过程
    scenario = """
情境：你在运营一个在线商城，遇到了以下问题：
1. 最近3天销售额下降了30%
2. 用户投诉数量增加了50%
3. 网站加载速度变慢了
4. 竞争对手推出了新的促销活动

作为AI助手，你需要制定应对策略。
"""

    print(f"🎭 场景：{scenario}")
    
    # AI分析当前状况
    print("\n🧠 步骤1：问题诊断")
    diagnosis_prompt = f"""
{scenario}

请诊断问题的根本原因，返回JSON：
{
    "problem_cause": "最可能的问题原因",
    "urgency_level": "紧急程度(1-10)",
    "affected_systems": ["受影响的系统1", "系统2"],
    "data_needed": ["需要收集的数据1", "数据2"]
}
"""
    
    result = await llm.ainvoke([UserMessage(content=diagnosis_prompt)])
    print(f"🤖 诊断结果：{result.completion}")
    
    # AI制定解决方案
    print("\n💡 步骤2：解决方案制定")
    solution_prompt = f"""
基于诊断结果：{result.completion}

请制定分阶段的解决方案：
{
    "immediate_actions": ["立即行动1", "行动2"],
    "short_term_plan": "短期计划",
    "long_term_strategy": "长期策略",
    "success_metrics": ["成功指标1", "指标2"],
    "resource_requirements": "资源需求"
}
"""
    
    result2 = await llm.ainvoke([UserMessage(content=solution_prompt)])
    print(f"🤖 解决方案：{result2.completion}")

if __name__ == "__main__":
    asyncio.run(demonstrate_multi_step_logic())
    asyncio.run(demonstrate_dynamic_decision())
