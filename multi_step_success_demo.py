#!/usr/bin/env python3.11
"""成功版多步骤LLM决策演示"""

import asyncio
import json
import os
from typing import Dict, Any, List
from minimax_llm_adapter import MinimaxChatModel
from browser_use.llm.messages import UserMessage

class StepByStepDecisionMaker:
    """多步骤决策制作器"""
    
    def __init__(self):
        if not os.getenv('MINIMAX_API_KEY'):
            raise ValueError("请设置MINIMAX_API_KEY环境变量")
        
        self.llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
        self.decision_steps = []
        
    async def make_multistep_decision(self, task: str, max_steps: int = 3) -> Dict[str, Any]:
        """执行多步骤决策"""
        
        print(f"🎯 多步骤决策任务: {task}")
        print("=" * 60)
        
        # 存储每一步的结果
        step_results = []
        current_context = f"初始任务: {task}"
        
        for step in range(max_steps):
            print(f"\n🔄 步骤 {step + 1}/{max_steps}")
            
            # 根据步骤数构建不同的提示
            if step == 0:
                prompt = f"""
分析任务: {task}

请进行初步分析，识别关键问题点。你需要:
1. 列出3-5个需要重点关注的方向
2. 对每个方向提供简要分析
3. 指出哪个方向最需要深入研究
"""
            elif step == 1:
                if len(step_results) > 0:
                    prompt = f"""
基于上一步分析: {step_results[0]['analysis']}

现在进行深度分析:
1. 对最有价值的方向进行深入分析
2. 提供具体的数据或案例支持
3. 分析潜在的解决方案
4. 评估实施的难度和风险
"""
                else:
                    prompt = "请进行深度分析，提供详细的解决方案"
            else:  # step >= 2
                analysis_history = " ".join([s['analysis'] for s in step_results])
                prompt = f"""
基于所有分析: {analysis_history}

请提供最终结论和行动建议:
1. 总结最优解决方案
2. 制定具体的实施计划
3. 提供风险控制措施
4. 预测成功概率和关键指标
"""
            
            print(f"💭 思考中...")
            
            try:
                # 调用LLM
                result = await self.llm.ainvoke([UserMessage(content=prompt)])
                
                step_data = {
                    "step_number": step + 1,
                    "prompt": prompt,
                    "analysis": result.completion,
                    "token_usage": result.usage.total_tokens if result.usage else 0
                }
                
                step_results.append(step_data)
                
                print(f"✅ 步骤 {step + 1} 完成")
                print(f"📊 分析要点: {result.completion[:150]}...")
                
                # 如果是最后一步，可以选择结束
                if step == max_steps - 1:
                    break
                    
            except Exception as e:
                print(f"❌ 步骤 {step + 1} 出错: {e}")
                break
        
        # 返回完整结果
        return {
            "original_task": task,
            "total_steps": len(step_results),
            "steps": step_results,
            "final_conclusion": step_results[-1]['analysis'] if step_results else "无结果",
            "total_tokens_used": sum(s['token_usage'] for s in step_results)
        }

async def demo_business_analysis():
    """商业分析演示"""
    
    try:
        decision_maker = StepByStepDecisionMaker()
        
        task = "分析在线教育平台的用户流失问题，并制定改进策略"
        
        print("🚀 开始商业分析多步骤决策")
        print("=" * 60)
        
        result = await decision_maker.make_multistep_decision(task, max_steps=3)
        
        # 显示详细结果
        print("\n" + "=" * 60)
        print("📊 多步骤分析结果总结")
        print("=" * 60)
        
        print(f"🎯 原始任务: {result['original_task']}")
        print(f"📝 执行步骤: {result['total_steps']} 步")
        print(f"📈 Token使用: {result['total_tokens_used']}")
        
        print(f"\n📋 步骤详情:")
        for step in result['steps']:
            print(f"\n🔍 步骤 {step['step_number']}:")
            print(f"   分析内容: {step['analysis'][:200]}...")
            print(f"   Token消耗: {step['token_usage']}")
        
        print(f"\n🎉 最终结论:")
        print(result['final_conclusion'])
        
        return result
        
    except Exception as e:
        print(f"❌ 演示失败: {e}")
        return None

async def demo_strategy_planning():
    """策略规划演示"""
    
    try:
        decision_maker = StepByStepDecisionMaker()
        
        task = "为一家初创科技公司制定市场进入策略"
        
        print("\n🚀 开始策略规划多步骤决策")
        print("=" * 60)
        
        result = await decision_maker.make_multistep_decision(task, max_steps=3)
        
        print("\n📊 策略规划结果:")
        print(f"🎯 任务: {result['original_task']}")
        print(f"📝 步骤: {result['total_steps']}")
        
        # 显示各步骤的核心洞察
        for i, step in enumerate(result['steps'], 1):
            print(f"\n💡 步骤 {i} 洞察:")
            # 提取关键信息
            lines = step['analysis'].split('\n')
            key_lines = [line for line in lines if any(keyword in line for keyword in ['关键', '重要', '建议', '策略', '优势'])]
            for line in key_lines[:3]:  # 只显示前3个关键点
                print(f"   • {line.strip()}")
        
        return result
        
    except Exception as e:
        print(f"❌ 策略规划失败: {e}")
        return None

if __name__ == "__main__":
    print("🎯 多步骤LLM决策演示")
    print("这个演示将展示AI如何分步骤分析和解决问题")
    print()
    
    # 运行两个演示
    demo1 = asyncio.run(demo_business_analysis())
    demo2 = asyncio.run(demo_strategy_planning())
    
    if demo1 and demo2:
        print("\n" + "🎉" * 20)
        print("✅ 多步骤LLM决策演示成功完成！")
        print("展示了AI如何:")
        print("1️⃣ 系统性分析复杂问题")
        print("2️⃣ 逐步深入研究各个层面") 
        print("3️⃣ 基于前面的结果优化后续步骤")
        print("4️⃣ 提供最终的综合解决方案")
        print("🎉" * 20)
    else:
        print("❌ 演示过程中遇到问题")
