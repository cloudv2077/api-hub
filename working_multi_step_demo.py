#!/usr/bin/env python3.11
"""工作版多步骤LLM决策演示"""

import asyncio
import json
import os
from typing import Dict, Any

# 导入MiniMax适配器
from minimax_llm_adapter import MinimaxChatModel
from browser_use.llm.messages import UserMessage, SystemMessage

async def demonstrate_sequential_analysis():
    """演示顺序分析过程"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
    
    print("🚀 多步骤顺序分析演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    # 任务：分析iPhone 15 Pro
    task = "分析iPhone 15 Pro的市场定位和竞争优势"
    
    print(f"🎯 分析任务：{task}")
    
    # 步骤1：初步分析
    print("\n📍 步骤1：初步分析")
    step1_prompt = f"""
请分析iPhone 15 Pro的基本特征和优势，识别需要深入研究的重点领域。
请用中文回答，重点关注：技术规格、用户体验、市场定位等
"""
    
    result1 = await llm.ainvoke([UserMessage(content=step1_prompt)])
    print(f"🤖 AI回复1：{result1.completion}")
    
    # 步骤2：深度技术分析
    print("\n📍 步骤2：深度技术分析")
    step2_prompt = f"""
基于前面的分析：{result1.completion}

请深入分析iPhone 15 Pro的技术规格优势，包括：
1. 处理器性能
2. 摄影系统
3. 显示屏技术
4. 电池续航
5. 与竞品的对比优势
"""
    
    result2 = await llm.ainvoke([UserMessage(content=step2_prompt)])
    print(f"🤖 AI回复2：{result2.completion}")
    
    # 步骤3：市场定位分析
    print("\n📍 步骤3：市场定位分析")
    step3_prompt = f"""
基于前面的分析：
初步分析：{result1.completion}
技术分析：{result2.completion}

请分析iPhone 15 Pro的：
1. 目标用户群体
2. 价格策略
3. 品牌定位
4. 市场竞争力
5. 营销策略建议
"""
    
    result3 = await llm.ainvoke([UserMessage(content=step3_prompt)])
    print(f"🤖 AI回复3：{result3.completion}")
    
    # 步骤4：综合结论
    print("\n📍 步骤4：综合结论")
    step4_prompt = f"""
基于前面三步的全面分析，请给出：
1. iPhone 15 Pro的三大核心竞争优势
2. 面临的主要挑战
3. 市场前景预测
4. 对苹果公司的战略建议
5. 对消费者的购买建议
"""
    
    result4 = await llm.ainvoke([UserMessage(content=step4_prompt)])
    print(f"🤖 AI回复4：{result4.completion}")
    
    # 总结
    print("\n" + "=" * 50)
    print("📊 多步骤分析完成")
    print("=" * 50)
    print(f"🎯 完成任务：{task}")
    print(f"📝 分析步骤：4步深度分析")
    print(f"📊 Token使用：{result1.usage.total_tokens if result1.usage else 'N/A'}")

async def demonstrate_problem_solving():
    """演示问题解决流程"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
        
    print("\n🔄 问题解决流程演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    # 问题场景
    problem = """
情境：在线商城遇到紧急问题
- 销售额下降了30%
- 用户投诉增加了50% 
- 网站速度变慢
- 竞争对手有促销
"""
    
    print(f"🎭 问题场景：{problem}")
    
    # 步骤1：问题诊断
    print("\n🔍 步骤1：问题诊断")
    diagnosis_prompt = "请分析上述问题的可能原因，并确定最紧急需要解决的核心问题"
    
    diagnosis = await llm.ainvoke([UserMessage(content=diagnosis_prompt)])
    print(f"🤖 诊断结果：{diagnosis.completion}")
    
    # 步骤2：制定方案
    print("\n💡 步骤2：制定解决方案")
    solution_prompt = f"""
基于问题诊断：{diagnosis.completion}

请制定分阶段的解决方案：
第一阶段：立即行动（24小时内）
第二阶段：短期措施（1周内）
第三阶段：长期策略（1个月内）
"""
    
    solution = await llm.ainvoke([UserMessage(content=solution_prompt)])
    print(f"🤖 解决方案：{solution.completion}")
    
    # 步骤3：评估效果
    print("\n📈 步骤3：效果评估")
    eval_prompt = f"""
基于解决方案：{solution.completion}

请分析：
1. 预期效果时间
2. 成功概率
3. 潜在风险
4. 需要监控的关键指标
"""
    
    evaluation = await llm.ainvoke([UserMessage(content=eval_prompt)])
    print(f"🤖 效果评估：{evaluation.completion}")

async def demonstrate_creative_ideation():
    """演示创意构思过程"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY")
        return
    
    print("\n🎨 创意构思流程演示")
    print("=" * 50)
    
    llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
    
    task = "为一个环保主题的移动应用设计功能"
    
    print(f"🎯 创意任务：{task}")
    
    # 步骤1：头脑风暴
    print("\n💭 步骤1：头脑风暴")
    brainstorm_prompt = f"""
请为{task}进行头脑风暴，提出：
1. 5个核心功能创意
2. 每个功能的用户价值
3. 技术实现难度评估
4. 市场潜力分析
"""
    
    brainstorm = await llm.ainvoke([UserMessage(content=brainstorm_prompt)])
    print(f"🤖 创意想法：{brainstorm.completion}")
    
    # 步骤2：筛选优化
    print("\n✨ 步骤2：筛选优化")
    filter_prompt = f"""
基于头脑风暴结果：{brainstorm.completion}

请进行筛选和深度优化：
1. 选择3个最有潜力的功能
2. 详细设计产品原型
3. 制定开发路线图
4. 预测可能的挑战
"""
    
    filtered = await llm.ainvoke([UserMessage(content=filter_prompt)])
    print(f"🤖 筛选结果：{filtered.completion}")

if __name__ == "__main__":
    asyncio.run(demonstrate_sequential_analysis())
    asyncio.run(demonstrate_problem_solving()) 
    asyncio.run(demonstrate_creative_ideation())
