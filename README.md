# 📊 Projeto MLOps - Previsão de preços de diamantes

## 👤 Desenvolvedor: Mateus Zambello

---

## 📋 Resumo do Projeto

Aplicação de Machine Learning para previsão de preços de diamantes utilizando:
- **Modelagem**: Scikit-learn (Random Forest)
- **Frontend**: Streamlit
- **Versioning**: Git
- **Containerização**: Docker
- **Tracking**: MLflow

---

## 🎯 Funcionalidades Implementadas

### ✅ Código Base
- [x] Módulo de dados (`src/data.py`)
- [x] Módulo de modelo (`src/model.py`)
- [x] Módulo de avaliação (`src/evaluate.py`)
- [x] Script de treinamento (`train.py`)
- [x] Testes automatizados (`tests/`)

### ✅ Interface Web (Streamlit)
- [x] **Personalização do App**:
  - ✨ Nome do desenvolvedor: **Mateus Zambello**
  - 🎨 Tema com cores verdes personalizadas
  - 💎 Logo/Imagem adicionada (`app/img/diamond-logo.jpg`)
  - © Copyright: "© 2026 Diamond Price Predictor - Desenvolvido por Mateus Zambello"

### ✅ Features do App
- [x] Entrada de 9 parâmetros do diamante
- [x] Layout em 3 colunas para melhor UX
- [x] Botão de predição com spinner
- [x] Resultado destacado em verde
- [x] Footer com informações do desenvolvedor

### ✅ Deployment
- [x] Dockerfile configurado
- [x] Docker Compose com orquestração
- [x] MLflow local para tracking

---

## 🚀 Como Executar

### 1️⃣ Preparar Ambiente
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente
.venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
```

### 2️⃣ Treinar Modelo
```bash
python train.py
```

### 3️⃣ Executar Streamlit (Local)
```bash
streamlit run app/streamlit_app.py
```
Abre em: `http://localhost:8501`

### 4️⃣ Executar com Docker
```bash
docker compose up --build
```
Acesso: `http://localhost:8501`

### 5️⃣ Rodar Testes
```bash
pytest
```

---

## 📁 Estrutura do Projeto

```
mlops/
├── app/
│   ├── streamlit_app.py          # App principal com personalização
├── src/
│   ├── __init__.py
│   ├── data.py                   # Carregamento e split de dados
│   ├── model.py                  # Construção do pipeline
│   └── evaluate.py               # Métricas de avaliação
├── tests/
│   ├── __init__.py
│   ├── test_data.py
│   ├── test_model.py
│   └── test_train.py
├── models/
│   └── diamond_price_model.joblib  # Modelo treinado
├── notebooks/
│   └── EDA_diamond.ipynb           # Análise exploratória
├── train.py                        # Script de treinamento
├── requirements.txt                # Dependências
├── Dockerfile                      # Container do app
├── docker-compose.yml              # Orquestração
└── pytest.ini                      # Config dos testes
```

---

## 🎨 Personalização do App

### Configurações Aplicadas:

#### 1. **Tema Streamlit** (`~/.streamlit/config.toml`)
```toml
[theme]
primaryColor = "#2ecc71"              # Verde
backgroundColor = "#0d3b0d"           # Verde escuro
secondaryBackgroundColor = "#1a5c1a"  # Verde secundário
textColor = "#ffffff"                 # Branco
```

#### 2. **CSS Personalizado**
- Botões com gradiente verde
- Títulos em verde com sombra
- Layout responsivo em 3 colunas
- Footer com copyright

#### 3. **Header Customizado**
```
💎 Previsão de preços de diamantes 💎
🧑‍💼 Desenvolvido por: Mateus Zambello
Modelo para previsão de preços de diamantes
```

#### 5. **Footer**
```
© 2026 Diamond Price Predictor - Desenvolvido por Mateus Zambello
📊 MLOps Project | 🎓 Modelo de Machine Learning para Previsão de Preços
```

---

### Interface
- ✅ Fundo verde personalizado
- ✅ Título e nome do desenvolvedor visível
- ✅ Logo exibida no header
- ✅ Botão verde funcional
- ✅ Resultado em destaque
- ✅ Copyright no footer

---

## 🔄 Histórico de Commits

Para visualizar o histórico completo de commits:

```bash
git log --oneline
```

**Commits principais:**
```
- Personalização do Streamlit com tema verde
- Adição de logo e footer com copyright
- Configuração do ambiente virtual
- Instalação de dependências
- Implementação do modelo
- Testes automatizados
```

---

## ✅ Checklist de Entrega

- [x] Código versionado no Git
- [x] Ambiente configurado e funcionando
- [x] App personalizado com nome do desenvolvedor
- [x] Tema com cores verdes
- [x] Logo adicionada
- [x] Footer com copyright
- [x] Modelo treinado e salvo
- [x] Testes passando
- [x] Docker configurado
- [x] Documentação completa

---

## 📝 Notas Importantes

- O modelo é salvo em `models/diamond_price_model.joblib`
- MLflow local em `mlruns/`
- Cache do Streamlit em `~/.streamlit/cache`
- Certifique-se de estar no `.venv` antes de rodar comandos

---

## 🤝 Contato

**Desenvolvedor:** Mateus Zambello  
**Projeto:** MLOps - Diamond Price Predictor  
**Data:** Fevereiro de 2026  
**Repositório:** GitHub (mrzambello/mlops)

---

## 📚 Recursos Utilizados

- Python 3.13
- Scikit-learn 1.8.0
- Streamlit 1.52.1
- Pandas 2.3.3
- Joblib 1.5.3
- MLflow 3.7.0
- Docker & Docker Compose
- Pytest 9.0.2
