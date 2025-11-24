#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版智能分解装饰器
==================

支持直接在装饰器中写任务描述：
@smart_decompose("把当前的ip地址进行求和，根据.进行分开")
def process_ip():
    pass
"""

import re
import time
from functools import wraps

class TaskComplexityAnalyzer:
    """任务复杂度分析器"""
    
    def __init__(self):
        self.complexity_indicators = {
            # 连接词（表示多步骤）
            '并且': 2, '然后': 2, '接着': 2, '同时': 2, '以及': 1,
            '最后': 1, '最终': 1, '再': 1, '还要': 2,
            
            # 复杂操作词
            '分析': 2, '统计': 2, '计算': 2, '处理': 2, '生成': 2,
            '转换': 2, '验证': 2, '提取': 2, '匹配': 2, '解析': 2,
            '排序': 2, '筛选': 2, '格式化': 2, '优化': 3, '预测': 3,
            
            # 简单操作词（减分）
            '获取': -1, '查询': -1, '显示': -1, '返回': -1, '输出': -1,
        }
    
    def analyze(self, description):
        """分析任务描述的复杂度"""
        if not description:
            return 0, ["无任务描述"]
        
        score = 0
        reasons = []
        
        # 1. 长度分析
        if len(description) > 30:
            score += 1
            reasons.append(f"描述长度: {len(description)}")
        
        # 2. 标点符号分析
        punctuation_count = len(re.findall(r'[，。、；,.]', description))
        if punctuation_count > 1:
            score += punctuation_count
            reasons.append(f"包含{punctuation_count}个子句")
        
        # 3. 关键词分析
        for keyword, weight in self.complexity_indicators.items():
            if keyword in description:
                score += weight
                if weight > 0:
                    reasons.append(f"复杂操作: {keyword}")
                else:
                    reasons.append(f"简单操作: {keyword}")
        
        # 4. 动词数量分析
        verbs = re.findall(r'[计算|分析|统计|处理|生成|转换|验证|提取|获取|查询|创建|删除|修改|格式化|排序|筛选]', description)
        if len(verbs) > 2:
            score += len(verbs) - 1
            reasons.append(f"包含{len(verbs)}个动作")
        
        return max(0, score), reasons

def smart_decompose(task_description=None, complexity_threshold=3):
    """
    增强版智能分解装饰器
    
    支持两种使用方式：
    1. @smart_decompose("任务描述")  # 直接在装饰器中写描述
    2. @smart_decompose()          # 使用函数的文档字符串
    
    参数:
        task_description: 任务描述字符串（可选）
        complexity_threshold: 复杂度阈值
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 优先使用装饰器参数中的描述，否则使用函数文档字符串
            final_task_desc = task_description or func.__doc__ or func.__name__
            
            print(f"🔍 增强版智能分解分析器")
            print(f"📝 函数: {func.__name__}")
            print(f"📋 任务: {final_task_desc}")
            print(f"📄 描述来源: {'装饰器参数' if task_description else '函数文档'}")
            print("="*50)
            
            # 分析复杂度
            analyzer = TaskComplexityAnalyzer()
            complexity, reasons = analyzer.analyze(final_task_desc)
            
            print(f"🧮 复杂度分析:")
            print(f"   评分: {complexity}")
            print(f"   阈值: {complexity_threshold}")
            print(f"   判断依据: {'; '.join(reasons)}")
            
            # 选择执行模式
            if complexity >= complexity_threshold:
                print(f"🚀 复杂度 {complexity} ≥ {complexity_threshold}, 启动分解模式")
                return execute_with_decomposition(final_task_desc, complexity, func.__name__)
            else:
                print(f"✅ 复杂度 {complexity} < {complexity_threshold}, 直接执行模式")
                return execute_directly(final_task_desc, func.__name__)
        
        return wrapper
    return decorator

