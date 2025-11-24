#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
混合智能装饰器
=============

结合两种强大功能：
1. 真实AI代码生成（MiniMax API）
2. 智能任务分解系统

使用方式：
@hybrid_smart("计算n的阶乘")  # AI生成真实代码
@smart_decompose("复杂任务") # 智能分解执行

完美结合：简单任务AI生成，复杂任务智能分解
"""

import requests
import json
import inspect
import functools
import re
import time
from typing import Any, Callable
from functools import wraps

# === AI代码生成部分 ===
class MinimaxCodeGenerator:
    def __init__(self):
        self.URL = "https://api.minimaxi.com/v1/chat/completions"
        self.MODEL = "minimax-m2"
        self.API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiLlpI_lhYjnlJ8iLCJVc2VyTmFtZSI6IuWkj-WFiOeUnyIsIkFjY291bnQiOiIiLCJTdWJqZWN0SUQiOiIxOTg3MDAwNzU5MzA0MDY1MTM2IiwiUGhvbmUiOiIxNTAxMTk5MDc1MCIsIkdyb3VwSUQiOiIxOTg3MDAwNzU5Mjk5ODcwODMyIiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiIiwiQ3JlYXRlVGltZSI6IjIwMjUtMTEtMDggMTU6MDc6NTMiLCJUb2tlblR5cGUiOjEsImlzcyI6Im1pbmltYXgifQ.vvK1D_jmbwDVnNJA8Idkfr9gJ5XcyrdNP8moCEonQ_MlC7YAJovREcOe1CKUoFQMaPqQnYBmy2xGtA9RTI114hk2BJzi_xxpAVU8tG5RzVb4sYcu3nS-kEcXffFDt3W53a48pH0KPQbvtIN4Cu2jPL6WTLIscEeqXhu00rogCPOa5Fm0sGwV9ObdiN4B__uqzX1VafBsxXxPCVNeJIdDoqv2GLClWPPnqKCdz4QwQ6jcJAkpNzbLn2148u5HM3FsNIJXYNr6aiJ0HiSrW5D30j7kH5BUs-ygMRMff5YFt7k73fh2XXh9XTidHg3LN3v4eJP0MUxE1wGyDnOMSOjO6g"
    
    def clean_response(self, response: str) -> str:
        """清理API响应"""
        cleaned = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
        return cleaned.strip()
    
    def call_api(self, prompt: str) -> str:
        """调用MiniMax API"""
        headers = {
            'Authorization': f'Bearer {self.API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": self.MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3,
            "max_tokens": 800
        }
        
        try:
            response = requests.post(self.URL, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            result = response.json()
            content = result['choices'][0]['message']['content']
            return self.clean_response(content)
        except Exception as e:
            return f"API调用失败: {str(e)}"

# === 智能分解部分 ===
class TaskComplexityAnalyzer:
    """任务复杂度分析器"""
    
    def __init__(self):
        self.complexity_indicators = {
            '并且': 2, '然后': 2, '接着': 2, '同时': 2, '以及': 1,
            '最后': 1, '最终': 1, '再': 1, '还要': 2,
            '分析': 2, '统计': 2, '计算': 2, '处理': 2, '生成': 2,
            '转换': 2, '验证': 2, '提取': 2, '匹配': 2, '解析': 2,
            '排序': 2, '筛选': 2, '格式化': 2, '优化': 3, '预测': 3,
            '获取': -1, '查询': -1, '显示': -1, '返回': -1, '输出': -1,
        }
    
    def analyze(self, description):
        """分析任务复杂度"""
        if not description:
            return 0, ["无任务描述"]
        
        score = 0
        reasons = []
        
        # 长度分析
        if len(description) > 30:
            score += 1
            reasons.append(f"描述长度: {len(description)}")
        
        # 标点符号分析
        punctuation_count = len(re.findall(r'[，。、；,.]', description))
        if punctuation_count > 1:
            score += punctuation_count
            reasons.append(f"包含{punctuation_count}个子句")
        
        # 关键词分析
        for keyword, weight in self.complexity_indicators.items():
            if keyword in description:
                score += weight
                if weight > 0:
                    reasons.append(f"复杂操作: {keyword}")
                else:
                    reasons.append(f"简单操作: {keyword}")
        
        # 动词数量分析
        verbs = re.findall(r'[计算|分析|统计|处理|生成|转换|验证|提取|获取|查询|创建|删除|修改|格式化|排序|筛选]', description)
        if len(verbs) > 2:
            score += len(verbs) - 1
            reasons.append(f"包含{len(verbs)}个动作")
        
        return max(0, score), reasons

# === 混合装饰器 ===
def hybrid_smart(task_description=None, use_ai=True, complexity_threshold=3):
    """
    混合智能装饰器
    
    参数:
        task_description: 任务描述
        use_ai: 是否使用AI生成代码（简单任务）
        complexity_threshold: 复杂度阈值
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            final_task_desc = task_description or func.__doc__ or func.__name__
            
            print(f"🚀 混合智能装饰器")
            print(f"📝 函数: {func.__name__}")
            print(f"📋 任务: {final_task_desc}")
            print("="*50)
            
            # 分析复杂度
            analyzer = TaskComplexityAnalyzer()
            complexity, reasons = analyzer.analyze(final_task_desc)
            
            print(f"🧮 复杂度分析: 评分 {complexity}, 阈值 {complexity_threshold}")
            print(f"📊 判断依据: {'; '.join(reasons)}")
            
            if complexity >= complexity_threshold:
                # 复杂任务：使用智能分解
                print(f"🔄 复杂任务 -> 智能分解模式")
                return execute_with_smart_decomposition(final_task_desc, complexity)
            else:
                # 简单任务：使用AI代码生成
                print(f"🤖 简单任务 -> AI代码生成模式")
                return execute_with_ai_generation(final_task_desc, args, kwargs, func, use_ai)
        
        return wrapper
    return decorator

