from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from application import routes

        from application.plotlydash.dashboard import create_dashboard
        app = create_dashboard(app)

        from application.plotlydash.graph import create_graph
        app = create_graph(app)

        return app