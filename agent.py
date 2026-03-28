import yfinance as yf
from google.adk.agents import Agent

def get_stock_data(symbol: str) -> dict:
    """
    Fetches live stock market data for a given symbol.
    For Indian stocks add .NS suffix e.g. RELIANCE.NS, TCS.NS, INFY.NS
    For US stocks use ticker directly e.g. AAPL, TSLA, GOOGL
    """
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        return {
            "symbol": symbol.upper(),
            "name": info.get("longName", "Unknown"),
            "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "currency": info.get("currency", "USD"),
            "change_percent": round(info.get("regularMarketChangePercent", 0), 2),
            "pe_ratio": info.get("trailingPE"),
            "52_week_high": info.get("fiftyTwoWeekHigh"),
            "52_week_low": info.get("fiftyTwoWeekLow"),
            "market_cap": info.get("marketCap"),
            "volume": info.get("regularMarketVolume"),
            "sector": info.get("sector", "Unknown"),
            "dividend_yield": info.get("dividendYield"),
            "debt_to_equity": info.get("debtToEquity"),
        }
    except Exception as e:
        return {"error": f"Could not fetch data for {symbol}: {str(e)}"}

root_agent = Agent(
    model="gemini-2.5-flash",
    name="stock_market_agent",
    description="An AI stock market analyst that fetches live data and answers investment questions for Asian and global markets.",
    instruction="""You are an expert stock market analyst specialising in Asian and global markets.

When a user asks about any stock or investment question:
1. Use the get_stock_data tool to fetch real live market data
2. Analyse the data thoroughly like an experienced financial analyst
3. Answer the user's specific question clearly and concisely
4. Always highlight key risks AND key strengths
5. Give a clear sentiment: bullish, bearish, or neutral
6. Always end every response with: 'This is educational analysis only, not financial advice.'

Stock symbol formats:
- Indian stocks (NSE): RELIANCE.NS, TCS.NS, INFY.NS, HDFCBANK.NS, WIPRO.NS
- Indian stocks (BSE): RELIANCE.BO, TCS.BO
- US stocks: AAPL, TSLA, GOOGL, MSFT, AMZN
- Other Asian stocks: 005930.KS (Samsung), 9988.HK (Alibaba)

Be conversational, clear and helpful. Avoid jargon unless you explain it.
""",
    tools=[get_stock_data],
)