def execute_with_decomposition(task_description, complexity_score, func_name):
    """分解执行模式"""
    print(f"\n🔄 分解执行模式")
    print("-" * 30)
    
    # 智能分解
    steps = smart_task_breakdown(task_description)
    
    print(f"📋 任务分解为 {len(steps)} 个步骤:")
    for i, step in enumerate(steps, 1):
        print(f"  {i}. {step}")
    
    print(f"\n⚡ 逐步执行:")
    results = []
    
    for i, step in enumerate(steps, 1):
        print(f"\n🔄 步骤 {i}: {step}")
        time.sleep(0.3)  # 模拟执行时间
        
        result = simulate_step_execution(step, i, len(steps))
        print(f"✅ 结果: {result}")
        results.append(result)
    
    final_result = results[-1] if results else "执行完成"
    
    print(f"\n🎉 分解执行完成!")
    print(f"🎯 最终结果: {final_result}")
    
    return {
        'execution_mode': 'decomposed',
        'function_name': func_name,
        'original_task': task_description,
        'complexity_score': complexity_score,
        'steps': steps,
        'results': results,
        'final_result': final_result,
        'steps_count': len(steps)
    }

def execute_directly(task_description, func_name):
    """直接执行模式"""
    print(f"\n✨ 直接执行模式")
    print("-" * 30)
    
    print(f"🔄 执行任务: {task_description}")
    time.sleep(0.5)
    
    result = simulate_direct_execution(task_description)
    
    print(f"✅ 执行完成: {result}")
    
    return {
        'execution_mode': 'direct',
        'function_name': func_name,
        'task': task_description,
        'result': result
    }

def smart_task_breakdown(task_desc):
    """智能任务分解"""
    
    # IP地址相关任务
    if 'ip' in task_desc.lower() and ('求和' in task_desc or '计算' in task_desc):
        return [
            "获取当前系统IP地址",
            "将IP地址按点号分割",
            "将各段转换为数字",
            "计算数字总和"
        ]
    
    # 文本分析相关
    elif '文本' in task_desc and '分析' in task_desc:
        steps = ["读取文本内容"]
        if '统计' in task_desc:
            steps.append("统计文本特征")
        if '转换' in task_desc or '大写' in task_desc:
            steps.append("执行文本转换")
        if '关键词' in task_desc:
            steps.append("提取关键词")
        steps.append("整合分析结果")
        return steps
    
    # 数据处理相关
    elif '数据' in task_desc and ('分析' in task_desc or '处理' in task_desc):
        return [
            "加载数据源",
            "清洗和预处理数据", 
            "执行数据分析",
            "生成分析报告"
        ]
    
    # 时间相关任务
    elif '时间' in task_desc:
        steps = ["获取系统时间"]
        if '格式化' in task_desc:
            steps.append("格式化时间显示")
        return steps
    
    # 计算相关任务
    elif '计算' in task_desc:
        return [
            "解析计算需求",
            "执行数值计算",
            "返回计算结果"
        ]
    
    # 默认分解
    else:
        if len(task_desc) > 40:
            return [
                "解析任务需求",
                "准备执行环境",
                "执行核心功能", 
                "整理输出结果"
            ]
        else:
            return [
                "分析任务需求",
                "执行任务操作",
                "返回执行结果"
            ]

def simulate_step_execution(step, step_num, total_steps):
    """模拟步骤执行"""
    
    if "IP地址" in step:
        if "获取" in step:
            return "192.168.1.100"
        elif "分割" in step:
            return "[192, 168, 1, 100]"
        elif "转换" in step:
            return "数字数组: [192, 168, 1, 100]"
        elif "求和" in step or "计算" in step:
            return "461 (192+168+1+100)"
    
    elif "文本" in step:
        if "读取" in step:
            return "Hello World Python"
        elif "统计" in step:
            return "字符数: 18, 单词数: 3"
        elif "转换" in step:
            return "HELLO WORLD PYTHON"
        elif "关键词" in step:
            return "['Hello', 'World', 'Python']"
        elif "整合" in step:
            return "文本分析完成"
    
    elif "时间" in step:
        if "获取" in step:
            return "2025-11-24 21:40:00"
        elif "格式化" in step:
            return "2025年11月24日 21:40:00"
    
    elif "计算" in step:
        if "解析" in step:
            return "识别数学表达式"
        elif "执行" in step:
            return "计算结果: 42"
        elif "返回" in step:
            return "42"
    
    return f"步骤{step_num}执行完成"

