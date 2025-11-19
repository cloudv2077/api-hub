#!/usr/bin/env python3.11
"""多步骤LLM自动判断示例"""

import asyncio
import json
import os
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv

# 导入我们的MiniMax适配器
from minimax_llm_adapter import MinimaxChatModel
from browser_use.llm.messages import UserMessage, SystemMessage, AssistantMessage

class MultiStepLLM:
    """多步骤LLM决策系统"""
    
    def __init__(self):
        self.llm = MinimaxChatModel(api_key=os.getenv('MINIMAX_API_KEY'))
        self.history = []
        self.current_state = {
            "context": "初始状态",
            "data": {},
            "completed_steps": []
        }
        
    async def think_and_decide(self, task: str) -> Dict[str, Any]:
        """核心决策方法：让AI分析当前状态并决定下一步"""
        
        # 构建决策提示
        decision_prompt = f"""
你是一个智能任务执行助手。当前任务: {task}

当前状态: {json.dumps(self.current_state, ensure_ascii=False, indent=2)}

你的历史操作: {json.dumps(self.history, ensure_ascii=False, indent=2)}

请分析当前状态，思考下一步应该做什么。返回JSON格式的决策:

{{
    "thinking": "你的思考过程",
    "action_type": "search_web | analyze_data | extract_content | complete_task | continue",
    "action_details": {{
        "description": "具体要做什么",
        "target": "目标网址或数据",
        "parameters": {{}}
    }},
    "expected_result": "你期望的结果",
    "success_criteria": "成功的判断标准"
}}
"""

        messages = [
            SystemMessage(content="你是一个专业的AI任务执行助手，善于分析问题并制定执行计划。"),
            UserMessage(content=decision_prompt)
        ]
        
        result = await self.llm.ainvoke(messages)
        
        # 解析AI的决策
        try:
            # 提取JSON部分
            content = result.completion
            
            # 尝试解析JSON
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                decision = json.loads(json_match.group())
                return decision
            else:
                # 如果无法解析JSON，返回默认决策
                return {
                    "thinking": "无法解析AI决策，使用默认策略",
                    "action_type": "continue",
                    "action_details": {"description": "继续任务"},
                    "expected_result": "推进任务进展",
                    "success_criteria": "任务有进展"
                }
        except Exception as e:
            print(f"⚠️ 决策解析错误: {e}")
            return {
                "thinking": f"决策解析失败: {e}",
                "action_type": "continue", 
                "action_details": {"description": "继续任务"},
                "expected_result": "推进任务进展",
                "success_criteria": "任务有进展"
            }

    async def execute_action(self, decision: Dict[str, Any]) -> Dict[str, Any]:
        """执行AI决定的行动"""
        
        action_type = decision.get('action_type', 'continue')
        action_details = decision.get('action_details', {})
        expected_result = decision.get('expected_result', '')
        
        print(f"🎯 执行行动: {action_type}")
        print(f"📋 行动描述: {action_details.get('description', '无描述')}")
        
        # 模拟各种行动类型
        if action_type == "search_web":
            result = await self._search_web(action_details)
        elif action_type == "analyze_data":
            result = await self._analyze_data(action_details)
        elif action_type == "extract_content":
            result = await self._extract_content(action_details)
        elif action_type == "complete_task":
            result = await self._complete_task(action_details)
        else:
            result = {"status": "completed", "message": "继续下一步"}
        
        # 更新状态
        self.history.append({
            "step": len(self.history) + 1,
            "decision": decision,
            "result": result,
            "timestamp": "now"
        })
        
        self.current_state["completed_steps"].append(action_type)
        
        print(f"✅ 执行结果: {result}")
        return result

    async def _search_web(self, details: Dict[str, Any]) -> Dict[str, Any]:
        """模拟网络搜索"""
        target = details.get('target', '通用搜索')
        return {
            "status": "success",
            "type": "web_search",
            "data": f"搜索到关于'{target}'的相关信息",
            "insights": f"网络搜索确认'{target}'是一个有效的查询目标"
        }

    async def _analyze_data(self, details: Dict[str, Any]) -> Dict[str, Any]:
        """模拟数据分析"""
        target_data = details.get('target', '当前数据')
        return {
            "status": "success", 
            "type": "data_analysis",
            "data": f"分析了{target_data}",
            "insights": "数据分析发现关键信息，需要进一步处理"
        }

    async def _extract_content(self, details: Dict[str, Any]) -> Dict[str, Any]:
        """模拟内容提取"""
        target = details.get('target', '目标页面')
        return {
            "status": "success",
            "type": "content_extraction", 
            "data": f"从{target}提取了重要内容",
            "insights": "内容提取成功，获得了所需信息"
        }

    async def _complete_task(self, details: Dict[str, Any]) -> Dict[str, Any]:
        """完成任务"""
        return {
            "status": "task_completed",
            "type": "task_finish",
            "data": "任务完成",
            "final_result": "所有步骤执行完毕"
        }

    async def run_multi_step_task(self, task: str, max_steps: int = 10) -> Dict[str, Any]:
        """运行多步骤任务"""
        
        print(f"🚀 开始多步骤任务: {task}")
        print(f"📊 最大步骤数: {max_steps}")
        print("-" * 50)
        
        for step in range(max_steps):
            print(f"\n🔄 步骤 {step + 1}/{max_steps}")
            
            # AI分析并决定下一步
            decision = await self.think_and_decide(task)
            print(f"💭 AI思考: {decision.get('thinking', '无思考')}")
            
            # 执行决定
            result = await self.execute_action(decision)
            
            # 检查是否完成
            if decision.get('action_type') == 'complete_task' or result.get('status') == 'task_completed':
                print(f"\n🎉 任务完成！")
                break
                
            # 检查是否需要更多步骤
            if len(self.history) >= 3:  # 如果已经执行了3步，尝试完成
                print("\n🤔 AI评估是否需要更多步骤...")
                completion_check = await self.check_task_completion(task)
                if completion_check.get('should_complete', False):
                    print("✅ AI决定任务可以结束")
                    break
        
        return {
            "task": task,
            "total_steps": len(self.history),
            "history": self.history,
            "final_state": self.current_state,
            "completed": True
        }

    async def check_task_completion(self, task: str) -> Dict[str, Any]:
        """让AI检查任务是否完成"""
        completion_prompt = f"""
当前任务: {task}
已完成步骤: {len(self.history)}
执行历史: {json.dumps(self.history[-3:], ensure_ascii=False, indent=2)}

请判断任务是否已经完成？返回JSON:
{{
    "should_complete": true/false,
    "reason": "完成原因或继续的理由"
}}
"""

        messages = [
            UserMessage(content=completion_prompt)
        ]
        
        result = await self.llm.ainvoke(messages)
        
        try:
            import re
            json_match = re.search(r'\{.*\}', result.completion, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
            
        return {"should_complete": False, "reason": "需要更多步骤"}

# 演示函数
async def demo_multi_step_task():
    """演示多步骤任务"""
    
    if not os.getenv('MINIMAX_API_KEY'):
        print("❌ 请设置MINIMAX_API_KEY环境变量")
        return
    
    # 创建多步骤LLM系统
    agent = MultiStepLLM()
    
    # 演示任务
    demo_tasks = [
        "分析一个电商网站的商品价格趋势",
        "研究AI技术的发展现状和未来方向",
        "收集特定行业的竞争信息"
    ]
    
    for i, task in enumerate(demo_tasks, 1):
        print(f"\n{'='*60}")
        print(f"🎯 演示任务 {i}: {task}")
        print(f"{'='*60}")
        
        result = await agent.run_multi_step_task(task, max_steps=5)
        
        print(f"\n📊 最终结果:")
        print(f"   任务: {result['task']}")
        print(f"   总步骤: {result['total_steps']}")
        print(f"   完成状态: {'✅' if result['completed'] else '❌'}")
        
        # 显示执行历史
        print(f"\n📋 执行历史:")
        for step in result['history']:
            print(f"   步骤 {step['step']}: {step['decision']['action_type']} - {step['result'].get('data', 'N/A')}")
        
        # 重置状态以便下一个任务
        agent.history = []
        agent.current_state = {
            "context": "初始状态",
            "data": {},
            "completed_steps": []
        }

if __name__ == "__main__":
    asyncio.run(demo_multi_step_task())
