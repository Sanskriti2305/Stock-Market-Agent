# Stock Market AI Agent 📈

An intelligent stock market analysis agent built with Google ADK and Gemini 2.5 Flash, deployed on Cloud Run. Ask anything about any stock — get real-time data powered by live market feeds, analysed by Gemini AI.

## 🌐 Live Demo
👉 **[Try it live](https://stock-market-agent-790401980891.us-central1.run.app)**

> Type any question like "Should I invest in RELIANCE.NS?" and get a full AI-powered analysis instantly.

---

## 🎯 What It Does

This agent performs **intelligent stock market analysis** in two steps:

1. **Fetches live market data** — current price, P/E ratio, 52-week high/low, market cap, volume, sector, debt-to-equity ratio, dividend yield
2. **Reasons with Gemini 2.5 Flash** — analyses the data like an experienced financial analyst and answers your specific question

### Example Questions You Can Ask
- `Should I invest in RELIANCE.NS right now?`
- `Is TCS.NS overvalued or undervalued?`
- `What are the risks of investing in AAPL?`
- `Compare the current price of INFY.NS to its 52-week range`
- `What is the market sentiment for TSLA?`

### Supported Stock Formats
| Market | Format | Example |
|--------|--------|---------|
| India (NSE) | TICKER.NS | RELIANCE.NS, TCS.NS, INFY.NS |
| India (BSE) | TICKER.BO | RELIANCE.BO |
| USA | TICKER | AAPL, TSLA, GOOGL, MSFT |
| South Korea | TICKER.KS | 005930.KS (Samsung) |
| Hong Kong | TICKER.HK | 9988.HK (Alibaba) |

---

## 🏗️ Architecture
```
User Question
      ↓
ADK Agent (stock_market_agent)
      ↓
get_stock_data tool → Yahoo Finance API (live data)
      ↓
Gemini 2.5 Flash (reasoning + analysis)
      ↓
Structured Response with sentiment, risks, strengths, recommendation
```

**Why this is agentic:** The agent decides when to call the `get_stock_data` tool, what symbol to fetch, and how to reason about the results — it's not just a prompt wrapper.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | Google ADK (Agent Development Kit) |
| AI Model | Gemini 2.5 Flash |
| Live Data | Yahoo Finance (yfinance) |
| Deployment | Google Cloud Run |
| Region | us-central1 |

---

## 🚀 Run Locally

### Prerequisites
- Python 3.11+
- Google ADK installed
- Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

### Setup
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/stock-market-agent.git
cd stock-market-agent

# Install dependencies
pip install google-adk yfinance

# Set up environment
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# Run locally
adk web --allow_origins="*"
```

Visit `http://localhost:8000` to use the agent.

---

## 📁 Project Structure
```
stock_agent/
├── agent.py          # ADK agent definition + stock data tool
├── requirements.txt  # Dependencies
├── .env.example      # Environment variables template
├── .env              # Your keys (not committed)
└── __init__.py       # ADK package init
```

---

## 🌏 Why This Matters

Asia has hundreds of millions of retail investors making decisions based on incomplete information, social media tips, and gut feelings. This agent gives anyone - regardless of their financial knowledge - access to structured, data-driven stock analysis in seconds.

Every analysis ends with a clear disclaimer that this is educational only - responsible AI in practice.

---

## ⚠️ Disclaimer

This agent provides AI-generated analysis for **educational purposes only**. It is not financial advice. Always consult a qualified financial advisor before making investment decisions.

---

*Built using *
*Google ADK + Gemini 2.5 Flash + Cloud Run*