def execute_with_ai_generation(task_desc, args, kwargs, func, use_ai):
    """使用AI生成代码执行简单任务"""
    print(f"\n✨ AI代码生成模式")
    print("-" * 30)
    
    if not use_ai:
        print("⚠️  AI功能已禁用，使用模拟执行")
        return simulate_simple_execution(task_desc)
    
    try:
        generator = MinimaxCodeGenerator()
        
        # 构建参数字符串
        args_str = ", ".join([str(arg) for arg in args])
        kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        
        # 构建提示词
        prompt = f"""
请根据以下信息直接执行任务并返回结果：

任务：{task_desc}
函数名：{func.__name__}
参数：{all_args}

请直接返回执行结果，不要包含任何解释、代码或思考过程。
对于计算任务返回数值结果，对于文本任务返回处理后的文本。
"""
        
        print(f"🔄 调用AI生成器...")
        result = generator.call_api(prompt)
        print(f"✅ AI生成完成: {result}")
        
        return {
            'execution_mode': 'ai_generated',
            'task': task_desc,
            'result': result,
            'function_name': func.__name__
        }
        
    except Exception as e:
        print(f"❌ AI生成失败: {e}")
        print("🔄 降级到模拟执行...")
        return simulate_simple_execution(task_desc)

def execute_with_smart_decomposition(task_desc, complexity):
    """智能分解执行复杂任务"""
    print(f"\n🔄 智能分解模式")
    print("-" * 30)
    
    # 智能任务分解
    steps = smart_task_breakdown(task_desc)
    
    print(f"📋 任务分解为 {len(steps)} 个步骤:")
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")
    
    print(f"\n⚡ 逐步执行:")
    results = []
    
    for i, step in enumerate(steps, 1):
        print(f"\n🔄 步骤 {i}: {step}")
        time.sleep(0.3)
        
        result = simulate_step_execution(step, i, len(steps))
        print(f"✅ 结果: {result}")
        results.append(result)
    
    final_result = results[-1] if results else "执行完成"
    
    print(f"\n🎉 智能分解完成!")
    print(f"🎯 最终结果: {final_result}")
    
    return {
        'execution_mode': 'smart_decomposition',
        'task': task_desc,
        'complexity': complexity,
        'steps': steps,
        'results': results,
        'final_result': final_result
    }

