import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("ICT Trading")

pairs = {"BTC": "BTC-USD", "ETH": "ETH-USD", "Gold": "GC=F"}
symbol = st.sidebar.selectbox("Asset:", list(pairs.keys()))

df = yf.download(pairs[symbol], period="1mo", auto_adjust=True, progress=False)
df.columns = df.columns.get_level_values(0)

price = float(df["Close"].iloc[-1])
high = float(df["High"].rolling(20).max().iloc[-1])
low = float(df["Low"].rolling(20).min().iloc[-1])
eq = (high + low) / 2

st.metric("Price", f"${price:,.2f}")
st.metric("Zone", "DISCOUNT 🟢" if price < eq else "PREMIUM 🔴")

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(df.index, df["Close"], color="white")
ax.axhline(eq, color="yellow", linestyle="--", label="EQ")
ax.axhline(high, color="#00ff88", linestyle=":", label="High")
ax.axhline(low, color="#ff4444", linestyle=":", label="Low")
ax.set_facecolor("#0e1117")
fig.patch.set_facecolor("#0e1117")
ax.tick_params(colors="white")
ax.legend(facecolor="#1a1a2e", labelcolor="white")
st.pyplot(fig)
plt.close()
