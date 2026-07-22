import os
import random
import re
from openai import OpenAI

from .base_ai import BaseAI
from src.model.constants import X, O, N

class AlibabaQwenAI(BaseAI):
    def __init__(self, symbol, api_key = None, model = "qwen-plus", base_url = None):
        super().__init__(symbol)
        self.opponent = X if symbol == O else O
        self.api_key = api_key or getenv("DASHSCOPE_API_KEY")
        if not self.api_key:
            raise ValueError("DASHSCOPE_API_KEY environment variarble (or api_key arg) is required. Get one from Alibaba Cloud Model Studio.")
    
        self.base_url = base_url or os.getenv(
            "DASHSCOPE_BASE_URL",
            "https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

        self.client = OpenAI(api_key = self.api_key, base_url = self.base_url)
        self.model = model
    
    def _format_board(self, board):
        """Human-readable board + position legend (1-9)."""
        cells = [c if c in (X, O) else "-" for c in board.grid]
        return (
            f" {cells[0]} | {cells[1]} | {cells[2]} \n"
            f"-----------\n"
            f" {cells[3]} | {cells[4]} | {cells[5]} \n"
            f"-----------\n"
            f" {cells[6]} | {cells[7]} | {cells[8]} \n"
            f"Positions (1-9):\n"
            f" 1 | 2 | 3 \n-----------\n 4 | 5 | 6 \n-----------\n 7 | 8 | 9 "
        )
    
    def get_move(self, board):
        free = board.get_free_indices()
        if not free:
            return None

        free_1based = [i+1 for i in free]
        system = ("You are an expert Tic-Tac-Toe player. Respond with only a single integer 1-9. No other text allowed.")
        user = (
            f"You are '{self.symbol}', opponent is '{self.opponent}'.\n"
            f"Board (positions 1-9, left→right, top→bottom):\n"
            f"{self._format_board(board)}\n\n"
            f"Legal moves: {free_1based}\n"
            f"Play the best move: win now if possible, else block, "
            f"else take center/corners/forks. Reply with only the number."
        )

        try:
            resp = self.client.chat.completions.create(
                model = self.model,
                messages = [
                    {"role": "system", "content": system},
                    {"role": "user", "content" : user},
                ],
                temperature = 0.1,
                max_tokens = 16,
            )
            
            text = (resp.choices[0].message.content or "").strip()
            m = re.search(r"\b([1-9])\b", text)
            if m:
                idx = int(m.group(1)) -1
                if idx in free:
                    return idx
                
            print(f"[Qwen]Bad/Illegal reply {text!r}; using fallback.")

        except Exception as e:
            print(f"[Qwen] API error: {e}; using fallback.")

        return random.choice(free)

