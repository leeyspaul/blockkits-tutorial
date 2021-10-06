import os

from views import DOCS_FEEDBACK_VIEW
from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

@app.shortcut("docs_report")
def docs_report(ack, shortcut, client):
    ack()
    
    client.views_open(trigger_id=shortcut["trigger_id"], view=DOCS_FEEDBACK_VIEW)

@app.view("")
def handle_view_events(ack, body, logger):
    pass

# Starts your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 8080)))