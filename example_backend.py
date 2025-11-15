"""
Simple Flask Backend Server for HTMLx Compiler
Demonstrates backend integration with the markup language
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import json

app = Flask(__name__)
CORS(app)

# Sample data store
users_db = {
    'users': [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'plan': 'professional'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'plan': 'starter'},
        {'id': 3, 'name': 'Mike Johnson', 'email': 'mike@example.com', 'plan': 'enterprise'},
    ]
}

forms_db = {
    'submissions': []
}

plans_db = {
    'starter': {'name': 'Starter', 'price': 9, 'users': 5, 'storage': '1GB'},
    'pro': {'name': 'Professional', 'price': 29, 'users': 'unlimited', 'storage': '100GB'},
    'enterprise': {'name': 'Enterprise', 'price': 'custom', 'users': 'unlimited', 'storage': 'unlimited'},
}

# ============ API ENDPOINTS ============

@app.route('/')
def index():
    """API Documentation"""
    return jsonify({
        'api': 'HTMLx Backend Example',
        'version': '1.0',
        'endpoints': {
            'POST /api/trackCTAClick': 'Track CTA button clicks',
            'POST /api/submitForm': 'Submit contact form',
            'GET /api/selectPlan/<plan>': 'Select a pricing plan',
            'POST /api/contactSales': 'Contact sales inquiry',
            'GET /api/getData': 'Get sample user data',
            'GET /api/getStats': 'Get platform statistics',
            'GET /api/users': 'Get all users',
            'GET /api/health': 'Health check',
        }
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'uptime': '99.9%'
    })

@app.route('/api/trackCTAClick', methods=['POST', 'GET'])
def track_cta_click():
    """Track CTA button clicks"""
    data = request.get_json() if request.method == 'POST' else {}
    
    return jsonify({
        'status': 'success',
        'message': 'CTA click tracked successfully',
        'timestamp': datetime.now().isoformat(),
        'event': 'CTA_CLICK',
        'user_agent': request.headers.get('User-Agent', 'Unknown'),
        'ip': request.remote_addr
    })

@app.route('/api/submitForm', methods=['POST', 'GET'])
def submit_form():
    """Handle form submissions"""
    data = request.get_json() if request.method == 'POST' else {
        'name': 'Demo User',
        'email': 'demo@example.com',
        'subject': 'Demo Submission',
        'message': 'This is a test submission'
    }
    
    # Store form submission
    submission = {
        'id': len(forms_db['submissions']) + 1,
        'name': data.get('name', ''),
        'email': data.get('email', ''),
        'subject': data.get('subject', ''),
        'message': data.get('message', ''),
        'submitted_at': datetime.now().isoformat(),
        'status': 'received'
    }
    forms_db['submissions'].append(submission)
    
    return jsonify({
        'status': 'success',
        'message': 'Form submitted successfully',
        'submission_id': submission['id'],
        'confirmation_email': data.get('email', 'not provided'),
        'received_at': datetime.now().isoformat(),
        'expected_response': '24 hours'
    }), 201

@app.route('/api/selectPlan/<plan>', methods=['POST', 'GET'])
def select_plan(plan):
    """Handle plan selection"""
    plan_lower = plan.lower()
    
    if plan_lower not in plans_db:
        return jsonify({
            'status': 'error',
            'message': f'Plan "{plan}" not found',
            'available_plans': list(plans_db.keys())
        }), 404
    
    plan_details = plans_db[plan_lower]
    
    return jsonify({
        'status': 'success',
        'message': f'Plan "{plan_details["name"]}" selected',
        'plan': plan_details,
        'selected_at': datetime.now().isoformat(),
        'billing_cycle': 'monthly',
        'next_billing': (datetime.now() + timedelta(days=30)).isoformat(),
        'auto_renew': True
    }), 200

@app.route('/api/contactSales', methods=['POST', 'GET'])
def contact_sales():
    """Handle sales contact requests"""
    data = request.get_json() if request.method == 'POST' else {}
    
    return jsonify({
        'status': 'success',
        'message': 'Your inquiry has been sent to our sales team',
        'inquiry_id': f'INQ-{datetime.now().strftime("%Y%m%d%H%M%S")}',
        'sales_representative': 'sales@company.com',
        'expected_response_time': '2-4 hours',
        'contact_method': 'email',
        'timestamp': datetime.now().isoformat(),
        'note': 'A sales representative will reach out to you shortly'
    }), 201

@app.route('/api/getData', methods=['GET', 'POST'])
def get_data():
    """Get sample data"""
    return jsonify({
        'status': 'success',
        'data': users_db['users'],
        'total_users': len(users_db['users']),
        'timestamp': datetime.now().isoformat(),
        'source': 'Database',
        'cached': False
    })

@app.route('/api/getStats', methods=['GET', 'POST'])
def get_stats():
    """Get platform statistics"""
    return jsonify({
        'status': 'success',
        'stats': {
            'activeUsers': 15234,
            'websitesCount': 987654,
            'perfScore': 98,
            'uptime': '99.9%',
            'securityLevel': 'A+',
            'validationScore': 100,
            'apiResponseTime': '45ms',
            'databaseConnections': 156,
            'cacheHitRate': '87%',
            'averageLoadTime': '1.2s'
        },
        'timestamp': datetime.now().isoformat(),
        'last_updated': (datetime.now() - timedelta(minutes=5)).isoformat()
    })

@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    return jsonify({
        'status': 'success',
        'users': users_db['users'],
        'total': len(users_db['users']),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/forms', methods=['GET'])
def get_forms():
    """Get all form submissions"""
    return jsonify({
        'status': 'success',
        'submissions': forms_db['submissions'],
        'total': len(forms_db['submissions']),
        'timestamp': datetime.now().isoformat()
    })

# ============ ERROR HANDLERS ============

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found',
        'error': str(error)
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({
        'status': 'error',
        'message': 'Internal server error',
        'error': str(error)
    }), 500

@app.before_request
def log_request():
    """Log incoming requests"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {request.method} {request.path}")

@app.after_request
def add_headers(response):
    """Add security and CORS headers"""
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

# ============ MAIN ============

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════╗
    ║   HTMLx Compiler - Backend Server     ║
    ║   Running on http://localhost:5000     ║
    ╚════════════════════════════════════════╝
    
    Available Endpoints:
    • POST/GET /api/trackCTAClick     - Track clicks
    • POST/GET /api/submitForm         - Form submission
    • GET      /api/selectPlan/<plan>  - Select plan
    • POST/GET /api/contactSales       - Contact sales
    • GET/POST /api/getData            - Get user data
    • GET/POST /api/getStats           - Get statistics
    • GET      /api/users              - Get all users
    • GET      /api/health             - Health check
    
    Press Ctrl+C to stop the server.
    """)
    
    # Run Flask app
    app.run(debug=True, host='localhost', port=5000)
