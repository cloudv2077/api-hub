# MiniMax API 装饰器

这是一个基于 MiniMax API 的 Python 装饰器，可以根据函数的文档字符串自动生成函数实现。

## 功能特性

- **自动函数生成**：根据函数名和文档字符串，AI 自动实现函数功能
- **智能清理**：自动移除 API 响应中的思考过程标记
- **多种任务支持**：支持计算、翻译、文本生成、情感分析等多种任务
- **简单易用**：只需添加装饰器和文档字符串即可

## 使用方法

### 1. 基础使用

```python
from minimax_decorator import auto_generate

@auto_generate
def your_function(param1, param2):
    """这里写你想要实现的功能描述"""
    pass

# 调用函数
result = your_function("参数1", "参数2")
print(result)
```

### 2. 示例函数

#### 数学计算
```python
@auto_generate
def calculate_prime_factors(n):
    """计算n的所有质因数"""
    pass

result = calculate_prime_factors(60)
# 输出：[2, 2, 3, 5]
```

#### 文本处理
```python
@auto_generate
def extract_keywords(text, count):
    """从文本中提取指定数量的关键词"""
    pass

keywords = extract_keywords("人工智能技术发展迅速...", 5)
```

#### 创意生成
```python
@auto_generate
def generate_company_name(industry, style):
    """为指定行业生成具有特定风格的公司名称"""
    pass

name = generate_company_name("科技", "现代简洁")
```

## 配置说明

装饰器使用预配置的 MiniMax API：
- API地址：https://api.minimaxi.com/v1/chat/completions
- 模型：minimax-m2
- API密钥：已预配置

## 测试结果

运行 `python minimax_decorator.py` 可以看到以下测试结果：

- ✅ 计算阶乘：6! = 720
- ✅ 文本翻译：英文转中文
- ✅ 诗歌生成：生成现代诗
- ✅ 情感分析：识别负面情感
- ✅ 斐波那契数列：第10项 = 55
- ✅ 文本摘要：长文本压缩

## 注意事项

1. **网络连接**：需要稳定的网络连接访问 MiniMax API
2. **API限制**：遵守 MiniMax API 的使用限制和配额
3. **响应时间**：API 调用可能需要几秒钟时间
4. **错误处理**：装饰器包含基本的错误处理机制

## 扩展使用

你可以根据需要创建更多功能的装饰器函数：

```python
@auto_generate
def analyze_code_complexity(code):
    """分析代码的时间复杂度和空间复杂度"""
    pass

@auto_generate
def generate_sql_query(table_name, conditions):
    """根据条件生成SQL查询语句"""
    pass

@auto_generate
def convert_units(value, from_unit, to_unit):
    """单位转换，支持长度、重量、温度等"""
    pass
```

## 许可证

此项目仅供学习和测试使用。
