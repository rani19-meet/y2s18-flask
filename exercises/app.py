from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    fav_players=["pele","salah","modric"]
    likes_same_sport = True    
    return render_template(
        "index.html",
        fav_players=fav_players)
        
if __name__ == '__main__':
   app.run(debug = True)