import streamlit as st

st.image("neurona.jpg", width=300)

st.header("¡Hola neurona!")

tabs = ["Una entrada", "Dos entradas", "Tres entradas y sesgo"]

tab1, tab2, tab3 = st.tabs(tabs)

# Primera ventana (Una entrada)
tab1.markdown('<h1 style="font-size:25px;">Una neurona con una entrada y un peso</h1>', unsafe_allow_html=True)

# Recogida de datos de la primera ventana
col1, col2 = tab1.columns(2)
with col1:
    tab1_w = st.slider("Peso", 0.0, 5.0)
with col2:
    tab1_x = st.number_input("Introduzca el valor de la entrada")

# Cálculo de la salida y presentación de resultados
salida1 = tab1_x * tab1_w
if tab1.button("Calcular la salida", key="button1"):
    tab1.text(f"La salida de la neurona es {salida1}")

# Segunda ventana (Dos entradas)
tab2.markdown('<h1 style="font-size:25px;">Una neurona con dos entradas y dos pesos</h1>', unsafe_allow_html=True)

# Recogida de datos de la segunda ventana
col1, col2 = tab2.columns(2)
with col1:
    tab2_w0 = st.slider("Peso w₀", 0.0, 5.0, key="tab2 w0")
    tab2_x0 = st.number_input("Entrada x₀", key="tab2 x0")
with col2:
    tab2_w1 = st.slider("Peso w₁", 0.0, 5.0, key="tab2 w1")
    tab2_x1 = st.number_input("Entrada x₁", key="tab2 x1")

# Cálculo de la salida y presentación de resultados
salida2 = tab2_x0 * tab2_w0 + tab2_x1 * tab2_w1
if tab2.button("Calcular la salida", key="button2"):
    tab2.text(f"La salida de la neurona es {salida2}")

# Tercera ventana (Tres entradas y sesgo)
tab3.markdown('<h1 style="font-size:25px;">Una neurona con tres entradas, tres pesos y un sesgo</h1>', unsafe_allow_html=True)

# Recogida de datos de la tercera ventana
col1, col2, col3 = tab3.columns(3)
with col1:
    tab3_w0 = st.slider("Peso w₀", 0.0, 5.0, key="tab3 w0")
    tab3_x0 = st.number_input("Entrada x₀", key="tab3 x0")
with col2:
    tab3_w1 = st.slider("Peso w₁", 0.0, 5.0, key="tab3 w1")
    tab3_x1 = st.number_input("Entrada x₁", key="tab3 x1")
with col3:
    tab3_w2 = st.slider("Peso w₂", 0.0, 5.0, key="tab3 w2")
    tab3_x2 = st.number_input("Entrada x₂", key="tab3 x2")

tab3_b = tab3.number_input("Introduzca el valor del sesgo")

# Cálculo de la salida y presentación de resultados
salida3 = tab3_x0 * tab3_w0 + tab3_x1 * tab3_w1 + tab3_x2 * tab3_w2 + tab3_b
if tab3.button("Calcular la salida", key="button3"):
    tab3.text(f"La salida de la neurona es {salida3}")
