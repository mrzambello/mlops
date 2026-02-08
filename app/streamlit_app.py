import joblib
import pickle
import pandas as pd
import streamlit as st
import mlflow
import mlflow.pyfunc
import os

st.set_page_config(
    page_title="Previsão de preço de diamantes - Mateus Zambello",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #0d3b0d 0%, #1a5c1a 100%);
    }
    .stButton>button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 28px;
        transition: all 0.3s;
        border: 2px solid #27ae60;
    }
    .stButton>button:hover {
        background-color: #27ae60;
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(46, 204, 113, 0.3);
    }
    h1 {
        color: #2ecc71;
        text-align: center;
        font-size: 2.8em;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.5);
        font-weight: bold;
    }
    h2 {
        color: #2ecc71;
        font-weight: bold;
    }
    h3 {
        color: #58d68d;
    }
    .header-container {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, rgba(46, 204, 113, 0.1), rgba(39, 174, 96, 0.1));
        border-radius: 15px;
        margin-bottom: 20px;
        border: 2px solid #2ecc71;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin: 15px 0;
    }
    .logo-container img {
        max-height: 100px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(46, 204, 113, 0.3);
    }
    .footer {
        text-align: center;
        padding: 20px;
        border-top: 2px solid #2ecc71;
        color: #a0a0a0;
        font-size: 0.9em;
        margin-top: 40px;
        background: rgba(46, 204, 113, 0.05);
        border-radius: 10px;
    }
    div[data-testid="stNumberInput"] label,
    div[data-testid="stSelectbox"] label {
        color: #2ecc71 !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    model_uri = "models:/diamonds_price_model@champion"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

@st.cache_resource
def load_model_local():
    model_path = "models/model.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.markdown("""
        <div class='header-container'>
            <h1>Previsão de preço de diamantes</h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
            <p style='font-size: 1.3em; color: #2ecc71; margin: 10px 0;'>
                <strong>Desenvolvido por: Mateus Zambello</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.write("Modelo treinado com o dataset `diamonds` do seaborn.")

    model = load_model_local()

    st.subheader("📊 Informe as características do diamante")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        carat = st.number_input("Quilates (carat)", min_value=0.0, max_value=5.0, value=0.5, step=0.01)
        depth = st.number_input("Profundidade (depth)", min_value=40.0, max_value=80.0, value=61.5, step=0.1)
        table = st.number_input("Tabela (table)", min_value=40.0, max_value=80.0, value=57.0, step=0.1)
    
    with col2:
        x = st.number_input("Comprimento (x)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
        y = st.number_input("Largura (y)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
        z = st.number_input("Altura (z)", min_value=0.0, max_value=15.0, value=3.0, step=0.1)
    
    with col3:
        cut = st.selectbox("Corte (cut)", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
        color = st.selectbox("Cor (color)", ["D", "E", "F", "G", "H", "I", "J"])
        clarity = st.selectbox(
            "Claridade (clarity)",
            ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"],
        )
    
    st.markdown("---")

    if st.button("Prever preço", use_container_width=True):
        with st.spinner("Calculando o valor do diamante..."):
            data = pd.DataFrame(
                {
                    "carat": [float(carat)],
                    "depth": [float(depth)],
                    "table": [float(table)],
                    "x": [float(x)],
                    "y": [float(y)],
                    "z": [float(z)],
                    "cut": [str(cut)],
                    "color": [str(color)],
                    "clarity": [str(clarity)],
                }
            )


            num_cols = ["carat", "depth", "table", "x", "y", "z"]
            data[num_cols] = data[num_cols].astype(float)

            cat_cols = ["cut", "color", "clarity"]
            data[cat_cols] = data[cat_cols].astype(str)

            EXPECTED_COLUMNS = [
                "carat",
                "depth",
                "table",
                "x",
                "y",
                "z",
                "cut",
                "color",
                "clarity",
            ]

            data = data[EXPECTED_COLUMNS]

            prediction = model.predict(data)[0]

            st.markdown("---")
            st.success("Previsão concluída!")
            
            st.markdown(f"""
                <div style='text-align: center; padding: 30px; background-color: rgba(46, 204, 113, 0.15); border-radius: 15px; margin: 20px 0; border: 2px solid #2ecc71;'>
                    <h2 style='color: #2ecc71; margin: 0;'>Preço Estimado</h2>
                    <h1 style='color: #58d68d; font-size: 3.5em; margin: 10px 0;'>${prediction:,.2f}</h1>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class='footer'>
            <p>© 2026 Previsão de preço de diamantes - Desenvolvido por <strong>Mateus Zambello</strong></p>
            <p>MLOps Projeto | Modelo para Previsão de Preços</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
