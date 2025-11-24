#!/bin/bash
# 智能任务装饰器 - 一键安装脚本

echo "🚀 智能任务装饰器 - 一键安装"
echo "================================"

# 获取当前目录
INSTALL_DIR=$(pwd)

# 创建可执行脚本
cat > /usr/local/bin/smart << 'SCRIPT'
#!/usr/bin/env python3
import sys
import os

# 添加安装目录到Python路径
sys.path.insert(0, 'INSTALL_DIR_PLACEHOLDER')

from hybrid_smart_decorator import hybrid_smart

def main():
    if len(sys.argv) < 2:
        print("""
🚀 智能任务执行器
================

用法: smart <任务描述>

示例:
  smart 计算10的阶乘
  smart 翻译hello为中文  
  smart 分析文本并生成摘要
        """)
        return
    
    task_description = " ".join(sys.argv[1:])
    print(f"🎯 执行: {task_description}")
    print("="*40)
    
    @hybrid_smart(task_description)
    def task():
        pass
    
    try:
        result = task()
        if result['execution_mode'] == 'ai_generated':
            print(f"🤖 结果: {result['result']}")
        else:
            print(f"🔄 完成: {result['final_result']}")
    except Exception as e:
        print(f"❌ 失败: {e}")

if __name__ == "__main__":
    main()
SCRIPT

# 替换安装路径
sed -i.bak "s|INSTALL_DIR_PLACEHOLDER|${INSTALL_DIR}|g" /usr/local/bin/smart

# 设置执行权限
chmod +x /usr/local/bin/smart

echo "✅ 安装完成！"
echo ""
echo "📖 使用方法："
echo "  smart 计算10的阶乘"
echo "  smart 翻译hello为中文"
echo "  smart 分析数据并生成报告"
echo ""
echo "🎉 现在可以在任何地方使用 'smart' 命令了！"
