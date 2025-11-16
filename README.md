# Gravity Analysis App

A comprehensive web application for fundamental and technical analysis of Iranian stock market symbols.

## ⚠️ IMPORTANT: Microservices Required!

This application **REQUIRES** 4 external microservices to function. You **MUST** install and run them before starting this app!

**Quick Start**:
```powershell
.\start-microservices.ps1   # Start all microservices
.\verify-microservices.ps1  # Verify they're running
python app.py               # Then start this app
```

See [MICROSERVICES_SETUP.md](MICROSERVICES_SETUP.md) for detailed instructions.

## Features

- 📊 **Technical Analysis**: Calculate technical indicators (RSI, MACD, MA, Bollinger Bands, Stochastic)
- 📈 **Fundamental Analysis**: Calculate financial ratios and fundamental evaluation
- 📁 **Financial Reports Upload**: Upload and process MHTML files from Codal
- 💾 **SQLite Database**: Local data storage
- 🎨 **Beautiful UI**: Modern and user-friendly design with Bootstrap RTL
- 🔌 **Microservices Architecture**: Integration with 4 external microservices

## Required Microservices

**This app will NOT work without these 4 microservices running!**

1. **GravityTSE** (Port 5001): Market data fetching - https://github.com/GravityWavesMl/GravityTSE
2. **Gravity_TechAnalysis** (Port 5002): Technical analysis - https://github.com/Shakour-Data/Gravity_TechAnalysis
3. **Gravity_TSE_Codal** (Port 5003): MHTML processing - https://github.com/GravtyWaves/Gravity_TSE_Codal
4. **Gravity_FundamentalAnalysis** (Port 5004): Fundamental analysis - https://github.com/GravtyWaves/Gravity_FundamentalAnalysis

**See [MICROSERVICES_SETUP.md](MICROSERVICES_SETUP.md) for installation instructions.**

## Installation

```powershell
# Clone the repository
git clone https://github.com/GravtyWaves/GravityAnalysisApp.git
cd GravityAnalysisApp

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Initialize database
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"

# Run the application
python app.py
```

Visit http://localhost:5000 to access the application.

## Quick Start

See [README_FA.md](README_FA.md) for detailed Persian documentation.

## License

MIT License

## Disclaimer

This application is for educational and analytical purposes only and should not be considered as investment advice.