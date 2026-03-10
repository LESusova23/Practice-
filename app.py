from flask import Flask, render_template, request
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"""
        <body style="font-family: Arial; background: #2c3e50; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
            <div style="text-align: center; background: #34495e; padding: 50px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                <h1 style="color: #27ae60;">Registration Success!</h1>
                <p style="font-size: 20px;">Welcome to the system, <b>{username}</b>!</p>
                <a href="/" style="color: #3498db; text-decoration: none; font-weight: bold;">Return to Form</a>
            </div>
        </body>
        """
    return render_template('register.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)