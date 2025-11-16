# GravityAnalysisApp - Complete Project Requirements & Plan

## 📋 Project Overview

**Objective**: Build a comprehensive web-based platform for fundamental and technical analysis of Iranian stock market symbols WITHOUT signal generation.

**Core Principle**: Integration of existing microservices, NOT reimplementation

---

## 🎯 Complete Feature Requirements

### 1. Market Data Integration
**Microservice**: GravityTSE (https://github.com/GravityWavesMl/GravityTSE)
- Fetch real-time and historical price data
- Market overview and statistics
- Symbol information
- OHLCV data

### 2. Technical Analysis
**Microservice**: Gravity_TechAnalysis (https://github.com/Shakour-Data/Gravity_TechAnalysis)
- Technical indicators (RSI, MACD, MA, Bollinger Bands, etc.)
- Chart patterns
- Support/Resistance levels
- Trend analysis
- Volume analysis

### 3. Financial Reports Management
**User Action**: Manual upload of MHTML files containing financial reports
**Microservice**: Gravity_TSE_Codal (https://github.com/GravtyWaves/Gravity_TSE_Codal)
- Parse MHTML files
- Extract financial data
- Clean and validate data
- Store in database

### 4. Fundamental Analysis (ENHANCED)
**Microservice**: Gravity_FundamentalAnalysis (https://github.com/GravtyWaves/Gravity_FundamentalAnalysis)

#### 4.1 Financial Statement Analysis
- **Balance Sheet** analysis
- **Income Statement** analysis
- **Cash Flow Statement** analysis
- Line-item trend analysis (YoY, QoQ)
- Horizontal & vertical analysis
- Common-size statements

#### 4.2 Financial Ratios
- **Liquidity Ratios**: Current ratio, Quick ratio, Cash ratio
- **Profitability Ratios**: ROE, ROA, Profit margin, Operating margin
- **Leverage Ratios**: Debt-to-equity, Interest coverage
- **Efficiency Ratios**: Asset turnover, Inventory turnover
- **Valuation Ratios**: P/E, P/B, EV/EBITDA, Dividend yield

#### 4.3 Stock Valuation (THREE SCENARIOS)
**Scenarios**:
1. **Optimistic** 🟢
2. **Neutral** 🟡
3. **Pessimistic** 🔴

**Valuation Methods**:
- Discounted Cash Flow (DCF)
- Dividend Discount Model (DDM)
- P/E Multiple method
- P/B Multiple method
- EV/EBITDA method

**User Customization**:
- Modify assumptions for each scenario
- Adjust growth rates
- Change discount rates
- Edit terminal value assumptions
- Modify risk-free rate
- Adjust market risk premium

#### 4.4 Value Drivers (ML-Based)
**System Features**:
- Extract value drivers from financial reports (per symbol)
- Machine learning model predicts default values for 3 scenarios
- User can modify all value drivers
- Examples:
  - Revenue growth rate
  - Operating margin
  - CAPEX as % of revenue
  - Working capital changes
  - Tax rate
  - WACC (Weighted Average Cost of Capital)

#### 4.5 Dollar Price Forecasting (ML-Based)
**Purpose**: Use in fundamental analysis calculations

**Methods**:
- Technical analysis
- Machine learning models
- Time series forecasting (ARIMA, LSTM)
- Sentiment analysis (if applicable)

**Output**: Three scenarios
1. Optimistic dollar rate 🟢
2. Neutral dollar rate 🟡
3. Pessimistic dollar rate 🔴

**Usage**: Apply forecasted dollar rates in valuation models

#### 4.6 Interest Rate Management
**Input Options**:
1. **User Upload**: User uploads time series of interest rates (CSV/Excel)
2. **System Default**: If no upload, use system's default interest rate curve

**Usage**: Discount rates in DCF, cost of debt calculations

---

### 5. Powerful Reporting System (NEW FEATURE)

#### 5.1 Report Formats

**A. Document Format (A4 Pages - Word-like)**
- Professional PDF-ready reports
- A4 page size (210mm × 297mm)
- Page breaks
- Headers & footers
- Table of contents
- Charts and tables embedded
- Print-ready

**B. Presentation Format (Slides - PowerPoint-like)**
- Slide-based layout
- Navigation controls
- Transitions
- Full-screen mode
- Export to PDF
- Presenter notes

#### 5.2 Report Customization (HTML/CSS/JavaScript)

**User Capabilities**:
- Add custom pages (Document format)
- Add custom slides (Presentation format)
- Write HTML structure
- Write CSS styling
- Write JavaScript interactivity
- Embed charts (Chart.js)
- Include data tables
- Add formulas and calculations

**System Features**:
- Template library
- Drag-and-drop builder
- Code editor (Monaco/Ace)
- Live preview
- Save custom templates
- Share templates with team

#### 5.3 Report Content

**Standard Sections**:
1. Executive Summary
2. Company Overview
3. Market Data & Price Analysis
4. Technical Analysis
   - Charts with indicators
   - Pattern recognition results
   - Support/resistance levels
5. Fundamental Analysis
   - Financial statements (3 years comparison)
   - Financial ratios (trend analysis)
   - Valuation (3 scenarios comparison)
   - Value drivers breakdown
6. Risk Assessment
7. Conclusion & Recommendations
8. Appendices

**Dynamic Data**:
- All data fetched from database
- Real-time calculations
- Interactive charts
- Filterable tables

---

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask 3.0.0
- **Language**: Python 3.9+
- **Database**: SQLite (with potential PostgreSQL migration)
- **ORM**: SQLAlchemy
- **HTTP Client**: requests
- **Data Processing**: pandas, numpy
- **ML/Forecasting**: scikit-learn, statsmodels, tensorflow (for LSTM)
- **Excel/CSV**: openpyxl, pandas

### Frontend
- **UI Framework**: Bootstrap 5 RTL
- **Charts**: Chart.js, D3.js (for advanced visualizations)
- **JavaScript**: ES6+, Axios
- **Code Editor**: Monaco Editor (VS Code engine) or Ace Editor
- **PDF Generation**: html2pdf.js, jsPDF
- **Presentation**: Reveal.js or custom slider
- **Icons**: Font Awesome

### Machine Learning
- **Frameworks**: scikit-learn, TensorFlow/Keras
- **Time Series**: statsmodels (ARIMA), Prophet (Facebook)
- **Feature Engineering**: pandas, numpy
- **Model Storage**: pickle, joblib

### DevOps
- **Containers**: Docker, docker-compose
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus, Grafana
- **Logging**: Python logging, ELK stack (optional)

---

## 📊 Database Schema (Enhanced)

### Core Tables

#### 1. symbols
```sql
- id (PK)
- code (UNIQUE)
- name
- industry
- sector
- market_cap
- created_at
- updated_at
```

#### 2. market_data
```sql
- id (PK)
- symbol_id (FK)
- date
- open_price
- high_price
- low_price
- close_price
- volume
- value
- trade_count
```

#### 3. financial_reports
```sql
- id (PK)
- symbol_id (FK)
- report_type (annual, quarterly)
- period_end_date
- fiscal_year
- mhtml_file_path
- uploaded_at
- processed_at
```

#### 4. balance_sheet
```sql
- id (PK)
- report_id (FK)
- cash_and_equivalents
- accounts_receivable
- inventory
- total_current_assets
- ppe_net
- intangible_assets
- total_assets
- current_liabilities
- long_term_debt
- total_liabilities
- shareholders_equity
- (... all line items)
```

#### 5. income_statement
```sql
- id (PK)
- report_id (FK)
- revenue
- cost_of_goods_sold
- gross_profit
- operating_expenses
- operating_income
- interest_expense
- income_before_tax
- tax_expense
- net_income
- eps
- (... all line items)
```

#### 6. cash_flow_statement
```sql
- id (PK)
- report_id (FK)
- operating_cash_flow
- investing_cash_flow
- financing_cash_flow
- free_cash_flow
- capex
- (... all line items)
```

#### 7. financial_ratios
```sql
- id (PK)
- symbol_id (FK)
- period_end_date
- current_ratio
- quick_ratio
- roe
- roa
- debt_to_equity
- pe_ratio
- pb_ratio
- (... all ratios)
```

### Valuation Tables

#### 8. valuation_scenarios
```sql
- id (PK)
- symbol_id (FK)
- scenario_type (optimistic, neutral, pessimistic)
- created_at
- updated_at
```

#### 9. valuation_assumptions
```sql
- id (PK)
- scenario_id (FK)
- assumption_type (growth_rate, discount_rate, etc.)
- year
- value
- is_user_modified
```

#### 10. value_drivers
```sql
- id (PK)
- symbol_id (FK)
- scenario_type
- driver_name
- driver_value
- ml_predicted_value
- user_modified_value
- is_user_modified
```

#### 11. stock_valuations
```sql
- id (PK)
- symbol_id (FK)
- scenario_id (FK)
- valuation_method (DCF, DDM, PE_Multiple, etc.)
- intrinsic_value
- current_price
- upside_downside_percent
- calculated_at
```

### Forecasting Tables

#### 12. dollar_forecasts
```sql
- id (PK)
- forecast_date
- scenario_type (optimistic, neutral, pessimistic)
- forecasted_value
- confidence_interval_lower
- confidence_interval_upper
- model_used
- created_at
```

#### 13. interest_rates
```sql
- id (PK)
- date
- rate_type (1year, 5year, 10year, etc.)
- rate_value
- is_user_uploaded
- uploaded_at
```

### Reporting Tables

#### 14. reports
```sql
- id (PK)
- symbol_id (FK)
- report_type (document, presentation)
- title
- created_by_user_id
- created_at
- updated_at
```

#### 15. report_pages
```sql
- id (PK)
- report_id (FK)
- page_number / slide_number
- page_type (standard, custom)
- html_content
- css_content
- js_content
- template_id (FK to templates)
```

#### 16. report_templates
```sql
- id (PK)
- template_name
- template_type (page, slide)
- html_template
- css_template
- js_template
- is_system_template
- created_by_user_id
- created_at
```

### ML Models Table

#### 17. ml_models
```sql
- id (PK)
- model_name
- model_type (dollar_forecast, value_driver_prediction)
- model_file_path
- accuracy_metrics (JSON)
- trained_at
- is_active
```

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────┐
│         GravityAnalysisApp (Flask)          │
│              Port 5000                      │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │  Web UI  │  │   API    │  │ Reporting│ │
│  │  (RTL)   │  │ Endpoints│  │  Engine  │ │
│  └──────────┘  └──────────┘  └──────────┘ │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │ ML Engine│  │ Database │  │  Cache   │ │
│  │(Forecast)│  │ (SQLite) │  │ (Redis)  │ │
│  └──────────┘  └──────────┘  └──────────┘ │
└──────────────────┬──────────────────────────┘
                   │ HTTP Requests
        ┌──────────┼──────────┬──────────┐
        │          │          │          │
        ▼          ▼          ▼          ▼
┌─────────────┐ ┌──────┐ ┌──────┐ ┌──────────┐
│ GravityTSE  │ │ Tech │ │Codal │ │Fundament.│
│ Port 5001   │ │ 5002 │ │ 5003 │ │Port 5004 │
└─────────────┘ └──────┘ └──────┘ └──────────┘
```

---

## 📅 Team Preparation & Planning

### Phase 1: Foundation (Sprint 1-2)
**Team Focus**: Setup, architecture, core integration

**Tasks**:
- [ ] Setup development environment (Lars - DevOps)
- [ ] Database schema design (Mohammed - Data Engineer)
- [ ] Microservices integration framework (Rajesh)
- [ ] Basic Flask app structure (Elena - Backend)
- [ ] UI/UX wireframes for all features (Maria - UX)
- [ ] Security baseline setup (Kim - Security)
- [ ] Documentation framework (Emma - Tech Writer)
- [ ] Test framework setup (Ana - QA)

**Deliverables**:
- Working Flask app
- Database created
- All 4 microservices connected
- Basic UI template
- CI/CD pipeline

### Phase 2: Core Features (Sprint 3-5)
**Team Focus**: Market data, technical analysis, financial reports

**Tasks**:
- [ ] Market data display (Elena + Sophie)
- [ ] Technical analysis charts (Sophie + Frontend)
- [ ] MHTML upload system (Elena + Rajesh)
- [ ] Financial statement display (Elena + Sarah)
- [ ] Financial ratios calculation (Sarah + Backend)
- [ ] Unit tests for all components (Ana)

**Deliverables**:
- Market data dashboard
- Technical analysis page
- Upload and process MHTML
- View financial statements
- Financial ratios dashboard

### Phase 3: Advanced Fundamental Analysis (Sprint 6-9)
**Team Focus**: Valuation, scenarios, ML integration

**Tasks**:
- [ ] Three-scenario valuation engine (Sarah + Elena)
- [ ] Value drivers extraction (Sarah + ML specialist)
- [ ] ML model for value drivers (Dedicated ML developer needed)
- [ ] DCF calculator (Sarah + Backend)
- [ ] Assumption editor UI (Sophie + Maria)
- [ ] Dollar forecast ML model (ML developer)
- [ ] Interest rate management (Elena + Frontend)

**Deliverables**:
- Complete valuation system
- Three scenarios working
- User can modify assumptions
- ML-based value drivers
- Dollar forecast integration

### Phase 4: Reporting System (Sprint 10-12)
**Team Focus**: Document & presentation builder

**Tasks**:
- [ ] Report engine architecture (Yuki + Elena)
- [ ] Document format (A4 pages) (Sophie + Maria)
- [ ] Presentation format (slides) (Sophie + Maria)
- [ ] HTML/CSS/JS editor integration (Sophie)
- [ ] Template system (Emma + Sophie)
- [ ] PDF export (Sophie)
- [ ] Custom page/slide builder (Sophie + Maria)

**Deliverables**:
- Document report generator
- Presentation report generator
- Custom page/slide creation
- Template library
- PDF export

### Phase 5: ML & Forecasting (Sprint 13-15)
**Team Focus**: Machine learning models

**Tasks**:
- [ ] Dollar price forecast model (ML developer)
- [ ] Value driver prediction model (ML developer)
- [ ] Model training pipeline (DevOps + ML)
- [ ] Model versioning (DevOps)
- [ ] Model monitoring (DevOps)
- [ ] Backtesting framework (QA + ML)

**Deliverables**:
- Trained dollar forecast model
- Trained value driver model
- Automated training pipeline
- Model performance dashboard

### Phase 6: Polish & Performance (Sprint 16-18)
**Team Focus**: Optimization, security, UX

**Tasks**:
- [ ] Performance optimization (Lars + Backend)
- [ ] Security audit (Kim)
- [ ] Penetration testing (Kim)
- [ ] UX improvements (Maria)
- [ ] Accessibility (WCAG) (Sophie + Maria)
- [ ] Mobile responsiveness (Sophie)
- [ ] Load testing (Ana + Lars)
- [ ] Final documentation (Emma)

**Deliverables**:
- Optimized application
- Security hardened
- Beautiful UX
- Complete documentation
- Production-ready

---

## 👥 Team Role Assignments (Enhanced)

### Core Team (12 members from TEAM_STRUCTURE.md)
All original roles remain unchanged

### Additional Specialists

#### 13. Git Workflow Manager & Version Control Specialist - Carlos Mendes (Portugal) 🇵🇹
**Expertise**: Git workflows, repository automation, commit organization
**Responsibilities**:
- Monitor repository changes (automated every 30 min)
- Organize commits when changes exceed 50 files
- Ensure Conventional Commits standard compliance
- Categorize file changes logically
- Automated commit and push workflow
- Maintain clean Git history
- Version control best practices

#### 14. Machine Learning Engineer - Dr. Wei Chen (China) 🇨🇳
**Expertise**: Time series forecasting, feature engineering, model deployment
**Responsibilities**:
- Build dollar price forecast models
- Develop value driver prediction models
- Feature engineering from financial data
- Model training and evaluation
- Hyperparameter tuning
- Model deployment and monitoring

#### 15. Financial Analyst/Quant - Amira Hassan (Egypt) 🇪🇬
**Expertise**: Equity valuation, financial modeling, scenario analysis
**Responsibilities**:
- Define valuation methodologies
- Validate DCF models
- Design scenario parameters
- Value driver identification
- Work with domain expert (Sarah)
- QA financial calculations

---

## 🎯 Success Metrics

### Technical Metrics
- API Response Time: < 2s (p95)
- ML Model Accuracy: > 85% for value drivers
- Test Coverage: > 80%
- Uptime: > 99.5%
- Report Generation: < 10s for 50-page document
- Git Commit Quality: 100% Conventional Commits compliance

### User Metrics
- Report customization usage: > 40%
- Scenario comparison usage: > 60%
- User-modified assumptions: > 30%
- Report exports: Track monthly

### Quality Metrics
- Critical bugs: 0
- High-priority bugs: < 3
- Code review approval: 100% within 24h
- Documentation completeness: 100%
- Uncommitted work at day end: 0 files (automated)

---

## 🚀 Getting Started (Team)

### Immediate Actions
1. **All team members**: Read all TEAM_*.md files
2. **Tech Lead (Yuki)**: Review this plan, propose architecture
3. **Scrum Master (Olga)**: Create sprint board, schedule planning
4. **Backend Lead (Elena)**: Assess technical feasibility
5. **ML Engineer (Wei)**: Research dollar forecast models
6. **UX Designer (Maria)**: Create wireframes for reporting system
7. **DevOps (Lars)**: Setup ML training infrastructure
8. **Everyone**: Vote on technology choices

### First Sprint Planning
- Duration: 2 weeks
- Goal: Foundation setup
- Team capacity: Calculate velocity
- Acceptance criteria: All microservices connected, basic UI

---

## 📝 Notes for Team

1. **Use Prompts Always**: Reference AI_AGENT_PROMPT.md, TEAM_PROMPTS.md
2. **Follow Standards**: CODING_STANDARDS.md is mandatory
3. **Democratic Decisions**: All major choices require team vote
4. **Quality First**: Don't rush, do it right
5. **Communicate Often**: Daily standups, async updates
6. **Document Everything**: Code, decisions, processes
7. **Test Thoroughly**: Unit, integration, E2E tests
8. **Security Mindset**: Think about vulnerabilities
9. **User-Centric**: Build for Iranian stock market analysts
10. **Iterate & Improve**: Continuous improvement
11. **Trust Carlos**: When changes > 50 files, Git Workflow Manager handles commits automatically

---

**Project Start**: Ready when team votes YES
**Estimated Duration**: 18-20 sprints (9-10 months)
**Team Size**: 15 members (12 core + 3 specialists)
**Complexity**: High (ML + Finance + Reporting)
**Risk**: Medium (Microservices dependency, ML accuracy)

**Let's build something amazing! 🚀**

---

**Version**: 2.0.0
**Date**: 2024-11-16
**Status**: Planning Phase
**Next Step**: Team vote on plan approval
