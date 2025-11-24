#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
混合智能装饰器 - 增强版
=====================

完美结合真实AI代码生成和智能任务分解
新增：显示AI生成的函数代码内容
"""

from functools import wraps
import re
from minimax_decorator import MiniMaxCodeGenerator
from enhanced_smart_decompose import smart_decompose

class ComplexityAnalyzer:
    """任务复杂度分析器"""
    
    # 复杂度权重配置
    COMPLEX_OPERATIONS = {
        '分析': 2, '统计': 2, '生成': 2, '计算': 2, '转换': 2,
        '提取': 2, '处理': 2, '识别': 2, '检测': 2, '优化': 2,
        '然后': 2, '接着': 2, '并且': 2, '同时': 2, '以及': 2
    }
    
    SIMPLE_OPERATIONS = {
        '获取': -1, '查询': -1, '显示': -1, '输出': -1, '返回': -1
    }
    
    def analyze_complexity(self, task_description):
        """分析任务复杂度"""
        score = 0
        reasons = []
        
        # 长度分析
        if len(task_description) > 30:
            score += 1
            reasons.append(f"长度超过30字符")
        
        # 子句分析（通过标点符号）
        clause_markers = ['，', '。', '；', '、', ',', '.', ';']
        clause_count = sum(task_description.count(marker) for marker in clause_markers)
        if clause_count > 0:
            score += clause_count * 2
            reasons.append(f"包含{clause_count + 1}个子句")
        
        # 复杂操作词分析
        for operation, weight in self.COMPLEX_OPERATIONS.items():
            if operation in task_description:
                score += weight
                reasons.append(f"复杂操作: {operation}")
        
        # 简单操作词分析
        for operation, weight in self.SIMPLE_OPERATIONS.items():
            if operation in task_description:
                score += weight
                reasons.append(f"简单操作: {operation}")
        
        # 动词计数
        action_words = ['计算', '生成', '分析', '处理', '转换', '提取', '统计', '优化', '检测', '识别']
        action_count = sum(1 for word in action_words if word in task_description)
        if action_count > 2:
            score += action_count - 2
            reasons.append(f"包含{action_count}个动作")
        
        return score, reasons

def hybrid_smart(task_description, complexity_threshold=3, use_ai=True):
    """
    混合智能装饰器
    
    Args:
        task_description: 任务描述
        complexity_threshold: 复杂度阈值，超过则使用分解模式
        use_ai: 是否启用AI代码生成
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("🚀 混合智能装饰器")
            print(f"📝 函数: {func.__name__}")
            print(f"📋 任务: {task_description}")
            print("="*50)
            
            # 分析任务复杂度
            analyzer = ComplexityAnalyzer()
            complexity_score, reasons = analyzer.analyze_complexity(task_description)
            
            print(f"🧮 复杂度分析: 评分 {complexity_score}, 阈值 {complexity_threshold}")
            print(f"📊 判断依据: {'; '.join(reasons) if reasons else '无特殊标记'}")
            
            # 根据复杂度选择执行模式
            if complexity_score < complexity_threshold and use_ai:
                print("🤖 简单任务 -> AI代码生成模式")
                print()
                return execute_ai_mode(task_description, func)
            else:
                print("🔄 复杂任务 -> 智能分解模式")
                print()
                return execute_decomposition_mode(task_description, func)
        
        return wrapper
    return decorator

def execute_ai_mode(task_description, func):
    """执行AI代码生成模式"""
    print("✨ AI代码生成模式")
    print("-" * 30)
    
    try:
        generator = MiniMaxCodeGenerator()
        print("🔄 调用AI生成器...")
        
        # 获取AI生成的代码和结果
        result, generated_code = generator.generate_code_with_source(task_description)
        
        print(f"✅ AI生成完成: {result}")
        
        # 🌟 新增：显示生成的函数代码
        if generated_code:
            print(f"\n📝 生成的函数代码:")
            print("```python")
            print(generated_code)
            print("```")
        
        return {
            'execution_mode': 'ai_generated',
            'result': result,
            'generated_code': generated_code,  # 新增代码字段
            'task_description': task_description,
            'complexity_score': 'low'
        }
        
    except Exception as e:
        print(f"❌ AI生成失败: {e}")
        print("🔄 切换到智能分解模式...")
        return execute_decomposition_mode(task_description, func)

def execute_decomposition_mode(task_description, func):
    """执行智能分解模式"""
    print("🔄 智能分解模式")
    print("-" * 30)
    
    try:
        # 使用智能分解器
        result = smart_decompose(task_description)
        
        return {
            'execution_mode': 'smart_decomposition',
            'steps': result.get('steps', []),
            'final_result': result.get('final_result', '执行完成'),
            'task_description': task_description,
            'complexity_score': 'high'
        }
        
    except Exception as e:
        print(f"❌ 智能分解失败: {e}")
        return {
            'execution_mode': 'error',
            'error': str(e),
            'task_description': task_description
        }

if __name__ == "__main__":
    # 测试示例
    print("🧪 混合智能装饰器测试")
    print("="*50)
    
    @hybrid_smart("计算10的阶乘", use_ai=True)
    def test_factorial():
        pass
    
    @hybrid_smart("分析用户数据，统计特征，然后生成报告")
    def test_complex():
        pass
    
    print("🧪 【测试AI生成】")
    result1 = test_factorial()
    
    print(f"\n🧪 【测试智能分解】")  
    result2 = test_complex()
    
    print(f"\n📊 测试完成")
