#!/usr/bin/env python3.11
"""最终正确版 MiniMax LLM适配器"""

import asyncio
import json
import os
from typing import List, Optional
from browser_use.llm.base import BaseChatModel, BaseMessage
from browser_use.llm.views import ChatInvokeCompletion, ChatInvokeUsage

class MinimaxChatModel(BaseChatModel):
    """MiniMax API适配器 - 正确返回格式"""
    
    def __init__(self, api_key: str, model: str = "minimax-m2"):
        self.api_key = api_key
        self.model = model
        self.url = "https://api.minimaxi.com/v1/chat/completions"
        
    @property
    def name(self) -> str:
        return "minimax"
    
    @property
    def provider(self) -> str:
        return "minimax"
        
    @property
    def model_name(self) -> str:
        return self.model
    
    async def ainvoke(self, messages: List[BaseMessage], output_format=None, **kwargs) -> ChatInvokeCompletion[str]:
        """异步调用MiniMax API - 返回ChatInvokeCompletion对象"""
        
        # 转换消息格式
        formatted_messages = []
        for msg in messages:
            formatted_messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        # 构建请求
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": self.model,
            "messages": formatted_messages,
            "stream": False,
            "max_tokens": kwargs.get("max_tokens", 2000),
            "temperature": kwargs.get("temperature", 0.7)
        }
        
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url, json=data, headers=headers) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        return ChatInvokeCompletion(
                            completion=f"Error: HTTP {response.status} - {error_text}",
                            usage=ChatInvokeUsage(
                                prompt_tokens=0,
                                prompt_cached_tokens=None,
                                prompt_cache_creation_tokens=None,
                                prompt_image_tokens=None,
                                completion_tokens=0,
                                total_tokens=0
                            )
                        )
                    
                    result = await response.json()
                    if 'choices' in result and len(result['choices']) > 0:
                        content = result['choices'][0]['message']['content']
                        
                        # 提取使用统计（如果有）
                        usage_data = result.get('usage', {})
                        usage = ChatInvokeUsage(
                            prompt_tokens=usage_data.get('prompt_tokens', 0),
                            prompt_cached_tokens=usage_data.get('prompt_cached_tokens', None),
                            prompt_cache_creation_tokens=usage_data.get('prompt_cache_creation_tokens', None),
                            prompt_image_tokens=usage_data.get('prompt_image_tokens', None),
                            completion_tokens=usage_data.get('completion_tokens', 0),
                            total_tokens=usage_data.get('total_tokens', 0)
                        )
                        
                        return ChatInvokeCompletion(
                            completion=content,
                            usage=usage
                        )
                    else:
                        return ChatInvokeCompletion(
                            completion="Error: No response from MiniMax API",
                            usage=ChatInvokeUsage(
                                prompt_tokens=0,
                                prompt_cached_tokens=None,
                                prompt_cache_creation_tokens=None,
                                prompt_image_tokens=None,
                                completion_tokens=0,
                                total_tokens=0
                            )
                        )
                        
        except Exception as e:
            return ChatInvokeCompletion(
                completion=f"Error: {str(e)}",
                usage=ChatInvokeUsage(
                    prompt_tokens=0,
                    prompt_cached_tokens=None,
                    prompt_cache_creation_tokens=None,
                    prompt_image_tokens=None,
                    completion_tokens=0,
                    total_tokens=0
                )
            )

# 测试函数
async def test_minimax_correct():
    """测试正确的返回格式"""
    api_key = os.getenv('MINIMAX_API_KEY')
    if not api_key:
        print("❌ 请设置MINIMAX_API_KEY环境变量")
        return
    
    print("🚀 测试正确返回格式...")
    
    llm = MinimaxChatModel(api_key=api_key)
    from browser_use.llm.messages import UserMessage
    
    messages = [
        UserMessage(content="请说'最终成功'")
    ]
    
    print("📝 测试消息: 最终成功")
    result = await llm.ainvoke(messages)
    print(f"🤖 响应: {result.completion}")
    print(f"📊 Token使用: {result.usage.total_tokens if result.usage else 'Unknown'}")
    print("✅ 测试完成")

if __name__ == "__main__":
    asyncio.run(test_minimax_correct())
