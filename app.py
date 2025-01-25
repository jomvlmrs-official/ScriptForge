from flask import Flask, render_template, request, jsonify
import esprima

app = Flask(__name__)

# Validate JavaScript script using Esprima
def validate_script(script):
    try:
        esprima.parseScript(script)
        return "✅ Script is valid and error-free."
    except Exception as e:
        return f"❌ Validation failed: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    data = request.get_json()
    script = data.get('script')

    # Validate the script
    result = validate_script(script)

    # Return validation result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)