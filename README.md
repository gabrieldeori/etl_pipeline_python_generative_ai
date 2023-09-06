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
        -[x]  [Arquivo com ids dos clientes]()
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

-[x]  [1.11.4 Extract (Extração)]()
-[x]  [1.11.5 Transform (Transformação ou Enriquecimento)]()
-[x]  [1.11.6 Load (Carregamento)](v
    
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
        -[x]  [Arquivo com ids dos clientes]()
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

-[x]  [1.11.4 Extract (Extração)]()
-[x]  [1.11.5 Transform (Transformação ou Enriquecimento)]()
-[x]  [1.11.6 Load (Carregamento)]()