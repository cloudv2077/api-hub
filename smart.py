#!/usr/bin/env python3
"""
🚀 终极简化版 - 一行搞定！
========================

最简单用法：
python smart.py 计算10的阶乘
python smart.py 翻译hello为中文
python smart.py 分析数据并生成报告

无需任何配置，描述即执行！
"""
import sys
from hybrid_smart_decorator import hybrid_smart

# 一行执行任务
if len(sys.argv) > 1:
    task = " ".join(sys.argv[1:])
    @hybrid_smart(task)
    def run(): pass
    result = run()
    print(f"\n🎯 最终结果: {result.get('result', result.get('final_result', '完成'))}")
else:
    print("用法: python smart.py <任务描述>")
