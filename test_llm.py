import litellm

litellm.set_verbose=True

base_url="https://api.robusta.dev"
api_key="16ecba1a-7993-4dd1-a98c-d201462ccba7 420efd40-d4b4-4bf7-8c98-fcecfb16836f"
model="gpt-4o-mini"

messages = [
    {"role": "user", "content": "Hi"},
]
result = litellm.completion(
    model=model,
    api_key=api_key,
    messages=messages,
    base_url=base_url,
    temperature=0.01,
)

print(result)
