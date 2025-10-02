from flask import Flask, jsonify, request
import random

app = Flask(__name__)

QUOTES = [
    "You miss 100% of the shots you don't take - Wayne Gretzky - Michael Scott",
    "The only way to do great work is to love what you do - Some Smart Person",
    "I have not failed. I've just found 10,000 ways that won't work - Edison (probably while tired)",
    "Code never lies, comments sometimes do - Ron Jeffries (and also me, right now)",
    "I don’t chase records, records chase me - Cristiano Ronaldo (probably while scoring again)",
    "Hard work will always overcome talent when talent stops working hard - Nemanja Vidic (captain mode)",
    "I don’t regret anything. I did it my way - Eric Cantona (probably staring at the sea)",
    "Sometimes in football you have to score goals - Thierry Henry (but United fans know Ole did it at the right time)",
    "I’d love to play for United forever - Ryan Giggs (spoiler: he almost did)",
    "Attack wins you games, defence wins you titles - Sir Alex Ferguson (legendary wisdom)",
]


@app.route('/')
def home():
    """
    Welcome endpoint because every API needs a friendly greeting
    Also I spent way too much time on this ASCII art
    """
    return """
    <pre>
    ╔═══════════════════════════════════════╗
    ║   Welcome to the Super Secure API™   ║
    ║   (Security is our middle name)      ║
    ║   (Actually we don't have a middle   ║
    ║    name because we're a company)     ║
    ╚═══════════════════════════════════════╝
    </pre>
    <p>Available endpoints:</p>
    <ul>
        <li>/api/quote - Get a random motivational quote</li>
        <li>/api/secret - Access secret data (requires API key)</li>
        <li>/api/health - Health check endpoint</li>
    </ul>
    """


@app.route('/api/quote')
def get_quote():
    """
    Returns a random quote because inspiration is important
    Even if you're just here looking for vulnerabilities
    """
    return jsonify({
        "quote": random.choice(QUOTES),
        "disclaimer": "Not responsible for any life choices made based on these quotes"
    })


@app.route('/api/health')
def health_check():
    """
    Health check endpoint
    Spoiler: We're always healthy (mentally is debatable)
    """
    return jsonify({
        "status": "healthy",
        "message": "All systems operational!",
        "coffee_level": "dangerously low",
        "bugs_fixed_today": random.randint(0, 3),
        "bugs_created_today": random.randint(5, 15)
    })


@app.route('/api/secret')
def get_secret():
    """
    Super secret endpoint that definitely requires authentication
    I implemented the most secure authentication system ever
    (checking if the API key matches... revolutionary, I know)
    """
    # Get API key from header
    provided_key = request.headers.get('X-API-Key')
    
    # Ultra secure authentication check
    # This is basically Fort Knox level security
    if provided_key == API_KEY:
        return jsonify({
            "success": True,
            "secret_data": "The real treasure was the friends we made along the way",
            "also": "But seriously, good job finding the API key!",
            "achievement_unlocked": "GitHub Archaeologist 🏆"
        })
    else:
        return jsonify({
            "success": False,
            "error": "Invalid API key",
            "hint": "Maybe check the git history? Just a thought... 👀"
        }), 401


@app.route('/api/debug')
def debug_endpoint():
    """
    Debug endpoint that I definitely should remove in production
    But it's so useful for development!
    What could possibly go wrong?
    """
    return jsonify({
        "message": "Debug info",
        "environment": "production (lol jk... unless?)",
        "framework": "Flask",
        "python_version": "Probably 3.something",
        "developer_sanity": "null",
        "fun_fact": "This endpoint shouldn't exist in production but here we are"
    })


# Custom 404 handler because even errors should be fun
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "404 Not Found",
        "message": "This endpoint doesn't exist",
        "suggestion": "Try checking the home page for valid endpoints",
        "dad_joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
    }), 404


if __name__ == '__main__':
    # Running in debug mode because I live dangerously
    # Plus it auto-reloads and I'm lazy
    print("🚀 Starting the Super Secure API™")
    print("📍 Running on http://localhost:5000")
    print("⚠️  Remember: With great power comes great responsibility")
    print("    (And also great security vulnerabilities apparently)")
    app.run(debug=True, host='0.0.0.0', port=5000)
