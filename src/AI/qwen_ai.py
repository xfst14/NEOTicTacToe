from openai import OpenAI
import os

class QwenAI:
    def __init__(self, symbol):
        self.symbol = symbol
        self.client = OpenAI(
            api_key = os.getenv("DASHSCOPE_API_KEY"),
            base_url = "https://dashscope-us.aliyuncs.com/compatible-mode/v1",
        )
