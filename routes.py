from config import app
from controller import main, add_user, login, logout


app.add_url_rule("/", view_func=main)
app.add_url_rule("/process/user", view_func=add_user, methods=['POST'])
app.add_url_rule("/login", view_func=login, methods=['POST'])
app.add_url_rule("/logout", view_func=logout)

