from .. import connection
import psycopg2


class FavoriteManager:
    def __init__(self):
        self.cursor = connection.cursor()

    def add_favorite(self, name: str) -> bool:
        """
        Add a favorite item to the database.

        Args:
            name (str): The name of the favorite item to add.

        Returns:
            bool: True if the item was added successfully, False otherwise.
        """
        try:
            self.cursor.execute(
                f"INSERT INTO favorite (text) VALUES ('{name}') RETURNING id")
            connection.commit()

            result = self.cursor.fetchone()
            if result is not None:
                return True

            return False

        except psycopg2.Error as e:
            connection.rollback()
            raise e

    def get_favorites(self) -> list:
        """
        Retrieve all favorite items from the database.

        Returns:
            list: A list of favorite items.
        """
        try:
            self.cursor.execute("SELECT text FROM favorite")
            all_rows = self.cursor.fetchall()
            all_rows = [row[0] for row in all_rows]
            return all_rows

        except psycopg2.Error as e:
            connection.rollback()
            raise e

    def delete_favorite(self, text: str) -> int:
        """
        Delete a favorite item from the database.

        Args:
            text (str): The text of the favorite item to delete.

        Returns:
            int: The number of rows affected by the delete operation.
        """
        try:
            self.cursor.execute(f"DELETE FROM favorite WHERE text = '{text}'")
            connection.commit()
            return self.cursor.rowcount

        except psycopg2.Error as e:
            connection.rollback()
            raise e

    def update_favorite(self, textToChange: str, newValue: str) -> None:
        """
        Update a favorite item in the database.

        Args:
            textToChange (str): The text of the item to be updated.
            newValue (str): The new text for the item.
        """
        try:
            self.cursor.execute(
                f"UPDATE favorite SET text = '{newValue}' WHERE text = '{textToChange}'")
            connection.commit()

        except psycopg2.Error as e:
            connection.rollback()
            raise e
