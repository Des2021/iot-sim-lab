# IoT Sim Lab – MQTT + Streamlit

Simulación de sensores IoT publicando datos por MQTT y visualización en Streamlit.

## 🚀 Ejecución local
```bash
python -m venv .venv
source .venv/bin/activate   # o .\\.venv\\Scripts\\activate en Windows
pip install -r requirements.txt

cp .env.example .env
python -m src.publisher
python -m src.subscriber_plot

