# Agente Especialista de Games

Aplicação que recomenda um jogo conforme o gênero, a plataforma e o nível de hardware escolhidos.

## Acesse o app online

**[Abrir Agente Especialista de Games](https://agente-especialista-de-games.streamlit.app/)**

## Executar pelo VS Code

### 1. Prepare o VS Code

Instale o [Python 3](https://www.python.org/downloads/) e o [Visual Studio Code](https://code.visualstudio.com/). No VS Code, abra **Extensions** e instale a extensão **Python**, publicada pela Microsoft.

### 2. Coloque o projeto no VS Code

Escolha uma das duas formas:

**Opção A — Clonar pelo VS Code**

1. Abra o VS Code e pressione **Ctrl+Shift+P** (no macOS, **Cmd+Shift+P**).
2. Digite e selecione **Git: Clone**.
3. Cole o endereço do repositório:

   ```
   https://github.com/oGusta-dev/Agente-Especialista-de-Games.git
   ```

4. Escolha onde salvar o projeto e, quando o VS Code perguntar, selecione **Open**.

**Opção B — Baixar pelo GitHub e abrir manualmente**

1. Abra o [repositório no GitHub](https://github.com/oGusta-dev/Agente-Especialista-de-Games).
2. Clique em **Code > Download ZIP** e extraia o arquivo baixado.
3. No VS Code, selecione **File > Open Folder** e abra a pasta extraída que contém os arquivos `interface.py`, `main.py` e `database.py`.

### 3. Crie o ambiente Python

No VS Code, pressione **Ctrl+Shift+P** (no macOS, **Cmd+Shift+P**), procure **Python: Create Environment**, selecione **Venv** e escolha uma instalação do Python. O VS Code criará o ambiente `.venv` para este projeto.

### 4. Instale e inicie o app

No VS Code, abra **Terminal > New Terminal**. No terminal integrado, execute:

```bash
python -m pip install streamlit
python -m streamlit run interface.py
```

Quando o Streamlit iniciar, abra [http://localhost:8501](http://localhost:8501) no navegador, se ele não abrir automaticamente. Para encerrar o app, volte ao terminal integrado e pressione **Ctrl+C**.

### 5. Como usar

1. Escolha um gênero: **RPG de Aventura**, **Corrida** ou **Tiro**.
2. Escolha uma plataforma: **PC**, **Console** ou **Mobile**.
3. Escolha **Leve** ou **Pesado**.
4. Clique em **Buscar Jogo**.

## Arquivos do projeto

- `interface.py`: tela e opções de seleção.
- `main.py`: busca o jogo correspondente às opções escolhidas.
- `database.py`: catálogo e informações dos jogos.

Para cadastrar jogos, edite `database.py`. Se criar novas opções de gênero, plataforma ou hardware, atualize também os seletores em `interface.py`.
