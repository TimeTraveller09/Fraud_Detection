import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page configurations
st.set_page_config(
    page_title="UPI Fraud Shield",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium styling
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
    /* CSS background and styling */
    .stApp {
        background-color: #0b0f19;
        color: #e2e8f0;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Header card */
    .header-box {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border-radius: 16px;
        padding: 28px;
        border: 1px solid #334155;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .header-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #6366f1, #3b82f6, #10b981);
    }
    
    /* Custom typography */
    h1, h2, h3 {
        font-family: 'Outfit', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    
    /* Form Section Card */
    .form-container {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(12px);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 24px;
    }

    /* Premium result cards */
    .result-card-fraud {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(239, 68, 68, 0.05));
        border-radius: 16px;
        padding: 28px;
        border: 1px solid rgba(239, 68, 68, 0.4);
        box-shadow: 0 8px 32px 0 rgba(239, 68, 68, 0.15), inset 0 0 12px rgba(239, 68, 68, 0.1);
        margin-top: 20px;
        animation: pulse-red 2s infinite alternate;
    }
    
    .result-card-safe {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(16, 185, 129, 0.05));
        border-radius: 16px;
        padding: 28px;
        border: 1px solid rgba(16, 185, 129, 0.4);
        box-shadow: 0 8px 32px 0 rgba(16, 185, 129, 0.15), inset 0 0 12px rgba(16, 185, 129, 0.1);
        margin-top: 20px;
    }
    
    @keyframes pulse-red {
        0% { box-shadow: 0 8px 32px 0 rgba(239, 68, 68, 0.15); }
        100% { box-shadow: 0 8px 32px 0 rgba(239, 68, 68, 0.25), 0 0 15px rgba(239, 68, 68, 0.15); }
    }

    .metric-card {
        background: rgba(30, 41, 59, 0.55);
        border-radius: 12px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: rgba(255, 255, 255, 0.1);
    }
    
    /* Styled buttons */
    div.stButton > button {
        background: linear-gradient(90deg, #4f46e5, #3b82f6) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.6) !important;
        background: linear-gradient(90deg, #6366f1, #2563eb) !important;
    }
    
    /* Custom Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #080c14;
        border-right: 1px solid #1e293b;
    }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        with open("UPI Fraud Detection updated.pkl", "rb") as f:
            model = pickle.load(f)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Load dataset
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("Sample_DATA.csv")
        # Ensure proper types
        df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y', errors='coerce')
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        return df
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return pd.DataFrame()

model = load_model()
df = load_data()

# Header Section
st.markdown("""
<div class="header-box">
    <h1 style="margin: 0; font-size: 2.5rem; display: flex; align-items: center; gap: 10px;">
        🛡️ UPI Fraud Shield
    </h1>
    <p style="margin: 5px 0 0 0; color: #8b949e; font-size: 1.1rem;">
        Real-time Transaction Fraud Detection & Analytics Dashboard
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.markdown("<h2 style='text-align: center;'>Navigation</h2>", unsafe_allow_html=True)
page = st.sidebar.radio("Go to", ["📊 Dashboard & Analytics", "🔎 Fraud Detector", "📋 View Dataset"])

# Categorical column options (alphabetical order)
TRANSACTION_TYPES = ['Bank Transfer', 'Bill Payment', 'Investment', 'Other', 'Purchase', 'Refund', 'Subscription']
PAYMENT_GATEWAYS = ['Alpha Bank', 'Bank of Data', 'CReditPAY', 'Dummy Bank', 'Gamma Bank', 'Other', 'SamplePay', 'Sigma Bank', 'UPI Pay']
STATES = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat', 'Haryana', 
          'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 
          'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 
          'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
MERCHANT_CATEGORIES = ['Brand Vouchers and OTT', 'Donations and Devotion', 'Financial services and Taxes', 
                       'Home delivery', 'Investment', 'More Services', 'Other', 'Purchases', 'Travel bookings', 'Utilities']

# ----------------- PAGE 1: DASHBOARD & ANALYTICS -----------------
if page == "📊 Dashboard & Analytics":
    st.subheader("System Performance & Dataset Insights")
    
    if not df.empty:
        # Key Metrics Row
        total_txs = len(df)
        fraud_txs = df['fraud'].sum()
        fraud_rate = (fraud_txs / total_txs) * 100
        avg_amount = df['amount'].mean()
        
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""
            <div class="metric-card">
                <span style="color: #8b949e; font-size: 0.9rem;">TOTAL TRANSACTIONS</span>
                <h2 style="margin: 5px 0; color: #58a6ff !important;">{total_txs:,}</h2>
            </div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-card">
                <span style="color: #8b949e; font-size: 0.9rem;">FRAUDULENT CASES</span>
                <h2 style="margin: 5px 0; color: #ff7b72 !important;">{fraud_txs:,}</h2>
            </div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-card">
                <span style="color: #8b949e; font-size: 0.9rem;">OVERALL FRAUD RATE</span>
                <h2 style="margin: 5px 0; color: #ff7b72 !important;">{fraud_rate:.2f}%</h2>
            </div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
            <div class="metric-card">
                <span style="color: #8b949e; font-size: 0.9rem;">AVG TRANSACTION AMOUNT</span>
                <h2 style="margin: 5px 0; color: #3fb950 !important;">₹{avg_amount:,.2f}</h2>
            </div>
            """, unsafe_allow_html=True)
            
        st.write("")
        
        # Plots Row 1: Fraud Rate Over Time & Amount Distribution
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Fraud vs Genuine Transaction Amounts")
            fig_amount = px.box(
                df, 
                x="fraud", 
                y="amount", 
                color="fraud",
                color_discrete_map={0: "#3fb950", 1: "#ff7b72"},
                labels={"fraud": "Is Fraud?", "amount": "Amount (₹)"},
                title="Transaction Amount Distribution by Fraud Status"
            )
            fig_amount.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_amount, use_container_width=True)
            
        with col2:
            st.markdown("### Transaction Type vs Fraud Status")
            fig_type = px.histogram(
                df, 
                x="Transaction_Type", 
                color="fraud",
                barmode="group",
                color_discrete_map={0: "#3fb950", 1: "#ff7b72"},
                labels={"Transaction_Type": "Type", "fraud": "Fraud"},
                title="Transactions Count by Type and Fraud Label"
            )
            fig_type.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_type, use_container_width=True)

        # Plots Row 2: State and Gateway Distribution
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("### Fraud Rate by State")
            state_fraud = df.groupby('Transaction_State')['fraud'].agg(['count', 'sum']).reset_index()
            state_fraud['fraud_rate'] = (state_fraud['sum'] / state_fraud['count']) * 100
            state_fraud = state_fraud.sort_values(by='fraud_rate', ascending=False).head(10)
            
            fig_state = px.bar(
                state_fraud,
                y="Transaction_State",
                x="fraud_rate",
                orientation='h',
                color="fraud_rate",
                color_continuous_scale="Reds",
                labels={"Transaction_State": "State", "fraud_rate": "Fraud Rate (%)"},
                title="Top 10 States by Fraud Rate (%)"
            )
            fig_state.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_state, use_container_width=True)
            
        with col4:
            st.markdown("### Payment Gateway Risk Profile")
            gateway_fraud = df.groupby('Payment_Gateway')['fraud'].agg(['count', 'sum']).reset_index()
            gateway_fraud['fraud_rate'] = (gateway_fraud['sum'] / gateway_fraud['count']) * 100
            gateway_fraud = gateway_fraud.sort_values(by='fraud_rate', ascending=False)
            
            fig_gateway = px.bar(
                gateway_fraud,
                x="Payment_Gateway",
                y="fraud_rate",
                color="fraud_rate",
                color_continuous_scale="Oranges",
                labels={"Payment_Gateway": "Gateway", "fraud_rate": "Fraud Rate (%)"},
                title="Fraud Rate by Payment Gateway"
            )
            fig_gateway.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_gateway, use_container_width=True)
            
    else:
        st.warning("No data found to show visualization dashboard.")

# ----------------- PAGE 2: FRAUD DETECTOR -----------------
elif page == "🔎 Fraud Detector":
    st.subheader("Manual Transaction Verification")
    
    if model is None:
        st.error("Prediction engine is unavailable. Please check the model pickle file.")
    else:
        st.write("Fill in the transaction details below to run real-time fraud inference:")
        
        # Columns for form input
        c1, c2 = st.columns(2)
        
        with c1:
            amount_val = st.number_input(
                "Transaction Amount (₹)", 
                min_value=0.0, 
                value=250.0, 
                step=10.0,
                help="Enter the amount of transaction in INR"
            )
            tx_date = st.date_input(
                "Transaction Date", 
                value=datetime.today(),
                help="Date on which transaction is executed"
            )
            tx_type = st.selectbox(
                "Transaction Type", 
                options=TRANSACTION_TYPES,
                index=4 # default to 'Purchase'
            )
            payment_gate = st.selectbox(
                "Payment Gateway", 
                options=PAYMENT_GATEWAYS,
                index=8 # default to 'UPI Pay'
            )
            
        with c2:
            tx_state = st.selectbox(
                "Transaction State", 
                options=STATES,
                index=19 # default to 'Punjab'
            )
            merchant_cat = st.selectbox(
                "Merchant Category", 
                options=MERCHANT_CATEGORIES,
                index=7 # default to 'Purchases'
            )
            
        # Run prediction button
        st.write("")
        if st.button("🔴 Run Fraud Analysis", use_container_width=True):
            # Extract Month and Year
            year_val = tx_date.year
            month_val = tx_date.month
            
            # Prepare feature dictionary matching model.feature_names_in_ exactly
            feature_dict = {}
            for col in model.feature_names_in_:
                feature_dict[col] = 0
                
            # Set direct numeric/date features
            feature_dict['amount'] = int(amount_val)  # note the model expects integer casting based on astype(int)
            feature_dict['Year'] = year_val
            feature_dict['Month'] = month_val
            
            # Helper to set dummy encoded features if selected category is not the base case
            def set_dummy(prefix, selected_val):
                dummy_col = f"{prefix}_{selected_val}"
                if dummy_col in feature_dict:
                    feature_dict[dummy_col] = 1
                    
            set_dummy("Transaction_Type", tx_type)
            set_dummy("Payment_Gateway", payment_gate)
            set_dummy("Transaction_State", tx_state)
            set_dummy("Merchant_Category", merchant_cat)
            
            # Convert feature_dict to a DataFrame with exact column order
            input_df = pd.DataFrame([feature_dict])[model.feature_names_in_]
            
            # Run inference
            pred = model.predict(input_df)[0]
            probs = model.predict_proba(input_df)[0]
            fraud_prob = probs[1]
            
            # Display Prediction Card
            st.markdown("### Analysis Result:")
            if pred == 1:
                st.markdown(f"""
                <div class="result-card-fraud">
                    <h3 style="color: #ef4444 !important; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                        ⚠️ HIGH RISK - FRAUD SUSPECTED
                    </h3>
                    <p style="font-size: 1.1rem; margin-bottom: 8px; color: #fca5a5;">This transaction exhibits indicators typical of payment fraud in the training set.</p>
                    <p style="font-size: 1.25rem; font-weight: bold; margin: 0; color: #ffffff;">Fraud Probability: <span style="font-size: 1.6rem; color: #f87171;">{fraud_prob * 100:.2f}%</span></p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-card-safe">
                    <h3 style="color: #10b981 !important; margin-top: 0; display: flex; align-items: center; gap: 8px;">
                        ✅ LOW RISK - SAFE
                    </h3>
                    <p style="font-size: 1.1rem; margin-bottom: 8px; color: #a7f3d0;">No significant anomalies detected. The transaction matches genuine payment patterns.</p>
                    <p style="font-size: 1.25rem; font-weight: bold; margin: 0; color: #ffffff;">Fraud Probability: <span style="font-size: 1.6rem; color: #34d399;">{fraud_prob * 100:.2f}%</span></p>
                </div>
                """, unsafe_allow_html=True)

# ----------------- PAGE 3: VIEW DATASET -----------------
elif page == "📋 View Dataset":
    st.subheader("Historical UPI Transaction Database")
    
    if not df.empty:
        st.write(f"Displaying all records ({len(df)} transactions) currently in `Sample_DATA.csv`:")
        
        # Simple filters
        st.write("")
        c1, c2, c3 = st.columns(3)
        with c1:
            search_query = st.text_input("🔍 Search by Transaction ID / Merchant ID", "")
        with c2:
            status_filter = st.multiselect("Filter by Fraud Status", options=["Genuine (0)", "Fraudulent (1)"], default=["Genuine (0)", "Fraudulent (1)"])
        with c3:
            min_amt, max_amt = st.slider("Amount Range (₹)", float(df['amount'].min()), float(df['amount'].max()), (float(df['amount'].min()), float(df['amount'].max())))
            
        # Apply filters
        filtered_df = df.copy()
        if search_query:
            filtered_df = filtered_df[
                filtered_df['Transaction_ID'].astype(str).str.contains(search_query, case=False) |
                filtered_df['Merchant_ID'].astype(str).str.contains(search_query, case=False)
            ]
            
        map_status = []
        if "Genuine (0)" in status_filter:
            map_status.append(0)
        if "Fraudulent (1)" in status_filter:
            map_status.append(1)
            
        filtered_df = filtered_df[filtered_df['fraud'].isin(map_status)]
        filtered_df = filtered_df[(filtered_df['amount'] >= min_amt) & (filtered_df['amount'] <= max_amt)]
        
        st.dataframe(filtered_df, use_container_width=True)
        st.write(f"Showing {len(filtered_df)} of {len(df)} rows.")
    else:
        st.warning("Historical dataset is not available.")