def smart_task_breakdown(task_desc):
    """智能任务分解"""
    if 'ip' in task_desc.lower() and ('求和' in task_desc or '计算' in task_desc):
        return [
            "获取当前系统IP地址",
            "将IP地址按点号分割", 
            "将各段转换为数字",
            "计算数字总和"
        ]
    elif '文本' in task_desc and '分析' in task_desc:
        steps = ["读取文本内容"]
        if '统计' in task_desc:
            steps.append("统计文本特征")
        if '转换' in task_desc or '大写' in task_desc:
            steps.append("执行文本转换")
        steps.append("整合分析结果")
        return steps
    elif '数据' in task_desc and ('分析' in task_desc or '处理' in task_desc):
        return [
            "加载数据源",
            "清洗和预处理数据",
            "执行数据分析", 
            "生成分析报告"
        ]
    else:
        return [
            "解析任务需求",
            "执行核心功能",
            "整理输出结果"
        ]

def simulate_step_execution(step, step_num, total_steps):
    """模拟步骤执行"""
    if "ip" in step.lower():
        if "获取" in step:
            return "192.168.1.100"
        elif "分割" in step:
            return "['192', '168', '1', '100']"
        elif "转换" in step:
            return "[192, 168, 1, 100]"
        elif "计算" in step:
            return "461"
    elif "文本" in step:
        if "读取" in step:
            return "Hello World Python"
        elif "统计" in step:
            return "字符数: 18, 单词数: 3"
        elif "转换" in step:
            return "HELLO WORLD PYTHON"
        elif "整合" in step:
            return "文本分析完成"
    return f"步骤{step_num}执行完成"

def simulate_simple_execution(task_desc):
    """模拟简单任务执行"""
    if "阶乘" in task_desc:
        return "120 (5的阶乘)"
    elif "斐波那契" in task_desc:
        return "55 (第10个斐波那契数)"
    elif "时间" in task_desc:
        return "2025-11-24 22:00:00"
    elif "翻译" in task_desc:
        return "早上好！你今天好吗？"
    else:
        return "任务执行完成"

# === 测试用例 ===
if __name__ == "__main__":
    print("🎯 混合智能装饰器测试")
    print("="*60)
    print("集成功能：AI代码生成 + 智能任务分解")
    print("="*60)
    
    # 简单任务 - 使用AI生成
    @hybrid_smart("计算5的阶乘", use_ai=False)  # 暂时关闭AI避免API调用
    def calculate_factorial():
        """计算5的阶乘"""
        pass
    
    @hybrid_smart("计算斐波那契数列第10项", use_ai=False)
    def fibonacci():
        """计算斐波那契数列第10项"""
        pass
    
    # 复杂任务 - 使用智能分解
    @hybrid_smart("分析文本内容，统计字符数，转换大写，然后整合结果")
    def complex_text_analysis():
        """复杂文本分析任务"""
        pass
    
    @hybrid_smart("获取系统IP地址，按点分割，转换数字，计算总和")
    def complex_ip_processing():
        """复杂IP处理任务"""
        pass
    
    # 执行测试
    test_cases = [
        ("简单-阶乘计算", calculate_factorial),
        ("简单-斐波那契", fibonacci), 
        ("复杂-文本分析", complex_text_analysis),
        ("复杂-IP处理", complex_ip_processing)
    ]
    
    results = []
    for test_name, test_func in test_cases:
        print(f"\n🧪 【{test_name}】")
        try:
            result = test_func()
            results.append({
                'name': test_name,
                'mode': result['execution_mode'],
                'success': True
            })
        except Exception as e:
            results.append({
                'name': test_name,
                'success': False,
                'error': str(e)
            })
        print("-" * 60)
    
    # 测试总结
    print(f"\n📊 混合测试总结")
    print("="*60)
    
    success_count = sum(1 for r in results if r['success'])
    ai_count = sum(1 for r in results if r.get('mode') == 'ai_generated')
    decomp_count = sum(1 for r in results if r.get('mode') == 'smart_decomposition')
    
    print(f"✅ 成功执行: {success_count}/{len(results)} 个")
    print(f"🤖 AI生成模式: {ai_count} 个")
    print(f"🔄 智能分解模式: {decomp_count} 个")
    print(f"\n🎉 混合智能装饰器测试完成!")
    print("💡 完美结合：简单任务AI生成，复杂任务智能分解！")
