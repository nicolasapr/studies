import pandas as pd
from langchain_community.llms import Ollama
import os

def load_data(file_path):
    """
    Carrega e limpa os dados do CSV
    """
    try:
        df = pd.read_csv(file_path)
        df = df.dropna()
        df = df.drop_duplicates()
        return df.reset_index(drop=True)
    except FileNotFoundError:
        print(f"Erro: Arquivo {file_path} não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return None

def analyze_data(df):
    """
    Analisa os dados usando o modelo Ollama
    """
    try:
        # Inicializar o modelo
        llm = Ollama(model="llama2")
        
        # Preparar os dados para análise
        data_info = f"""
        Resumo estatístico:
        {df.describe().to_string()}
        
        Primeiras linhas:
        {df.head().to_string()}
        """
        
        # Criar prompt para análise
        prompt = f"""
        Analise os seguintes dados e forneça insights importantes:
        {data_info}
        
        Por favor, forneça:
        1. Principais tendências
        2. Estatísticas relevantes
        3. Possíveis correlações
        4. Recomendações baseadas nos dados
        """
        
        # Gerar análise
        response = llm.invoke(prompt)
        return response
    
    except Exception as e:
        print(f"Erro durante a análise: {str(e)}")
        return None

def main():
    # Caminho do arquivo
    file_path = "Python/testes.csv"
    
    # Carregar dados
    print("Carregando dados...")
    df = load_data(file_path)
    
    if df is not None:
        print("\nIniciando análise...")
        analysis = analyze_data(df)
        
        if analysis:
            print("\nResultados da Análise:")
            print(analysis)
        else:
            print("Não foi possível completar a análise.")
    else:
        print("Não foi possível carregar os dados.")

if __name__ == "__main__":
    main()
