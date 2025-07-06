import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("エラー: .envファイルにANTHROPIC_API_KEYが設定されていません")
    exit(1)

client = anthropic.Anthropic()

try:
    message = client.messages.create(
        model="claude-opus-4-20250514",
        max_tokens=1000,
        temperature=1,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "なぜ太陽は東から昇るの？"
                    }
                ]
            }
        ]
    )
    print(message.content[0].text)
except Exception as e:
    print(f"API呼び出しエラー: {e}")
