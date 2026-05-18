---
name: ollama-gemma-router
description: Use the local Ollama Gemma model through the MCP tool ask_gemma whenever the user types @gemma, @local, asks to use Gemma, asks to use Ollama, or asks to use a local model. Do not run terminal commands for these requests.
---

# Ollama Gemma Router

When the user message starts with or contains:

- @gemma
- @local
- Gemma
- Ollama
- 로컬 모델
- 로컬 Ollama
- 내 컴퓨터 모델

You must follow these rules:

1. Do not run terminal commands.
2. Do not run `ollama list`.
3. Do not run `ollama serve`.
4. Use the MCP tool named `ask_gemma`.
5. Send the user's actual question as the `prompt` argument.
6. Return the MCP tool response directly in Korean.
7. If the tool response is garbled, still return the decoded meaning if clear.
8. If the MCP tool is unavailable, say: "ollama MCP 서버가 아직 로드되지 않았습니다. MCP Servers에서 refresh 해주세요."

Examples:

User:
@gemma 너는 누구야?

Action:
Call MCP tool `ask_gemma` with:
{
  "prompt": "너는 누구야?"
}

User:
@local 오늘 할 일을 정리해줘

Action:
Call MCP tool `ask_gemma` with:
{
  "prompt": "오늘 할 일을 정리해줘"
}
