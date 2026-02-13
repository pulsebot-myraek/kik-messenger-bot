import os
from fastapi import FastAPI, Request
from utils.logger import setup_logger
from utils.http_client import HttpClient
from automation.message_router import route_message
from automation.response_builder import build_response

app = FastAPI()
logger = setup_logger()

BOT_USERNAME = os.getenv("KIK_BOT_USERNAME", "")
API_KEY = os.getenv("KIK_API_KEY", "")
KIK_API_URL = "https://api.kik.com/v1/message"

client = HttpClient()

@app.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    try:
        message = payload["messages"][0]
        from_user = message["from"]
        text = message.get("body", "")

        route = route_message(text)
        reply = build_response(route)

        body = {
            "messages": [{
                "to": from_user,
                "type": "text",
                "body": reply
            }]
        }
        client.post(KIK_API_URL, headers={
            "Authorization": f"Basic {API_KEY}",
            "Content-Type": "application/json"
        }, json=body)

        logger.info(f"Replied to {from_user}: {reply}")
    except Exception as e:
        logger.error(str(e))
    return {"status": "ok"}
