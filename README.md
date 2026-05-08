# Binance Futures Testnet Trading Bot

A modular Python trading bot for Binance USDT-M Futures Testnet supporting MARKET and LIMIT orders with CLI interaction, logging, validation, and error handling.

---

## Features

- Binance Futures Testnet integration
- MARKET and LIMIT order support
- BUY and SELL support
- Rich CLI interface
- Logging support
- Error handling
- Modular architecture

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── README.md
├── requirements.txt
├── trading_bot.log
└── .gitignore