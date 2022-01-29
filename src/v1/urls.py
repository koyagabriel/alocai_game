from src.v1 import v1
from src.v1.views import index, get_database_status, post_games

v1.add_url_rule("/index", endpoint="index", methods=["GET"], view_func=index, strict_slashes=False)
v1.add_url_rule("/status", endpoint="status", methods=["GET", "HEAD"], view_func=get_database_status, strict_slashes=False)
v1.add_url_rule("/games", endpoint="games", methods=["POST"], view_func=post_games, strict_slashes=False)
