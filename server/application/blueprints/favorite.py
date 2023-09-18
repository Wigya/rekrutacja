from database.managers.favorite import FavoriteManager
from flask import Blueprint, request, jsonify


favorite_bp = Blueprint("favorite_bp", __name__)

favorite_db_manager = FavoriteManager()


@favorite_bp.route("/favorite", methods=["POST"])
def add_favorite():
    """
    Add a favorite item to the database.

    This route expects a JSON request with a "data" field containing the text of the favorite item.
    It adds the favorite item to the database using the FavoriteManager.

    Returns:
        A JSON response with a "success" field indicating whether the operation was successful.
    """
    try:
        # Get JSON data from the request
        jsoned_req = request.get_json()
        text = jsoned_req["data"]

        # Call the FavoriteManager to add the favorite
        db_response = favorite_db_manager.add_favorite(text)

        if db_response:
            return jsonify({"success": True})

        return jsonify({"success": False})

    except Exception as e:
        # Handle exceptions (e.g., JSON parsing error or database error)
        error_message = str(e)
        return jsonify({"success": False, "error": error_message})


@favorite_bp.route("/favorite", methods=["GET"])
def get_all_favorites():
    """
    Retrieve all favorite items from the database.

    Returns:
        A JSON response with a list of favorite items or an empty list if no items are found.
    """
    try:
        # Call the FavoriteManager to retrieve all favorite items
        db_resp = favorite_db_manager.get_favorites()

        return jsonify(db_resp)

    except Exception as e:
        # Handle exceptions (e.g., database error)
        error_message = str(e)
        return jsonify({"error": error_message}), 500


@favorite_bp.route("/favorite/<name>", methods=["DELETE"])
def remove_favorite(name):
    """
    Remove a favorite item from the database by name.

    Args:
        name (str): The name of the favorite item to remove.

    Returns:
        A JSON response with the number of rows affected by the delete operation.
    """
    try:
        num_deleted = favorite_db_manager.delete_favorite(name)
        return jsonify({"deleted_rows": num_deleted})

    except Exception as e:
        # Handle exceptions (e.g., database error)
        error_message = str(e)
        return jsonify({"error": error_message}), 500


@favorite_bp.route("/favorite", methods=["PATCH"])
def update_favorite():
    """
    Update a favorite item in the database.

    This route expects a JSON request with "original" and "newValue" fields specifying the item to update.

    Returns:
        A JSON response with a boolean indicating whether the update was successful.
    """
    try:
        jsoned_req = request.get_json()
        original, newValue = jsoned_req["original"], jsoned_req["newValue"]
        favorite_db_manager.update_favorite(original, newValue)
        return jsonify({"success": True})

    except Exception as e:
        # Handle exceptions (e.g., database error)
        error_message = str(e)
        return jsonify({"success": False, "error": error_message}), 500
