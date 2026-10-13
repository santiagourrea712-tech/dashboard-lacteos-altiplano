import streamlit as st
import pandas as pd
import numpy as np
import base64
import os

# Configuración de la página
st.set_page_config(
    page_title="Executive Dashboard - Lácteos del Altiplano S.A.S.",
    page_icon="📊",
    layout="wide"
)

# Estilo CSS personalizado: Fondo negro unificado, fuente elegante, rojo brillante y enlaces en blanco
st.markdown("""
    <style>
        /* Importar fuente moderna y elegante desde Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&display=swap');

        /* Aplicar la fuente elegante a toda la aplicación */
        .stApp, html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }

        /* Fondo general unificado en NEGRO ABSOLUTO para toda la página */
        .stApp {
            background-color: #000000 !important;
            color: #e0e0e0;
        }
        
        /* Contenedores y tarjetas con borde rojo brillante */
        div[data-testid="stVerticalBlock"] > div[style*="border"] {
            background-color: #121212 !important;
            border: 1px solid #ff1a1a !important;
            border-radius: 8px;
            padding: 20px;
        }
        
        /* Sidebar en NEGRO ABSOLUTO unificado con el fondo */
        section[data-testid="stSidebar"] {
            background-color: #000000 !important;
            border-right: 1px solid #220000;
        }

        /* Forzar que los enlaces de la barra lateral (como el nombre/LinkedIn) sean blancos y estéticos */
        section[data-testid="stSidebar"] a {
            color: #ffffff !important;
            text-decoration: none !important;
            font-weight: 600 !important;
        }
        section[data-testid="stSidebar"] a:hover {
            color: #ff1a1a !important;
            text-decoration: underline !important;
        }
        
        /* Alineación perfecta y vertical de los botones de radio (opciones del menú) */
        div[data-baseweb="radio"] label {
            display: flex !important;
            align-items: center !important;
            gap: 10px;
        }
        div[data-baseweb="radio"] input:checked ~ div {
            background-color: #ff1a1a !important;
            border-color: #ff1a1a !important;
        }
        span[data-baseweb="radio"] div:nth-child(1) {
            border-color: #ff1a1a !important;
        }
        
        /* Cajas de información (st.info y notificaciones) */
        div.stInfo, div[data-baseweb="notification"] {
            background-color: #260000 !important;
            border: 1px solid #ff1a1a !important;
            color: #ffffff !important;
        }
        
        /* Métricas */
        .stMetric {
            background-color: #121212;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #ff1a1a;
        }
        
        /* Pestañas */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #121212;
            border-radius: 4px;
            color: #cccccc;
            border: 1px solid #4d0000;
        }
        .stTabs [aria-selected="true"] {
            background-color: #ff1a1a !important;
            color: white !important;
        }
        
        /* Título lateral grande y llamativo */
        .sidebar-title {
            font-size: 36px !important;
            font-weight: 900;
            color: #ff1a1a;
            line-height: 1.1;
            margin-bottom: 0px;
        }
        .sidebar-subtitle {
            font-size: 20px !important;
            font-weight: 700;
            color: #ffffff;
            margin-top: 4px;
            margin-bottom: 6px;
        }
        
        /* Estilización de Tablas en escala de rojos */
        [data-testid="stDataFrame"] {
            border: 1px solid #ff1a1a;
            border-radius: 8px;
            background-color: #0f0505;
        }
        
        th {
            background-color: #2b0000 !important;
            color: #ff4d4d !important;
            font-weight: bold !important;
            border-bottom: 2px solid #ff1a1a !important;
        }
        
        td {
            background-color: #0f0505 !important;
            color: #e0e0e0 !important;
        }
        
        tr:nth-child(even) td {
            background-color: #170707 !important;
        }
        
        tr:hover td {
            background-color: #260d0d !important;
        }

        /* Estilos visuales optimizados para barras de transferencia de Incoterms */
        .incoterm-bar-container {
            width: 100%;
            background-color: #222;
            border-radius: 6px;
            overflow: hidden;
            display: flex;
            height: 32px;
            margin-top: 8px;
            margin-bottom: 15px;
            border: 1px solid #444;
            font-size: 11px;
            font-weight: bold;
        }
        .seller-part {
            background-color: #8b0000;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            border-right: 2px solid #ff1a1a;
            white-space: nowrap;
            padding: 0 4px;
        }
        .buyer-part {
            background-color: #333;
            color: #bbb;
            display: flex;
            align-items: center;
            justify-content: center;
            white-space: nowrap;
            padding: 0 4px;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado Ejecutivo Principal
st.markdown("## LÁCTEOS DEL ALTIPLANO S.A.S.")
st.markdown("#### *Centro de Control Estratégico: Adquisición de Envasadora Aséptica & Gestión de Riesgos*")
st.markdown("---")

# Función auxiliar para renderizar cualquier imagen local mediante HTML puro
def render_html_image(file_path, width="120px", center=False):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        mime = "image/png" if file_path.endswith(".png") else "image/jpeg"
        
        if center:
            html_tag = f'<div style="text-align: center;"><img src="data:{mime};base64,{encoded}" width="{width}" style="border-radius: 8px; border: 1px solid #ff1a1a; margin-top: 15px; margin-bottom: 15px;"></div>'
        else:
            html_tag = f'<img src="data:{mime};base64,{encoded}" width="{width}" style="border-radius: 6px; margin-bottom: 10px;">'
            
        st.markdown(html_tag, unsafe_allow_html=True)
    else:
        st.warning(f"No se encontró el archivo '{file_path}' en el Escritorio.")

# Menú lateral con etiqueta HTML pura para el logo y enlace a LinkedIn en blanco
with st.sidebar:
    if os.path.exists("logo.png"):
        render_html_image("logo.png", width="120px")
    else:
        render_html_image("logo.jpg", width="120px")
        
    st.markdown('<p class="sidebar-title">Optativa III</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-subtitle">Universidad Libre</p>', unsafe_allow_html=True)
    
    # Nombre con hipervínculo a LinkedIn
    st.markdown("[🔗 Santiago Urrea González](https://www.linkedin.com/in/santiago-urrea-gonz%C3%A1lez-2854a7323)")
    
    st.markdown("---")
    st.markdown("### Módulos de Decisión")
    fase = st.radio(
        "Seleccione el análisis:",
        [
            "1. Diagnóstico Gerencial",
            "2. Análisis de Carga",
            "3. Recomendación de Incoterms",
            "4. Modelado de Plazos & Día 150",
            "5. Evaluación Comparativa (A, B, C)",
            "6. Matriz de Riesgo & Forex",
            "7. TCO y Sensibilidad OEE",
            "8. Resumen Ejecutivo & Recomendación"
        ]
    )
    st.markdown("---")
    st.info("Objetivo: Cumplir el día 150 para evitar penalidad de 20 millones COP/día y asegurar OEE mayor o igual a 8.000 u/h.")

# -------------------------------------------------------------
# FASE 1: DIAGNÓSTICO GERENCIAL
# -------------------------------------------------------------
if fase == "1. Diagnóstico Gerencial":
    st.markdown("### Fase 1: Diagnóstico de Importaciones Históricas")
    st.markdown("Análisis de ineficiencias operativas basadas en las últimas 10 importaciones (Sección 2.5).")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Días en Puerto (Sin Decl. Anticipada)", value="9.1 días", delta="Crítico", delta_color="inverse")
    with col2:
        st.metric(label="Días en Puerto (Con Decl. Anticipada)", value="3.0 días", delta="-6.1 días", delta_color="inverse")
    with col3:
        st.metric(label="Sobrecostos por Demoras Acumuladas", value="$6,300 USD", delta="Evitable", delta_color="inverse")

    st.markdown("#### Registro Detallado de Operaciones Anteriores")
    df_diag = pd.DataFrame({
        "#": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Origen": ["Alemania", "China", "México", "Italia", "China", "EE. UU.", "China", "Alemania", "España", "China"],
        "Término": ["EXW", "FOB", "DAP", "EXW", "CFR", "FCA", "FOB", "EXW", "CIF", "FOB"],
        "Valor FOB (USD)": ["$38,000", "$22,500", "$41,000", "$17,800", "$29,000", "$12,400", "$35,600", "$26,300", "$19,700", "$31,200"],
        "Decl. Ant.": ["No", "No", "No", "Sí", "No", "Sí", "No", "No", "Sí", "No"],
        "Demoras (USD)": ["$1,080", "$360", "$1,440", "$0", "$720", "$0", "$180", "$1,800", "$180", "$540"],
        "Novedad Principal": [
            "Falta trámite exportación proveedor", "Ninguna", 
            "Ajuste DIAN por flete no discriminado", "Ninguna", 
            "Avería sin póliza del comprador", "Ninguna", 
            "Ninguna", "Carga retenida en origen", 
            "Seguro ICC(C) insuficiente", "Ninguna"
        ]
    })
    st.dataframe(df_diag, use_container_width=True, hide_index=True)

    with st.container(border=True):
        st.markdown("#### Conclusión del Diagnóstico")
        st.markdown("La compañía padece una **vulnerabilidad sistémica** debido al uso excesivo de términos EXW sin control de origen, ausencia de declaración anticipada obligatoria y contratación de seguros básicos (ICC-C) que no cubren daños por manipulación.")

# -------------------------------------------------------------
# FASE 2: ANÁLISIS DE TIPO Y NATURALEZA DE LA CARGA
# -------------------------------------------------------------
elif fase == "2. Análisis de Carga":
    st.markdown("### Fase 2: Análisis de Tipo y Naturaleza de la Carga")
    st.markdown("Caracterización técnica de la envasadora aséptica y requerimientos especiales de manipulación logística.")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### Requerimientos Físicos y Sensibilidad")
            st.markdown("""
            * **Naturaleza:** Maquinaria industrial de alta precisión y componentes electrónicos delicados.
            * **Sensibilidad:** Altamente sensible a impactos mecánicos, humedad y vibraciones excesivas durante el tránsito internacional.
            * **Dimensiones y Peso:** Carga pesada y sobredimensionada que requiere contenedores especiales (Open Top o Flat Rack) o manejo cuidadoso en consolidación marítima/terrestre.
            """)
    with col2:
        with st.container(border=True):
            st.markdown("#### Implicaciones Logísticas")
            st.markdown("""
            * **Izaje y Maniobras:** Exige supervisión técnica especializada en puertos y planta para evitar daños estructurales (evitar pérdidas de hasta 60,000 USD).
            * **Cobertura de Seguro:** Inadmisible usar pólizas básicas ICC(C); se requiere obligatoriamente **ICC(A)** contra todo riesgo de daños materiales.
            * **Cadena de Suministro:** Requiere un operador logístico con experiencia en proyectos industriales pesados (Project Cargo).
            """)
            
    st.markdown("---")
    st.markdown("#### Visualización de Planta & Línea Aséptica")
    if os.path.exists("Planta láctea aséptica en neón rojo.png"):
        render_html_image("Planta láctea aséptica en neón rojo.png", width="100%", center=True)
    elif os.path.exists("Planta láctea aséptica en neón rojo.jpg"):
        render_html_image("Planta láctea aséptica en neón rojo.jpg", width="100%", center=True)
    else:
        render_html_image("planta.png", width="100%", center=True)

# -------------------------------------------------------------
# FASE 3: RECOMENDACIÓN DE INCOTERMS (CON VISUALIZACIÓN)
# -------------------------------------------------------------
elif fase == "3. Recomendación de Incoterms":
    st.markdown("### Fase 3: Recomendación de Términos de Comercio Internacional (Incoterms 2020)")
    st.markdown("Evaluación estratégica y mapeo de transferencia de costos y riesgos entre Vendedor y Comprador.")
    
    tab_inc1, tab_inc2, tab_inc3 = st.tabs(["EXW vs FCA (Origen)", "CFR/CIF vs CIP (Tránsito)", "DAP vs DPU (Destino)"])
    
    with tab_inc1:
        with st.container(border=True):
            st.markdown("#### EXW (En Fábrica)")
            st.markdown('<div class="incoterm-bar-container"><div class="seller-part" style="width: 15%;">VEND. 10%</div><div class="buyer-part" style="width: 85%;">COMPRADOR 90% (Riesgo en origen)</div></div>', unsafe_allow_html=True)
            st.markdown("* **Evaluación:** Desaconsejado. El comprador asume todos los riesgos y trámites de exportación en país origen.")
            
            st.markdown("---")
            st.markdown("#### FCA (Franco Transportista) — RECOMENDADO")
            st.markdown('<div class="incoterm-bar-container"><div class="seller-part" style="width: 30%;">VENDEDOR 30% (Despachado Exp.)</div><div class="buyer-part" style="width: 70%;">COMPRADOR 70%</div></div>', unsafe_allow_html=True)
            st.markdown("* **Evaluación:** **Ideal para Lácteos del Altiplano**. El proveedor asume el despacho aduanero de exportación en origen y entrega al transportista elegido por el comprador.")

    with tab_inc2:
        with st.container(border=True):
            st.markdown("#### CIF / CFR (Cost, Insurance and Freight)")
            st.markdown('<div class="incoterm-bar-container"><div class="seller-part" style="width: 50%;">VENDEDOR 50% (Puerto Carga)</div><div class="buyer-part" style="width: 50%;">COMPRADOR 50%</div></div>', unsafe_allow_html=True)
            st.markdown("* **Evaluación:** Riesgoso en carga marítima multimodal. Históricamente causó errores de facturación 'CIF Bogotá'.")
            
            st.markdown("---")
            st.markdown("#### CIP (Carriage and Insurance Paid to) — RECOMENDADO MULTIMODAL")
            st.markdown('<div class="incoterm-bar-container"><div class="seller-part" style="width: 80%;">VENDEDOR 80% (Incluye Seguro ICC-A)</div><div class="buyer-part" style="width: 20%;">COMPRADOR 20%</div></div>', unsafe_allow_html=True)
            st.markdown("* **Evaluación:** **Excelente para China/Europa**. Exige al vendedor contratar póliza ICC(A) 'A todo riesgo' protegiendo el equipo hasta el puerto/terminal acordado.")

    with tab_inc3:
        with st.container(border=True):
            st.markdown("#### DAP / DPU (Delivered at Place)")
            st.markdown('<div class="incoterm-bar-container"><div class="seller-part" style="width: 90%;">VENDEDOR 90% (Entrega en Planta)</div><div class="buyer-part" style="width: 10%;">COMPRADOR 10%</div></div>', unsafe_allow_html=True)
            st.markdown("* **Evaluación:** El vendedor asume el transporte hasta Tocancipá. Sin embargo, incrementa significativamente el margen de sobreprecio por riesgo del proveedor. Solo viable para México.")

    with st.expander("Ver Matriz Analítica Oficial de Obligaciones Incoterms 2020"):
        st.markdown("Resumen gerencial de la transferencia de riesgos y costos entre vendedor y comprador según las reglas vigentes:")
        df_incoterms_table = pd.DataFrame({
            "Incoterm": ["EXW", "FCA", "FAS", "FOB", "CFR", "CIF", "CPT", "CIP", "DAP", "DPU", "DDP"],
            "Riesgo Principal": ["Fábrica", "Punto convenido", "Puerto carga", "Puerto carga", "Puerto destino", "Puerto destino", "Destino convenido", "Destino convenido", "Destino planta", "Destino descargado", "Destino aduanado"],
            "Transporte Principal": ["Comprador", "Comprador", "Comprador", "Comprador", "Vendedor", "Vendedor", "Vendedor", "Vendedor", "Vendedor", "Vendedor", "Vendedor"],
            "Seguro Opcional/Obligatorio": ["Ninguno", "Ninguno", "Ninguno", "Ninguno", "Ninguno", "Mínimo (ICC-C)", "Ninguno", "Obligatorio (ICC-A)", "Ninguno", "Ninguno", "Ninguno"]
        })
        st.dataframe(df_incoterms_table, use_container_width=True, hide_index=True)

# -------------------------------------------------------------
# FASE 4: MODELADO DE PLAZOS & DÍA 150
# -------------------------------------------------------------
elif fase == "4. Modelado de Plazos & Día 150":
    st.markdown("### Fase 4: Simulación de Plazos y Riesgo Contractual")
    st.markdown("Evaluación estocástica del tiempo de ciclo frente a la fecha límite (Día 150).")
    
    col_sel1, col_sel2 = st.columns([2, 1])
    with col_sel1:
        prov_escogido = st.selectbox("Seleccione la Alternativa de Proveedor:", [
            "Oferta A (Alemania - Maschinenbau Isar GmbH)", 
            "Oferta B (China - Ningbo Hengtai Packaging)", 
            "Oferta C (México - Envasadoras del Bajío)"
        ])
    
    if "Alemania" in prov_escogido:
        fab, trans, puesta = 74.3, 41.0, 14
    elif "China" in prov_escogido:
        fab, trans, puesta = 70.0, 58.5, 28
    else:
        fab, trans, puesta = 44.2, 25.0, 14

    total_ciclo = fab + trans + puesta

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Fabricación Promedio", f"{fab:.1f} días")
    c2.metric("Tránsito & Aduana", f"{trans:.1f} días")
    c3.metric("Puesta en Marcha", f"{puesta} días")
    c4.metric("Ciclo Total (Door-to-Door)", f"{total_ciclo:.1f} días", delta="Límite: 150d", delta_color="off")

    with st.container(border=True):
        if total_ciclo <= 150:
            st.success(f"Viabilidad Alta: El proyecto finaliza en el día **{total_ciclo:.1f}**, cumpliendo holgadamente el plazo contractual con Supermercados Nativa.")
        else:
            retraso_dias = total_ciclo - 150
            st.error(f"Alerta Crítica de Retraso: Se proyectan **{retraso_dias:.1f} días de retraso** sobre el día 150. Penalización esperada: **$ {retraso_dias * 20000000:,.0f} COP**.")

# -------------------------------------------------------------
# FASE 5: EVALUACIÓN COMPARATIVA
# -------------------------------------------------------------
elif fase == "5. Evaluación Comparativa (A, B, C)":
    st.markdown("### Fase 5: Evaluación de Ofertas y Condiciones Contractuales")
    
    tab_a, tab_b, tab_c = st.tabs(["Oferta A: Alemania", "Oferta B: China", "Oferta C: México"])
    
    with tab_a:
        with st.container(border=True):
            st.markdown("#### Maschinenbau Isar GmbH (Múnich)")
            col1, col2 = st.columns(2)
            col1.write("**Capacidad:** 12.000 u/h (OEE: 88%)")
            col1.write("**Plazo Fabricación:** 70 días")
            col2.write("**Alternativas:** FCA Múnich (EUR 410k) vs FCA Hamburgo (EUR 414.8k)")
            st.info("Recomendación Directiva: Contratar **FCA Múnich** y autogestionar el transporte interno europeo para evitar sobreprecios y garantizar el registro REX.")

    with tab_b:
        with st.container(border=True):
            st.markdown("#### Ningbo Hengtai Packaging Machinery")
            col1, col2 = st.columns(2)
            col1.write("**Capacidad:** 10.500 u/h (OEE: 72%)")
            col1.write("**Plazo Fabricación:** 56 días")
            col2.write("**Alternativas:** CIF Bogotá ($295k) / CIP Buenaventura ($297.3k)")
            st.warning("Advertencia Jurídica: 'CIF Bogotá' es un término inadecuado para carga marítima interior. Exigir **CIP Buenaventura** con cobertura ICC(A).")

    with tab_c:
        with st.container(border=True):
            st.markdown("#### Envasadoras del Bajío S.A. de C.V. (Querétaro)")
            col1, col2 = st.columns(2)
            col1.write("**Capacidad:** 10.000 u/h (OEE: 80%)")
            col1.write("**Plazo Fabricación:** 42 días")
            col2.write("**Alternativas:** DAP Tocancipá ($338k) / FCA Querétaro ($310.5k)")
            st.success("Ventaja Logística: Tiempos de tránsito muy cortos, pero requiere validar estrictamente la regla de origen del TLC Colombia-México (contenido regional >= 50%).")

# -------------------------------------------------------------
# FASE 6: MATRIZ DE RIESGO & FOREX
# -------------------------------------------------------------
elif fase == "6. Matriz de Riesgo & Forex":
    st.markdown("### Fase 6: Gestión de Riesgos y Exposición Cambiaria")
    
    with st.container(border=True):
        st.markdown("#### Simulador de Exposición Cambiaria (TRM Base: 4,050 COP/USD)")
        trm_sim = st.slider("Simular TRM de Cierre de Pagos (COP/USD):", 3800.0, 4300.0, 4050.0, 10.0)
        impacto_trm = (trm_sim - 4050.0) * 150000  
        st.metric("Impacto Financiero sobre Saldos Pendientes", f"$ {impacto_trm:,.2f} COP")

    st.markdown("#### Mapa de Riesgos Logísticos Críticos")
    df_riesgos = pd.DataFrame({
        "Evento Crítico": ["Cierre vía Buenaventura-Bogotá", "Cancelación de Zarpes (Asia)", "Daño en Izaje en Planta"],
        "Probabilidad": ["Media (5 eventos/24m)", "Alta (7 de 104 zarpes)", "Baja (1 de 40 maniobras)"],
        "Impacto Estimado": ["Retraso = Días de cierre", "+7 a +14 días de tránsito", "USD 60.000 + 30 días de parada"],
        "Mitigación Recomendada": ["Enrutar carga vía Cartagena", "Booking anticipado (3 semanas)", "Exigir póliza de RC a grúa local"]
    })
    st.dataframe(df_riesgos, use_container_width=True, hide_index=True)

# -------------------------------------------------------------
# FASE 7: TCO Y SENSIBILIDAD OEE
# -------------------------------------------------------------
elif fase == "7. TCO y Sensibilidad OEE":
    st.markdown("### Fase 7: Costo Total de Propiedad (TCO) y Sensibilidad OEE")
    
    col_tco1, col_tco2 = st.columns(2)
    with col_tco1:
        oferta_tco = st.selectbox("Seleccione Oferta para Evaluar TCO:", ["Alemania (FCA Múnich)", "China (CIP Buenaventura)", "México (FCA Querétaro)"])
    with col_tco2:
        tasa_oportunidad = st.number_input("Tasa de Oportunidad Mensual (%):", value=1.5, step=0.1)

    if "Alemania" in oferta_tco:
        base_usd, arancel_pct, oee_val = 446900, 0.05, 88
    elif "China" in oferta_tco:
        base_usd, arancel_pct, oee_val = 297300, 0.05, 72
    else:
        base_usd, arancel_pct, oee_val = 310500, 0.00, 80

    arancel_val = base_usd * arancel_pct
    iva_val = (base_usd + arancel_val) * 0.19
    costo_total_est = base_usd + arancel_val + iva_val + 11500

    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Inversión Base + Tributos (USD)", f"$ {costo_total_est:,.2f}")
    col_m2.metric("Inversión en COP (TRM 4,050)", f"$ {costo_total_est * 4050:,.0f}")
    col_m3.metric("OEE Histórico Evaluado", f"{oee_val}%")

    with st.container(border=True):
        st.markdown("#### Análisis de Sensibilidad OEE & Multas")
        if oee_val < 80:
            st.error(f"Riesgo Operativo Severo: Con un OEE de **{oee_val}%**, la máquina no garantiza las 8,000 u/h mínimas exigidas. Se incurrirá en costos por horas extra de hasta **COP 38.000.000 mensuales**.")
        else:
            st.success(f"Rentabilidad Validada: El OEE de **{oee_val}%** supera el umbral crítico, blindando a la compañía frente a penalidades de capacidad.")

# -------------------------------------------------------------
# FASE 8: RESUMEN EJECUTIVO & RECOMENDACIÓN FINAL
# -------------------------------------------------------------
elif fase == "8. Resumen Ejecutivo & Recomendación":
    st.markdown("### Fase 8: Resumen Ejecutivo y Recomendación Basada en Datos")
    st.markdown("Dictamen directivo consolidado para la toma de decisiones de la gerencia de Lácteos del Altiplano S.A.S.")
    
    with st.container(border=True):
        st.markdown("#### Consolidado de Hallazgos Clave")
        st.markdown("""
        1. **Cumplimiento de Plazos (Día 150):** Las alternativas de Alemania y México cumplen sin riesgo de penalización, mientras que China presenta cuellos de botella críticos en tránsito marítimo que rozan el límite sancionatorio de 20 millones COP diarios.
        2. **Rendimiento Operativo (OEE $\\ge$ 8.000 u/h):** La **Oferta A (Alemania)** destaca con un OEE histórico del 88%, garantizando la productividad exigida por Supermercados Nativa y evitando sobrecostos por horas extra.
        3. **Mitigación Aduanera y Logística:** Es imperativo abandonar el uso de términos EXW y CIF mal aplicados, adoptando **FCA en origen** y **CIP con póliza ICC(A)** para proteger la carga industrial contra daños en izaje y manipulación.
        """)
        
    st.markdown("---")
    st.success("""
    **RECOMENDACIÓN FINAL DE LA CONSULTORÍA:** 
    Se recomienda a la junta directiva seleccionar la **Oferta A (Alemania - Maschinenbau Isar GmbH)** bajo el término **FCA Múnich**. Aunque representa una inversión inicial superior en TCO, su alta eficiencia (OEE 88%), confiabilidad técnica para maquinaria aséptica sensible y cumplimiento holgado del cronograma aseguran la rentabilidad a largo plazo y evitan multas operativas catastróficas.
    """)