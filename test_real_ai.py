#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试真实AI代码生成功能
"""

from hybrid_smart_decorator import hybrid_smart

# 测试真实AI代码生成（简单任务）
@hybrid_smart("计算5的阶乘", use_ai=True, complexity_threshold=4)
def test_factorial():
    """计算5的阶乘"""
    pass

@hybrid_smart("将文本'hello world'转换为大写", use_ai=True, complexity_threshold=4)  
def test_uppercase():
    """将文本转换为大写"""
    pass

if __name__ == "__main__":
    print("🧪 测试真实AI代码生成")
    print("="*50)
    
    print("\n🧪 【测试1: 阶乘计算】")
    try:
        result = test_factorial()
        print(f"📊 执行模式: {result['execution_mode']}")
        print(f"🎯 结果: {result['result']}")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    print("\n🧪 【测试2: 文本转换】")
    try:
        result = test_uppercase()
        print(f"📊 执行模式: {result['execution_mode']}")
        print(f"🎯 结果: {result['result']}")
    except Exception as e:
        print(f"❌ 错误: {e}")
    
    print("\n✅ AI测试完成")
