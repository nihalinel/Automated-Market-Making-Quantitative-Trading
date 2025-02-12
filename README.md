# Automated Market Making & Quantitative Trading

## Overview
This project implements an **automated market-making algorithm** for a quantitative trading simulation. The goal is to dynamically adjust bid-offer spreads and optimize risk management strategies using Python.

## Challenges & Solutions
- **Challenge 1: Non-Skewed Market Making**
  - Implemented a **2% non-skewed bid-offer spread** around the reference price.  
  - Processed real-time **price requests** and logged completed trades.  
  - Visualized bid, offer, and reference prices using **Matplotlib**.

- **Challenge 2: Skewed Market Making with Risk Management** 
  - Developed a **dynamic pricing algorithm** that **skews bid-ask spreads** based on risk exposure.  
  - Implemented **position-based adjustments** (Axed Long, Axed Short).  
  - Plotted price data for all tickers traded during the simulation.

## Technologies Used
- 🐍 **Python** (OOP, Data Processing)
- 📊 **Matplotlib** (Data Visualization)
- 📈 **Pandas** (Data Manipulation)
- ⚡ **AmplifyQuantTrading API** (Simulated Market Data)
