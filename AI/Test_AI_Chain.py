import ollama


user_text0 = input("Enter your text: ")

def get_prompt(user_text):
    prompt = f"""ONLY rewrite this question: {user_text}"""
    return prompt



def first_response(user_text1):
    response = ollama.generate("tinyllama", get_prompt(user_text1))
    print(1)
    print(response['response'])
    return response['response']
def second_response(user_text2):
    response = ollama.generate("phi", get_prompt(first_response(user_text2)))
    print(2)
    print(response['response'])
    return response['response']
def third_response(user_text3):
    response = ollama.generate("deepseek-r1", second_response(user_text3))
    return response['response']


#testing
print(third_response(user_text0))

#TINYLLAMA HAS TOO MUCH HALLUCINATIONS.