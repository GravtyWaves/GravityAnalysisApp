"""
Gravity Analysis App - Main Application
تحلیل بنیادی و تکنیکال بازار سرمایه ایران
"""
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_cors import CORS
import os
from datetime import datetime
from werkzeug.utils import secure_filename

# Import services
from services.market_data_service import MarketDataService
from services.technical_analysis_service import TechnicalAnalysisService
from services.codal_service import CodalService
from services.fundamental_analysis_service import FundamentalAnalysisService
from database.db_manager import DatabaseManager

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gravity-analysis-secret-key-2025'
app.config['UPLOAD_FOLDER'] = 'uploads/mhtml'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['ALLOWED_EXTENSIONS'] = {'mhtml', 'mht'}

CORS(app)

# Initialize database
db_manager = DatabaseManager()

# Initialize services
market_service = MarketDataService()
technical_service = TechnicalAnalysisService()
codal_service = CodalService()
fundamental_service = FundamentalAnalysisService()

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')


@app.route('/symbols')
def symbols_list():
    """List all available symbols"""
    symbols = db_manager.get_all_symbols()
    return render_template('symbols.html', symbols=symbols)


@app.route('/symbol/<symbol_code>')
def symbol_detail(symbol_code):
    """Detailed view for a specific symbol"""
    symbol_data = db_manager.get_symbol_data(symbol_code)
    if not symbol_data:
        flash('نماد مورد نظر یافت نشد', 'error')
        return redirect(url_for('symbols_list'))
    
    return render_template('symbol_detail.html', symbol=symbol_data)


@app.route('/technical-analysis/<symbol_code>')
def technical_analysis(symbol_code):
    """Technical analysis page for a symbol"""
    return render_template('technical_analysis.html', symbol_code=symbol_code)


@app.route('/fundamental-analysis/<symbol_code>')
def fundamental_analysis(symbol_code):
    """Fundamental analysis page for a symbol"""
    return render_template('fundamental_analysis.html', symbol_code=symbol_code)


@app.route('/upload')
def upload_page():
    """Page for uploading MHTML files"""
    return render_template('upload.html')


# ==================== API Endpoints ====================

@app.route('/api/market/symbols', methods=['GET'])
def api_get_symbols():
    """Get all market symbols"""
    try:
        symbols = market_service.get_symbols()
        return jsonify({'success': True, 'data': symbols})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/market/price/<symbol_code>', methods=['GET'])
def api_get_price(symbol_code):
    """Get current price data for a symbol"""
    try:
        days = request.args.get('days', 30, type=int)
        price_data = market_service.get_price_data(symbol_code, days)
        return jsonify({'success': True, 'data': price_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/market/update/<symbol_code>', methods=['POST'])
def api_update_market_data(symbol_code):
    """Update market data for a symbol"""
    try:
        result = market_service.update_symbol_data(symbol_code)
        if result:
            db_manager.save_market_data(symbol_code, result)
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/technical/analyze/<symbol_code>', methods=['GET'])
def api_technical_analyze(symbol_code):
    """Perform technical analysis on a symbol"""
    try:
        # Get price data from database
        price_data = db_manager.get_price_history(symbol_code)
        
        # Perform technical analysis
        analysis_result = technical_service.analyze(price_data)
        
        # Save results
        db_manager.save_technical_analysis(symbol_code, analysis_result)
        
        return jsonify({'success': True, 'data': analysis_result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/technical/indicators/<symbol_code>', methods=['GET'])
def api_get_indicators(symbol_code):
    """Get technical indicators for a symbol"""
    try:
        indicators = request.args.getlist('indicators')
        if not indicators:
            indicators = ['RSI', 'MACD', 'MA', 'BB']
        
        price_data = db_manager.get_price_history(symbol_code)
        result = technical_service.calculate_indicators(price_data, indicators)
        
        return jsonify({'success': True, 'data': result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/upload/mhtml', methods=['POST'])
def api_upload_mhtml():
    """Upload and process MHTML files"""
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'فایلی انتخاب نشده است'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'error': 'فایلی انتخاب نشده است'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            file.save(filepath)
            
            # Process MHTML file
            result = codal_service.process_mhtml(filepath)
            
            if result:
                # Save financial data to database
                db_manager.save_financial_data(result)
                
                return jsonify({
                    'success': True,
                    'message': 'فایل با موفقیت آپلود و پردازش شد',
                    'data': result
                })
            else:
                return jsonify({'success': False, 'error': 'خطا در پردازش فایل'}), 500
        
        return jsonify({'success': False, 'error': 'فرمت فایل نامعتبر است'}), 400
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/fundamental/analyze/<symbol_code>', methods=['GET'])
def api_fundamental_analyze(symbol_code):
    """Perform fundamental analysis on a symbol"""
    try:
        # Get financial data from database
        financial_data = db_manager.get_financial_data(symbol_code)
        
        if not financial_data:
            return jsonify({
                'success': False,
                'error': 'اطلاعات مالی برای این نماد یافت نشد'
            }), 404
        
        # Perform fundamental analysis
        analysis_result = fundamental_service.analyze(financial_data)
        
        # Save results
        db_manager.save_fundamental_analysis(symbol_code, analysis_result)
        
        return jsonify({'success': True, 'data': analysis_result})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/fundamental/ratios/<symbol_code>', methods=['GET'])
def api_get_financial_ratios(symbol_code):
    """Get financial ratios for a symbol"""
    try:
        financial_data = db_manager.get_financial_data(symbol_code)
        
        if not financial_data:
            return jsonify({
                'success': False,
                'error': 'اطلاعات مالی برای این نماد یافت نشد'
            }), 404
        
        ratios = fundamental_service.calculate_ratios(financial_data)
        
        return jsonify({'success': True, 'data': ratios})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/search', methods=['GET'])
def api_search():
    """Search for symbols"""
    try:
        query = request.args.get('q', '')
        if len(query) < 2:
            return jsonify({'success': True, 'data': []})
        
        results = db_manager.search_symbols(query)
        return jsonify({'success': True, 'data': results})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return render_template('500.html'), 500


if __name__ == '__main__':
    # Initialize database tables
    db_manager.init_db()
    
    # Run the application
    app.run(debug=True, host='0.0.0.0', port=5000)
