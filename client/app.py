import db
import json
from flask import Flask, request, render_template, session, redirect, url_for, jsonify
from flask import jsonify


app = Flask(__name__)
app.secret_key = 'your_very_secure_secret_key'  # You should generate a secure key

users=db.users
videos=db.userdb.videos

		
def check_liked_lables():
    try:
        if request.method == 'POST':
            email=session.get('email')
            fields = 'liked_labels'
            user = {
                    'email': email,
                    fields: {"$exists": True}
                }
            user_data = users.find_one(user)
            if user_data is None:
                    recommended_list = videos.aggregate([
                        {"$sortByCount": "$video_id"},
                        {"$sort": {"count": -1}},
                        {"$limit": 5}
                    ])
                    vid_list = [doc["_id"] for doc in recommended_list]

                    data = {
                        'status': False,
                        'vid_list': vid_list
                    }
                    return data
            else:
                pass

    except Exception as e:
        print(e)


        


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("signin.html")




@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template("signup.html")



@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    status, email, username = db.check_user()

    data = {
        "username": username,
        "status": status
    }
    if status:
        session['username'] = username  # Store the username in session
        session['email'] = email
    return json.dumps(data)



@app.route('/register', methods = ['GET', 'POST'])
def register():
    status = db.insert_data()
    return json.dumps(status)


@app.route('/home',methods=['GET','POST'])
def display():
    username = session.get('username')
    email = session.get('email')
    return render_template("content.html",username=username)    
    # else:
    #     return redirect(url_for('home'))  # Redirect to login if no user is logged in

@app.route('/generate_list',methods=['GET','POST'])
def get_recommendation():
    data=check_liked_lables()
    print("DATA:",data)
    return json.dumps(data)
    # return render_template('content.html', data=data)

@app.route('/play_video/<videoId>')
def play_video(videoId):
    return render_template('play_video.html',videoId=videoId)

# Route to handle liking or disliking a video
@app.route('/like_video/<video_id>', methods=['POST'])
def like_video(video_id):
    action = request.json.get('action')
    user_email = session.get('email')

    # Check if user exists
    user_exists = users.find_one({'email': user_email})
    print("ACTION:",action)
    print("email:",user_email)
    if not user_exists:
        print(3)
        return jsonify({'error': 'User not found'})

    if action == 'like':
        print("ADDING")
        # Update user's liked videos array with video_id
        users.update_one({'email': user_email}, {'$addToSet': {'liked_videos': video_id}})
        return jsonify({'message': 'Video liked'})
    elif action == 'dislike':
        # Update user's disliked videos array with video_id
        users.update_one({'email': user_email}, {'$addToSet': {'disliked_videos': video_id}})
        return jsonify({'message': 'Video disliked'})
    else:
        return jsonify({'error': 'Invalid action'})

if __name__ == '__main__':
    app.run(debug = True)