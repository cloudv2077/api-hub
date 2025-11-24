#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🚀 最简单的调用方式
==================

用法：
python run.py 计算10的阶乘
python run.py 翻译hello为中文
python run.py 分析文本内容并生成摘要报告

一行命令，自动执行！
"""

import sys
from hybrid_smart_decorator import hybrid_smart

def main():
    if len(sys.argv) < 2:
        print("""
🚀 智能任务执行器 - 最简单用法
=============================

用法: python run.py <任务描述>

示例:
  python run.py 计算10的阶乘
  python run.py 计算1到100的和  
  python run.py 翻译hello为中文
  python run.py 生成一首关于春天的诗
  python run.py 分析文本内容，统计词频，生成摘要

✨ 简单任务自动AI生成，复杂任务自动分解！
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
        
        if result['execution_mode'] == 'ai_generated':
            print(f"🤖 AI生成结果: {result['result']}")
        else:
            print(f"🔄 智能分解完成: {result['final_result']}")
            
    except Exception as e:
        print(f"❌ 执行失败: {e}")

if __name__ == "__main__":
    main()
