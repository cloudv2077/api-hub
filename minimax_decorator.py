import requests
import json
import inspect
import functools
import re
from typing import Any, Callable

class MinimaxDecorator:
    def __init__(self):
        self.URL = "https://api.minimaxi.com/v1/chat/completions"
        self.MODEL = "minimax-m2"
        self.API_KEY = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJHcm91cE5hbWUiOiLlpI_lhYjnlJ8iLCJVc2VyTmFtZSI6IuWkj-WFiOeUnyIsIkFjY291bnQiOiIiLCJTdWJqZWN0SUQiOiIxOTg3MDAwNzU5MzA0MDY1MTM2IiwiUGhvbmUiOiIxNTAxMTk5MDc1MCIsIkdyb3VwSUQiOiIxOTg3MDAwNzU5Mjk5ODcwODMyIiwiUGFnZU5hbWUiOiIiLCJNYWlsIjoiIiwiQ3JlYXRlVGltZSI6IjIwMjUtMTEtMDggMTU6MDc6NTMiLCJUb2tlblR5cGUiOjEsImlzcyI6Im1pbmltYXgifQ.vvK1D_jmbwDVnNJA8Idkfr9gJ5XcyrdNP8moCEonQ_MlC7YAJovREcOe1CKUoFQMaPqQnYBmy2xGtA9RTI114hk2BJzi_xxpAVU8tG5RzVb4sYcu3nS-kEcXffFDt3W53a48pH0KPQbvtIN4Cu2jPL6WTLIscEeqXhu00rogCPOa5Fm0sGwV9ObdiN4B__uqzX1VafBsxXxPCVNeJIdDoqv2GLClWPPnqKCdz4QwQ6jcJAkpNzbLn2148u5HM3FsNIJXYNr6aiJ0HiSrW5D30j7kH5BUs-ygMRMff5YFt7k73fh2XXh9XTidHg3LN3v4eJP0MUxE1wGyDnOMSOjO6g"
    
    def clean_response(self, response: str) -> str:
        """清理API响应，移除思考过程标记"""
        # 移除 <think> ... </think> 标签及其内容
        cleaned = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)
        # 移除多余的空白字符
        cleaned = cleaned.strip()
        # 移除开头的换行符
        cleaned = re.sub(r'^\n+', '', cleaned)
        return cleaned
    
    def call_api(self, prompt: str) -> str:
        """调用MiniMax API"""
        headers = {
            'Authorization': f'Bearer {self.API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            "model": self.MODEL,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3,
            "max_tokens": 800
        }
        
        try:
            response = requests.post(self.URL, headers=headers, json=data, timeout=30)
            response.raise_for_status()
            result = response.json()
            raw_content = result['choices'][0]['message']['content']
            # 清理响应内容
            return self.clean_response(raw_content)
        except requests.exceptions.RequestException as e:
            return f"API调用失败: {str(e)}"
        except KeyError as e:
            return f"API响应格式错误: {str(e)}"
    
    def auto_generate(self, func: Callable) -> Callable:
        """装饰器：根据函数备注自动生成函数实现"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 获取函数的文档字符串
            doc = inspect.getdoc(func)
            if not doc:
                return "错误：函数没有文档字符串，无法自动生成实现"
            
            # 获取函数签名
            sig = inspect.signature(func)
            func_name = func.__name__
            
            # 构建参数字符串
            args_str = ", ".join([str(arg) for arg in args])
            kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))
            
            # 构建提示词
            prompt = f"""
请根据以下信息直接执行任务并返回结果：

任务：{doc}
函数名：{func_name}
参数：{all_args}

请直接返回执行结果，不要包含任何解释、代码或思考过程。
对于计算任务返回数值结果，对于文本任务返回处理后的文本，对于生成任务返回生成的内容。
"""
            
            # 调用API生成结果
            result = self.call_api(prompt)
            return result
        
        return wrapper

# 创建装饰器实例
minimax = MinimaxDecorator()
auto_generate = minimax.auto_generate

# 测试函数
@auto_generate
def calculate_factorial(n):
    """计算n的阶乘"""
    pass

@auto_generate
def translate_text(text, target_language):
    """将文本翻译成目标语言"""
    pass

@auto_generate
def generate_poem(theme, style):
    """根据主题和风格生成一首诗"""
    pass

@auto_generate
def analyze_sentiment(text):
    """分析文本的情感倾向，返回正面、负面或中性"""
    pass

@auto_generate
def calculate_fibonacci(n):
    """计算斐波那契数列的第n项"""
    pass

@auto_generate
def summarize_text(text, max_words):
    """将文本总结为指定字数以内的摘要"""
    pass

def main():
    """测试函数"""
    print("=" * 60)
    print("MiniMax装饰器测试 - 自动函数生成")
    print("=" * 60)
    
    # 测试1：计算阶乘
    print("\n1. 测试计算阶乘:")
    try:
        result = calculate_factorial(6)
        print(f"6的阶乘 = {result}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试2：文本翻译
    print("\n2. 测试文本翻译:")
    try:
        result = translate_text("Good morning! How are you today?", "中文")
        print(f"翻译结果: {result}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试3：生成诗歌
    print("\n3. 测试生成诗歌:")
    try:
        result = generate_poem("春天", "现代诗")
        print(f"生成的诗歌:\n{result}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试4：情感分析
    print("\n4. 测试情感分析:")
    try:
        result = analyze_sentiment("这个产品质量很差，非常失望！")
        print(f"情感分析结果: {result}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试5：计算斐波那契数
    print("\n5. 测试计算斐波那契数:")
    try:
        result = calculate_fibonacci(10)
        print(f"斐波那契数列第10项 = {result}")
    except Exception as e:
        print(f"错误: {e}")
    
    # 测试6：文本摘要
    print("\n6. 测试文本摘要:")
    try:
        long_text = "人工智能是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器。该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。人工智能从诞生以来，理论和技术日益成熟，应用领域也不断扩大。"
        result = summarize_text(long_text, 30)
        print(f"文本摘要: {result}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n" + "=" * 60)
    print("测试完成！")

if __name__ == "__main__":
    main()
