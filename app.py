import streamlit as st

# CONFIGURAÇÕES DO SEU CLIO
GASOLINA = 6.19
CONSUMO = 10  # km/L

st.set_page_config(
    page_title="Analisador Lalamove",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Analisador Lalamove")
st.caption("Descubra rapidamente se uma corrida vale a pena.")

st.divider()

with st.expander("⚙️ Configurações"):
    st.write(f"⛽ Gasolina: **R$ {GASOLINA:.2f}/L**")
    st.write(f"🚗 Consumo do Clio: **{CONSUMO} km/L**")

st.subheader("📋 Dados da corrida")

# VALOR
valor = st.number_input(
    "💰 Valor da corrida (R$)",
    min_value=0.0,
    step=1.0,
    format="%.2f"
)

# KM TOTAL
km_total = st.number_input(
    "📏 Km total da corrida",
    min_value=0.0,
    step=0.5,
    format="%.1f"
)

# TEMPO
tempo = st.number_input(
    "⏱️ Tempo total (minutos)",
    min_value=5.0,
    step=5.0
)

st.write("")

if st.button("🔎 ANALISAR CORRIDA", use_container_width=True):

    litros = km_total / CONSUMO
    custo_combustivel = litros * GASOLINA

    lucro = valor - custo_combustivel

    horas = tempo / 60

    reais_por_km = lucro / km_total if km_total > 0 else 0
    reais_por_hora = lucro / horas if horas > 0 else 0

    # DECISÃO
    if reais_por_hora >= 30 and reais_por_km >= 1.50:
        status = "🟢 PEGA"
        mensagem = "Essa corrida está boa!"
    elif reais_por_hora >= 20:
        status = "🟡 ANALISA"
        mensagem = "Pode valer a pena. Analise trânsito e região."
    else:
        status = "🔴 NÃO PEGA"
        mensagem = "Essa corrida está fraca."

    st.divider()

    st.subheader("Resultado")

    st.markdown(
        f"""
        <div style="
            padding: 25px;
            border-radius: 15px;
            border: 2px solid #ddd;
            text-align: center;
            margin-bottom: 20px;
        ">
            <h1>{status}</h1>
            <p style="font-size:18px;">{mensagem}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("💵 Lucro líquido", f"R$ {lucro:.2f}")
        st.metric("⛽ Combustível", f"R$ {custo_combustivel:.2f}")
        st.metric("📏 Km total", f"{km_total:.1f} km")

    with col2:
        st.metric("💰 R$/hora", f"R$ {reais_por_hora:.2f}")
        st.metric("🚗 R$/km", f"R$ {reais_por_km:.2f}")
        st.metric("⛽ Litros", f"{litros:.2f} L")

    st.divider()

    st.caption(
        f"Clio: {CONSUMO} km/L • Gasolina: R$ {GASOLINA:.2f}/L"
    )