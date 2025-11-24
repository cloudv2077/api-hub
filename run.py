#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 标准调用版 - 显示AI生成的代码
==============================

用法：
python run.py 计算10的阶乘
python run.py 翻译hello为中文
python run.py 分析文本内容并生成摘要报告

增强功能：显示AI生成的函数代码内容
"""

import sys
from hybrid_smart_decorator import hybrid_smart

def main():
    if len(sys.argv) < 2:
        print("""
🚀 智能任务执行器 - 标准版（显示代码）
==================================

用法: python run.py <任务描述>

示例:
  python run.py 计算10的阶乘
  python run.py 计算1到100的和  
  python run.py 翻译hello为中文
  python run.py 生成一首关于春天的诗
  python run.py 分析文本内容，统计词频，生成摘要

✨ 简单任务自动AI生成，复杂任务自动分解！
🔍 新增：显示AI生成的完整函数代码！
        """)
        return
    
    # 获取任务描述（合并所有参数）
    task_description = " ".join(sys.argv[1:])
    
    print(f"🎯 执行任务: {task_description}")
    print("="*50)
    
    # 动态创建并执行任务
    @hybrid_smart(task_description)
    def execute_task():
        pass
    
    try:
        result = execute_task()
        
        print(f"\n✅ 任务完成!")
        print(f"📊 执行模式: {result.get('execution_mode', 'unknown')}")
        
        if result['execution_mode'] == 'ai_generated':
            print(f"🤖 AI生成结果: {result['result']}")
            
            # 🌟 显示生成的函数代码
            generated_code = result.get('generated_code')
            if generated_code:
                print(f"\n📝 AI生成的函数代码:")
                print("```python")
                print(generated_code)
                print("```")
                
                print(f"\n💡 代码说明:")
                print(f"   - 函数功能: {task_description}")
                print(f"   - 返回结果: {result['result']}")
                print(f"   - 代码行数: {len(generated_code.split('\\n'))} 行")
                
        elif result['execution_mode'] == 'smart_decomposition':
            print(f"🔄 智能分解完成")
            print(f"📊 分解步骤数: {len(result.get('steps', []))} 个")
            print(f"🎯 最终结果: {result['final_result']}")
            
            # 显示分解的步骤
            steps = result.get('steps', [])
            if steps:
                print(f"\n📋 分解步骤详情:")
                for i, step in enumerate(steps, 1):
                    print(f"   {i}. {step}")
                    
    except Exception as e:
        print(f"❌ 执行失败: {e}")

if __name__ == "__main__":
    main()
