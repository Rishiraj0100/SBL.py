from os import environ as env
from sblpy.webhook.logger import log
from flask import Blueprint, request, abort, jsonify


flask_webhook = Blueprint("sbl_flask_webhook",__name__)

@flask_webhook.route(config.WEBHOOK_ROUTE, methods=["POST"])
def hook_resp():
  try:
    token = os.environ["SBL_HOOK_TOKEN"]
  except:
    raise ValueError("Sbl environment variable 'SBL_HOOK_TOKEN' not found!")

  if not request.headers.get("Authorization"): return jsonify({"code": 401, "message": "Unauthorised","success": False})
  if request.json["type"] == "test": log("test", request.json)
  else: log("Upvote", request.json)

  return jsonify({"code": 200, "success": True})

