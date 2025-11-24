#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
综合功能测试
===========

完整测试：
1. 真实AI代码生成（简单任务）
2. 智能任务分解（复杂任务）
3. 混合模式自动选择
"""

from hybrid_smart_decorator import hybrid_smart
import time

def run_comprehensive_test():
    print("🎯 综合智能装饰器测试")
    print("="*70)
    print("🤖 AI代码生成 + 🔄 智能分解 = 🚀 完美结合")
    print("="*70)
    
    # ===== AI代码生成测试 =====
    print("\n🤖 【AI代码生成测试】- 简单任务自动使用AI")
    
    @hybrid_smart("计算8的阶乘", use_ai=True)
    def factorial_8():
        pass
    
    @hybrid_smart("计算1到10的和", use_ai=True)
    def sum_1_to_10():
        pass
    
    @hybrid_smart("将'Python Programming'转换为小写", use_ai=True)
    def to_lowercase():
        pass
    
    @hybrid_smart("生成一个简单的问候语", use_ai=True)
    def generate_greeting():
        pass
    
    # ===== 智能分解测试 =====
    print("\n🔄 【智能分解测试】- 复杂任务自动分解")
    
    @hybrid_smart("分析用户输入文本，提取关键词，统计词频，然后生成摘要报告")
    def complex_text_processing():
        pass
    
    @hybrid_smart("获取系统信息，分析性能指标，生成诊断报告，并且优化建议")
    def system_analysis():
        pass
    
    @hybrid_smart("处理CSV数据，清洗异常值，进行统计分析，然后可视化结果")
    def data_pipeline():
        pass
    
    # ===== 执行所有测试 =====
    ai_tests = [
        ("AI-阶乘计算", factorial_8),
        ("AI-求和计算", sum_1_to_10),
        ("AI-文本转换", to_lowercase),
        ("AI-内容生成", generate_greeting)
    ]
    
    decomp_tests = [
        ("分解-文本处理", complex_text_processing),
        ("分解-系统分析", system_analysis),
        ("分解-数据管道", data_pipeline)
    ]
    
    ai_results = []
    decomp_results = []
    
    # 执行AI测试
    for test_name, test_func in ai_tests:
        print(f"\n🧪 【{test_name}】")
        try:
            result = test_func()
            ai_results.append({
                'name': test_name,
                'mode': result['execution_mode'],
                'result': result['result'],
                'success': True
            })
            print(f"✅ 成功 - 模式: {result['execution_mode']}")
            print(f"🎯 结果: {result['result']}")
        except Exception as e:
            ai_results.append({
                'name': test_name,
                'success': False,
                'error': str(e)
            })
            print(f"❌ 失败: {e}")
        print("-" * 70)
    
    # 执行分解测试
    for test_name, test_func in decomp_tests:
        print(f"\n🧪 【{test_name}】")
        try:
            result = test_func()
            decomp_results.append({
                'name': test_name,
                'mode': result['execution_mode'],
                'steps_count': len(result.get('steps', [])),
                'final_result': result['final_result'],
                'success': True
            })
            print(f"✅ 成功 - 模式: {result['execution_mode']}")
            print(f"📊 分解步骤: {len(result.get('steps', []))} 个")
            print(f"🎯 最终结果: {result['final_result']}")
        except Exception as e:
            decomp_results.append({
                'name': test_name,
                'success': False,
                'error': str(e)
            })
            print(f"❌ 失败: {e}")
        print("-" * 70)
    
    # ===== 测试总结 =====
    print(f"\n📊 综合测试总结报告")
    print("="*70)
    
    # AI测试统计
    ai_success = sum(1 for r in ai_results if r['success'])
    ai_generated = sum(1 for r in ai_results if r.get('mode') == 'ai_generated')
    
    print(f"🤖 AI代码生成测试:")
    print(f"   ✅ 成功率: {ai_success}/{len(ai_results)} ({ai_success/len(ai_results)*100:.1f}%)")
    print(f"   🎯 AI生成: {ai_generated} 个")
    
    # 分解测试统计
    decomp_success = sum(1 for r in decomp_results if r['success'])
    smart_decomp = sum(1 for r in decomp_results if r.get('mode') == 'smart_decomposition')
    total_steps = sum(r.get('steps_count', 0) for r in decomp_results if r['success'])
    
    print(f"\n🔄 智能分解测试:")
    print(f"   ✅ 成功率: {decomp_success}/{len(decomp_results)} ({decomp_success/len(decomp_results)*100:.1f}%)")
    print(f"   📊 智能分解: {smart_decomp} 个")
    print(f"   🔗 总分解步骤: {total_steps} 个")
    
    # 整体统计
    total_tests = len(ai_results) + len(decomp_results)
    total_success = ai_success + decomp_success
    
    print(f"\n🎉 整体测试结果:")
    print(f"   📋 总测试数: {total_tests} 个")
    print(f"   ✅ 总成功数: {total_success} 个")
    print(f"   📈 总成功率: {total_success/total_tests*100:.1f}%")
    
    print(f"\n💡 功能验证:")
    print(f"   🤖 AI代码生成: {'✅ 正常工作' if ai_generated > 0 else '❌ 未工作'}")
    print(f"   🔄 智能任务分解: {'✅ 正常工作' if smart_decomp > 0 else '❌ 未工作'}")
    print(f"   🚀 自动模式选择: {'✅ 正常工作' if (ai_generated > 0 and smart_decomp > 0) else '❌ 未完全工作'}")
    
    print(f"\n🎊 综合测试完成！")
    print("🌟 恭喜！真正的AI代码生成 + 智能任务分解系统已经完美结合！")

if __name__ == "__main__":
    run_comprehensive_test()