def simulate_direct_execution(task_desc):
    """模拟直接执行"""
    
    if "时间" in task_desc:
        return "2025-11-24 21:40:00"
    elif "求和" in task_desc or "计算" in task_desc:
        if "1+2+3" in task_desc:
            return "6"
        elif "ip" in task_desc.lower():
            return "IP地址各段求和: 461"
        else:
            return "计算结果: 42"
    elif "获取" in task_desc:
        return "数据获取成功"
    elif "查询" in task_desc:
        return "查询完成"
    else:
        return "任务执行完成"

# === 测试用例：展示新的使用方式 ===

if __name__ == "__main__":
    print("🎯 增强版智能分解装饰器测试")
    print("="*60)
    print("新特性：支持直接在装饰器中写任务描述！")
    print("="*60)
    
    # === 新方式：直接在装饰器中写描述 ===
    
    # 你的原始例子 - 新写法
    @smart_decompose("把当前的ip地址进行求和，根据.进行分开")
    def process_ip():
        pass  # 函数只做命名标记
    
    @smart_decompose("查询当前系统时间")
    def get_current_time():
        pass
    
    @smart_decompose("根据字符串验证并且判断系统ip是什么")
    def validate_and_check_ip():
        pass
    
    # 更复杂的例子
    @smart_decompose("分析文本'Hello World'，统计字符数，转换大写，然后逆序排列")
    def complex_text_analysis():
        pass
    
    @smart_decompose("生成1到10的数字序列，计算平方和，然后求平均值")
    def math_operations():
        pass
    
    # === 传统方式：使用函数文档字符串（向下兼容） ===
    
    @smart_decompose()
    def traditional_way():
        """处理数据并转换格式"""
        pass
    
    # === 自定义复杂度阈值 ===
    
    @smart_decompose("处理并验证数据", complexity_threshold=1)  # 低阈值，容易分解
    def low_threshold_task():
        pass
    
    @smart_decompose("分析数据，统计结果，生成报告", complexity_threshold=10)  # 高阈值
    def high_threshold_task():
        pass
    
    # 执行测试
    test_cases = [
        ("新方式-IP处理", process_ip),
        ("新方式-时间查询", get_current_time),
        ("新方式-IP验证", validate_and_check_ip),
        ("新方式-文本分析", complex_text_analysis),
        ("新方式-数学运算", math_operations),
        ("传统方式-兼容", traditional_way),
        ("自定义-低阈值", low_threshold_task),
        ("自定义-高阈值", high_threshold_task),
    ]
    
    results = []
    
    for test_name, test_func in test_cases:
        print(f"\n🧪 【{test_name}】")
        try:
            result = test_func()
            results.append({
                'name': test_name,
                'mode': result['execution_mode'],
                'success': True,
                'function': result['function_name']
            })
            
        except Exception as e:
            results.append({
                'name': test_name,
                'mode': 'error',
                'success': False,
                'error': str(e)
            })
        
        print("-" * 60)
    
    # 测试总结
    print(f"\n📊 增强版测试总结")
    print("="*60)
    
    success_count = sum(1 for r in results if r['success'])
    direct_count = sum(1 for r in results if r.get('mode') == 'direct')
    decomposed_count = sum(1 for r in results if r.get('mode') == 'decomposed')
    
    print(f"✅ 成功执行: {success_count}/{len(results)} 个")
    print(f"📋 直接执行: {direct_count} 个")
    print(f"🔄 分解执行: {decomposed_count} 个")
    
    print(f"\n🎉 新特性测试完成!")
    print("💡 现在支持两种使用方式:")
    print("   1. @smart_decompose('任务描述') - 新方式！")
    print("   2. @smart_decompose() + 函数文档 - 兼容旧方式")
    print("✨ 函数现在只需要做命名标记，更简洁！")
