from flask import render_template
from flask import current_app as app

@app.route('/')
def home():
    """Landing page."""
    return """<h1>Welcome. This is Flask App Homepage</h1><div class="main">
			<ul>
				<li><a href="/">Home</a></li>
				<li><a href="/other">Go to Other Flask rendered Page</a></li>
				<li><a href="/dashgraph">Graph Rendered using Dash</a></li>
				<li><a href="/dashapp">table Rendered using Dash</a></li>
			</ul>
		</div>"""

@app.route('/other')
def other():
    return '<h1>Welcome. This is Flask App Other Page</h1>'