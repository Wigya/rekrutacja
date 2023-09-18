from json import JSONDecodeError
from flask import Blueprint, jsonify
import requests
import json

dog_facts_bp = Blueprint("dog_facts_bp", __name__)


@dog_facts_bp.route("/dog_fact", methods=["GET"])
def get_dog_fact():
    """
    Get a random dog fact from an external API.

    This route sends a request to an external API that provides random dog facts.
    It handles API errors and JSON decoding errors, returning appropriate responses.

    Returns:
        dict: A JSON response containing a dog fact or an error message.
    """
    try:
        # Send a request to the external API
        random_fact = requests.get("https://dogapi.dog/api/facts")

        # Check if the API request was successful (status code 200)
        if random_fact.status_code != 200:
            return jsonify({"status": False, "payload": "Problem with an external API"})

        # Decode the JSON response from the external API
        response = json.loads(random_fact.content)

        # Extract a random dog fact from the response
        random_fact = response["facts"][0]

        return jsonify({"status": True, "payload": random_fact})

    except json.JSONDecodeError as e:
        return jsonify({"status": False, "payload": str(e)})

    except requests.RequestException as e:
        return jsonify({"status": False, "payload": f"Request error: {str(e)}"})
