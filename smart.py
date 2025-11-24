#!/usr/bin/env python3
"""
🚀 终极简化版 - 显示AI生成的代码
===============================

最简单用法：
python smart.py 计算10的阶乘
python smart.py 翻译hello为中文
python smart.py 分析数据并生成报告

新增功能：显示AI生成的函数代码内容
"""
import sys
from hybrid_smart_decorator import hybrid_smart

# 一行执行任务
if len(sys.argv) > 1:
    task = " ".join(sys.argv[1:])
    print(f"🎯 执行任务: {task}")
    print("="*50)
    
    @hybrid_smart(task)
    def run(): 
        pass
    
    result = run()
    
    # 显示执行结果
    print(f"\n✅ 任务完成!")
    print(f"📊 执行模式: {result.get('execution_mode', 'unknown')}")
    
    if result.get('execution_mode') == 'ai_generated':
        print(f"🎯 AI生成结果: {result.get('result', '无结果')}")
        
        # 🌟 新增：显示生成的函数代码
        generated_code = result.get('generated_code')
        if generated_code:
            print(f"\n📝 AI生成的函数代码:")
            print("```python")
            print(generated_code)
            print("```")
    
    elif result.get('execution_mode') == 'smart_decomposition':
        print(f"🔄 分解步骤数: {len(result.get('steps', []))} 个")
        print(f"🎯 最终结果: {result.get('final_result', '执行完成')}")
    
else:
    print("""
🚀 智能任务执行器 - 增强版
========================

用法: python smart.py <任务描述>

示例:
  python smart.py 计算10的阶乘
  python smart.py 翻译hello为中文  
  python smart.py 生成一首关于春天的诗
  python smart.py 分析数据并生成报告

✨ 新功能: 显示AI生成的函数代码内容！
    """)
