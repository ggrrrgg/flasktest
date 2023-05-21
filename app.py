# from flask import Flask
# import datetime

# app = Flask(__name__)

# @app.route("/")
# def excerise():
#     nownow = datetime.datetime.now()
#     return f'<p>It is currently {nownow}<p>'

# from flask import Flask
# import json
# from datetime import datetime

# app = Flask(__name__)

# @app.route("/")
# def homepage():
#      return """<p>Hi, welcome to my API! Here are the endpoints that are available:</p>
#             <ul>
#                 <li>Current Time: /time</li>
#                 <li>Educator Info: /educators</li>
#             </ul>"""

# @app.route("/time")
# def current_time():
#      time_dict = {"current time": str(datetime.now().strftime('%H:%M'))}
#      return json.dumps(time_dict)

# @app.route("/educators")
# def educators():
#      educator_dict = {
#          "educators": [
#              {
#                  "Name": "Oliver",
#                  "Specialty": "Automated testing"
#              },
#              {
#                  "Name": "Jairo",
#                  "Specialty": "Discrete Mathematics"
#              },
#              {
#                  "Name": "Amir",
#                  "Specialty": "Web Development"
#              },
#              {
#                  "Name": "Iryna",
#                  "Specialty": "Database Engineering"
#              },
#              {
#                  "Name": "George",
#                  "Specialty": "Internet Security"
#              },
#          ]
#      }
#      return json.dumps(educator_dict)

from flask import Flask

app = Flask(__name__)

import random
import json

@app.route("/")
def coinflip():
    num=random.randint(1,2)
    if num == 1:
        result = 'Heads'
    if num == 2:
        result = 'Tails'          
    return json.dumps(result)