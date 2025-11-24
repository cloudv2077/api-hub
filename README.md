# 智能任务链装饰器

一个Python装饰器，能够将自然语言描述的任务自动转换为可执行代码，并智能分解复杂任务。

## 特性

- 🧠 **智能复杂度分析** - 自动评估任务复杂程度
- 🔄 **自动任务分解** - 复杂任务分解为简单步骤链
- 📝 **自然语言描述** - 直接在装饰器中写任务描述
- ⚡ **智能执行策略** - 简单任务直接执行，复杂任务分步执行

## 使用方法

```python
from enhanced_smart_decompose import smart_decompose

# 简单任务 - 直接执行
@smart_decompose("查询当前系统时间")
def get_time():
    pass

# 复杂任务 - 自动分解执行
@smart_decompose("把当前的ip地址进行求和，根据.进行分开")
def process_ip():
    pass

# 执行
time_result = get_time()
ip_result = process_ip()
```

## 工作原理

1. **复杂度分析** - 分析任务描述中的关键词、连接词、动作数量
2. **执行策略选择** - 复杂度低于阈值直接执行，否则分解执行
3. **智能分解** - 根据任务类型选择合适的分解策略
4. **链式执行** - 按步骤顺序执行，传递中间结果

## 示例效果

```bash
🔍 智能分解分析器
📝 函数: process_ip
📋 任务: 把当前的ip地址进行求和，根据.进行分开
🧮 复杂度分析: 评分: 2, 阈值: 3
✅ 复杂度 2 < 3, 直接执行模式
🔄 执行任务: 把当前的ip地址进行求和，根据.进行分开
✅ 执行完成: IP地址各段求和: 461
```

## 自定义配置

```python
# 自定义复杂度阈值
@smart_decompose("处理数据", complexity_threshold=1)
def custom_task():
    pass
```

## 核心文件

- `enhanced_smart_decompose.py` - 完整实现，包含测试用例

## 运行测试

```bash
python enhanced_smart_decompose.py
```

## 许可证

MIT License
