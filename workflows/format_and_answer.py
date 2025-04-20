from providers.openai_provider import chat_with_openai

async def run(input):
    formatted = await chat_with_openai([
        {"role": "system", "content": "請將問題轉為有條理、清楚格式"},
        {"role": "user", "content": input["question"]}
    ])
    formatted_text = formatted['choices'][0]['message']['content']

    answer = await chat_with_openai([
        {"role": "system", "content": "根據問題與資料提供回答"},
        {"role": "user", "content": f"{formatted_text}\n\n資料：{input['context']}"}
    ])
    return {
        "formatted_question": formatted_text,
        "answer": answer['choices'][0]['message']['content']
    }