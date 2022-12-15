from flask import Flask, request, render_template

import videocompiler
import videouploader

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    print("WELCOME TO THE VIDEO COMPILATION SCRAPER")
    if request.method == 'POST':
        #extract the user's input from the request data
        instagram_account = request.form['instagram_account']
        #form understands what the input is supposed to be
        return 'You entered the Instagram account: {}'.format(instagram_account), render_template('index.html')
        #return render_template('index.html')
        app.run(instagram_account)
    else:
        #return a form that allows the user to enter an Instagram account name
        return '''
            <form method="post">
                <input type="text" name="instagram_account" placeholder="Enter an Instagram account">
                <input type="submit" value="Submit">
            </form>
        '''
@app.route('/run')
def run(instagram_account):
    from instaloader import Instaloader, Profile
    import time
    L = Instaloader()
    # initalizing instaloader
    user = "Cats0f1nstagramn"
    passw = "Tinypeoplemod"
    L.login(user, passw)
    # logging in to test account
    PROFILE = instagram_account  # specified instagram account to get posts\
    #L.download_profile(profile_name=PROFILE)

    profile = Profile.from_username(L.context, PROFILE)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes,reverse=True)
    selected_range = posts_sorted_by_likes[0:2] #to download from only 2 posts
    #sorting to get most liked posts
    for post in posts_sorted_by_likes:
        if post.is_video:
            L.download_post(post, PROFILE)
            #dowdloading posts

    videocompiler.videocompiler()
    #calls video compiler file
    videouploader.videouploader()
    #calls video uploader file to complete the program

if __name__ == '__main__':
    app.run()
