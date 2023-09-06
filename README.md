# etl_pipeline_python_generative_ai

Recebi a tarefa de envolver meus clientes de maneira mais personalizada. O objetivo é usar o poder da IA Generativa para criar mensagens de marketing personalizadas que serão entregues a cada cliente de forma personalizada buscando mais engajamento.

## 1.11.9 Entregar Projeto

### Configuração inicial ambiente de desenvolvimento

## 1.11.9 Entregar Projeto

### Configuração inicial ambiente de desenvolvimento

-[x]  venv
    
    Crie o ambiente: `python -m venv .venv`
    
    Ative o ambiente:  `.venv\Scripts\activate`
    
-[x]  .gitignore
    - Code
        
        ```python
        # Environments
        .env
        .venv
        env/
        venv/
        ENV/
        env.bak/
        venv.bak/
        ```
        
-[x]  Arquivo CSV id clientes
    - Arquivo
        -[x]  [Arquivo com ids dos clientes](https://www.notion.so/Arquivo-com-ids-dos-clientes-c8399a97039e4897af9feb1adb627a0e?pvs=21)
-[x]  `pip install python-decouple`
-[x]  `pip install pandas`
-[x]  `pip install openai`
-[x]  .env
    - Code
        
        ```python
        BANK_API_URL="api_url"
        ```
        
-[x]  global_configs

```python
from decouple import config

API_URL = config(BANK_API_URL) or config('API_URL')
```

### Desenvolvimento

-[x]  [1.11.4 Extract (Extração)](https://www.notion.so/1-11-4-Extract-Extra-o-40279b80ba94494f9a7a7c56c3e5b6c0?pvs=21)
-[x]  [1.11.5 Transform (Transformação ou Enriquecimento)](https://www.notion.so/1-11-5-Transform-Transforma-o-ou-Enriquecimento-9584b2829f2942f983c00d093682bd29?pvs=21)
-[x]  [1.11.6 Load (Carregamento)](https://www.notion.so/1-11-6-Load-Carregamento-e10f93ea04da41e788da3cd9d0cdcd22?pvs=21)  venv
    
    Crie o ambiente: `python -m venv .venv`
    
    Ative o ambiente:  `.venv\Scripts\activate`
    
-[x]  .gitignore
    - Code
        
        ```python
        # Environments
        .env
        .venv
        env/
        venv/
        ENV/
        env.bak/
        venv.bak/
        ```
        
-[x]  Arquivo CSV id clientes
    - Arquivo
        -[x]  [Arquivo com ids dos clientes](https://www.notion.so/Arquivo-com-ids-dos-clientes-c8399a97039e4897af9feb1adb627a0e?pvs=21)
-[x]  `pip install python-decouple`
-[x]  `pip install pandas`
-[x]  `pip install openai`
-[x]  .env
    - Code
        
        ```python
        BANK_API_URL="api_url"
        ```
        
-[x]  global_configs

```python
from decouple import config

API_URL = config(BANK_API_URL) or config('API_URL')
```

### Desenvolvimento

-[x]  [1.11.4 Extract (Extração)](https://www.notion.so/1-11-4-Extract-Extra-o-40279b80ba94494f9a7a7c56c3e5b6c0?pvs=21)
-[x]  [1.11.5 Transform (Transformação ou Enriquecimento)](https://www.notion.so/1-11-5-Transform-Transforma-o-ou-Enriquecimento-9584b2829f2942f983c00d093682bd29?pvs=21)
-[x]  [1.11.6 Load (Carregamento)](https://www.notion.so/1-11-6-Load-Carregamento-e10f93ea04da41e788da3cd9d0cdcd22?pvs=21)