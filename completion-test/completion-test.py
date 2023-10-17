import openai
import os
import json

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

input1 = ""

messages1=[
    {"role": "system", "content": "Pergunte algo ao Chatbot da UCS."}
]

while (input1 != "q"):
    print("Digite uma entrada, para sair digite 'q':")
    input1 = input()
    if(input1 != "q"):
        messages1.append({"role": "user", "content": input1})
        response = openai.ChatCompletion.create(
            model="ft:gpt-3.5-turbo-0613:personal::81NwI1HE",
            messages=messages1,
            max_tokens = 100,
            temperature = 0.2
        )
        y = response["choices"][0]["message"]
        messages1.append({"role": "assistant", "content": y["content"]})
        os.system('cls')
        print(messages1)



# print(response)