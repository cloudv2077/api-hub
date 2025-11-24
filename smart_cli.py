#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能命令行接口 - 增强版
=====================

新增功能：显示AI生成的函数代码内容

支持多种调用模式：
1. 直接执行：python smart_cli.py "任务描述"
2. 交互模式：python smart_cli.py -i
3. 强制AI模式：python smart_cli.py -a "任务描述"
4. 强制分解模式：python smart_cli.py -d "任务描述"
5. 显示代码：python smart_cli.py --show-code "任务描述"
"""

import sys
import argparse
from hybrid_smart_decorator import hybrid_smart

class SmartCLI:
    def __init__(self):
        self.banner = """
🚀 智能任务CLI - 最强大的AI代码生成工具
=====================================
✨ 描述任务，自动执行！
🤖 简单任务 → AI生成代码
🔄 复杂任务 → 智能分解
🔍 新增：显示AI生成的函数代码！
"""
    
    def execute_task(self, task_description, force_mode=None, use_ai=True, show_code=True):
        """执行任务"""
        print(f"📝 任务: {task_description}")
        print("="*60)
        
        # 动态创建装饰器函数
        if force_mode == 'ai':
            # 强制AI模式
            @hybrid_smart(task_description, use_ai=use_ai, complexity_threshold=999)
            def dynamic_task():
                pass
        elif force_mode == 'decompose':
            # 强制分解模式
            @hybrid_smart(task_description, complexity_threshold=0)
            def dynamic_task():
                pass
        else:
            # 自动选择模式
            @hybrid_smart(task_description, use_ai=use_ai)
            def dynamic_task():
                pass
        
        try:
            result = dynamic_task()
            
            print(f"\n🎉 执行完成!")
            print(f"📊 执行模式: {result.get('execution_mode', 'unknown')}")
            
            if result.get('execution_mode') == 'ai_generated':
                print(f"🤖 AI生成结果: {result.get('result', '无结果')}")
                
                # 显示生成的函数代码
                if show_code:
                    generated_code = result.get('generated_code')
                    if generated_code:
                        print(f"\n📝 AI生成的函数代码:")
                        print("```python")
                        print(generated_code)
                        print("```")
                        
                        # 代码分析
                        code_lines = generated_code.split('\n')
                        print(f"\n🔍 代码分析:")
                        print(f"   📏 代码行数: {len(code_lines)} 行")
                        print(f"   🎯 函数功能: {task_description}")
                        print(f"   📤 返回值: {result.get('result', '未知')}")
                        
                        # 检测代码特征
                        code_features = []
                        if 'import' in generated_code:
                            code_features.append("使用了外部库")
                        if 'for' in generated_code or 'while' in generated_code:
                            code_features.append("包含循环结构")
                        if 'if' in generated_code:
                            code_features.append("包含条件判断")
                        if 'def' in generated_code:
                            code_features.append("定义了函数")
                            
                        if code_features:
                            print(f"   🔧 代码特征: {', '.join(code_features)}")
                
            elif result.get('execution_mode') == 'smart_decomposition':
                print(f"🔄 分解步骤数: {len(result.get('steps', []))} 个")
                print(f"🎯 最终结果: {result.get('final_result', '执行完成')}")
                
                # 显示详细步骤
                steps = result.get('steps', [])
                if steps and show_code:
                    print(f"\n📋 智能分解步骤:")
                    for i, step in enumerate(steps, 1):
                        print(f"   {i}. {step}")
            
            return result
            
        except Exception as e:
            print(f"❌ 执行失败: {e}")
            return None
    
    def interactive_mode(self):
        """增强的交互模式"""
        print(self.banner)
        print("💡 交互模式 - 输入 'quit' 退出，'help' 查看帮助")
        print("="*60)
        
        while True:
            try:
                task = input("\n🎯 请输入任务描述: ").strip()
                
                if task.lower() in ['quit', 'exit', 'q']:
                    print("👋 再见！")
                    break
                
                if task.lower() in ['help', 'h']:
                    print("""
🆘 交互模式帮助:
================
• 直接输入任务描述自动执行
• -a <任务> : 强制使用AI生成模式  
• -d <任务> : 强制使用分解模式
• --no-code : 不显示生成的代码
• help : 显示此帮助
• quit : 退出程序

示例:
  计算10的阶乘
  -a 翻译hello为中文
  -d 复杂的数据分析任务
                    """)
                    continue
                
                if not task:
                    print("⚠️ 请输入有效的任务描述")
                    continue
                
                # 解析特殊指令
                show_code = True
                force_mode = None
                
                if task.startswith('-a '):
                    force_mode = 'ai'
                    task = task[3:]
                elif task.startswith('-d '):
                    force_mode = 'decompose'
                    task = task[3:]
                elif task.startswith('--no-code '):
                    show_code = False
                    task = task[11:]
                
                # 执行任务
                self.execute_task(task, force_mode=force_mode, show_code=show_code)
                
            except KeyboardInterrupt:
                print("\n👋 再见！")
                break
            except Exception as e:
                print(f"❌ 错误: {e}")

def main():
    cli = SmartCLI()
    
    parser = argparse.ArgumentParser(
        description="🚀 智能任务CLI - 描述即执行，显示生成代码！",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用示例：
  python smart_cli.py "计算10的阶乘"                    # 自动模式+显示代码
  python smart_cli.py -a "翻译hello为中文"              # 强制AI模式  
  python smart_cli.py -d "处理数据，分析，生成报告"       # 强制分解模式
  python smart_cli.py --no-code "计算平方根"            # 不显示代码
  python smart_cli.py -i                              # 交互模式
        """
    )
    
    parser.add_argument('task', nargs='?', help='任务描述')
    parser.add_argument('-i', '--interactive', action='store_true', help='交互模式')
    parser.add_argument('-a', '--ai', action='store_true', help='强制使用AI生成模式')
    parser.add_argument('-d', '--decompose', action='store_true', help='强制使用分解模式')
    parser.add_argument('--no-ai', action='store_true', help='禁用AI，仅使用分解模式')
    parser.add_argument('--no-code', action='store_true', help='不显示生成的代码')
    parser.add_argument('-v', '--verbose', action='store_true', help='详细输出')
    
    args = parser.parse_args()
    
    # 交互模式
    if args.interactive:
        cli.interactive_mode()
        return
    
    # 检查任务描述
    if not args.task:
        print("❌ 错误: 请提供任务描述或使用 -i 进入交互模式")
        parser.print_help()
        return
    
    # 确定执行参数
    force_mode = None
    use_ai = not args.no_ai
    show_code = not args.no_code
    
    if args.ai:
        force_mode = 'ai'
    elif args.decompose:
        force_mode = 'decompose'
    
    # 显示banner（详细模式）
    if args.verbose:
        print(cli.banner)
    
    # 执行任务
    result = cli.execute_task(args.task, force_mode=force_mode, 
                             use_ai=use_ai, show_code=show_code)
    
    # 返回适当的退出码
    sys.exit(0 if result else 1)

if __name__ == "__main__":
    main()
