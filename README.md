# Nocode API BR

Estrutura inicial de um aplicativo Python seguindo boas praticas. O projeto utiliza FastAPI como framework web e inclui configuracoes para conteinerizacao com Docker.

## Como iniciar

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Instale as dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o servidor de desenvolvimento:
   ```bash
   uvicorn app.main:app --reload
   ```

## Estrutura de pastas

- `app/` codigo fonte do aplicativo
- `Dockerfile` imagem base para execucao
- `.env` variaveis de ambiente de desenvolvimento
- `requirements.txt` dependencias do projeto
- `pyproject.toml` metadados e ferramentas de build

## Testes

Execute os testes com:

```bash
pytest
```
