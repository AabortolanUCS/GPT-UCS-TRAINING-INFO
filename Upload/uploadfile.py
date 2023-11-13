import openai
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
openai.File.create(
  file=open(".\\Dados-Migrados\\dados.jsonl", "rb"),
  purpose='fine-tune'
)
