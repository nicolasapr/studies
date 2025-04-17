import ollama
import pandas as pd
import time

try:
    df_benchmark = pd.read_csv("csqa_dev_processed.csv")
    df_benchmark = df_benchmark.dropna()
    print(df_benchmark.columns)
except FileNotFoundError:
    print("Erro: Arquivo benchmark não encontrado.")
    exit(1)

def model(question, choices):
    response = ollama.chat(
        model="tinyllama",
        messages=[{
            "role": "user",
            "content": make_prompt(question, choices)
        }]
    )
    return response['message']['content'].strip()

def make_prompt(question, choices):  
    return f"""You are taking a multiple choice test. For the following question, select the EXACT text of the best answer from the given choices.

Question: {question}

Available choices:
{choices}

Important: Your response must be EXACTLY one of the choices provided above, with no additional text or explanation. Copy and paste the correct choice."""

def evaluate_model(model, df):
    results = []
    for index, row in df.iterrows():
        try:
            question = row['question']
            choices = row['choices']
            answer = row['answer_text']
            response = model(question, choices)
            
            #only for debug
            print(f"\nQuestion {index + 1}: {question}")
            print(f"Choices: {choices}")
            print(f"Expected: {answer}")
            print(f"Got: {response}")
            if response.strip().lower() in answer.strip().lower():
                print(f"Correct: True")
            else:
                print(f"Correct: False")
            
            results.append({
                'question': question,
                'choices': choices,
                'expected_answer': answer,
                'model_response': response,
                'correct': response.strip().lower() == answer.strip().lower()
            })
            
            print(f"Processed question {index + 1}/{len(df)}")
        except Exception as e:
            print(f"Error on {index}: {str(e)}")
            continue
            
    return pd.DataFrame(results)

try:
    csv_evaluation = evaluate_model(model, df_benchmark)
    csv_evaluation.to_csv("evaluation_tinyllama.csv", index=False)
    print("Finish")
except Exception as e:
    print(f"Final Error on: {str(e)}")
