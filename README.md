# Automated Market Making & Quantitative Trading Simulation
This project involves developing an automated market-making algorithm within a quantitative trading simulation. The goal is to implement a market maker that dynamically adjusts bid-offer spreads based on market conditions, while optimizing risk management strategies. The simulation consists of multiple challenges designed to introduce and refine key concepts in market microstructure, algorithmic trading, and object-oriented programming (OOP) in Python.

Challenge 1: Non-Skewed Price Making <br />
Implement an automated market-making algorithm that provides a 2% non-skewed bid-offer spread around a reference price.<br />
Process price requests from a simulated hedge fund (HF).<br />
Log quoted trades and completed trades using OOP principles.<br />
Visualize bid, offer, and reference price data using Matplotlib.

Challenge 2: Skewed Price Making with Risk Management <br />
Extend the market-making algorithm to dynamically skew bid-offer spreads based on position risk:<br />
Neutral: 2% spread (non-skewed).<br />
Axed Long: 1% bid, 7% offer (encouraging selling).<br />
Axed Short: 7% bid, 1% offer (encouraging buying).<br />
Implement functions to handle hedge fund responses, logging trades into a Market Maker object.<br />
Generate dynamic price visualizations for all tickers traded.

Technologies Used: <br />
Python (Object-Oriented Programming, Data Processing) <br />
Matplotlib (Data Visualization)<br />
Pandas (Data Manipulation)<br />
Simulated Market Data API (AmplifyQuantTrading package)
