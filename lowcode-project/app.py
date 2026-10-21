
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello from Marcela</h1>"

@app.route("/about")
def about():
    return """
    <h1>What I would build in one evening</h1>
    <p>If I could build an application in one evening instead of a quarter, I would create a simple personal learning planner. The application would help students organise their studies, set goals, and track their progress. Users could add tasks, choose deadlines, and mark activities as completed. It would also show a daily checklist and a weekly progress summary.</p>
    <p>I would start with a basic version using Python and Flask, with a simple web interface. I would use AI tools such as ChatGPT to help me understand the code, identify errors, and develop new features. I would test the application with a few real tasks and improve it based on the results.</p>
    <p>My goal would not be to create a perfect product in one evening. Instead, I would focus on solving one small, useful problem. This approach would help me learn by doing, gain confidence in programming, and understand how an idea can become a working application.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
