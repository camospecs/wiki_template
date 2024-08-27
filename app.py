from flask import Flask, abort, request, render_template, flash, redirect, url_for
from markupsafe import Markup
import sqlite3 as sqlite
import variables as var

view_count = {} #Used to store home and posts view count as {url_path : no_views

app = Flask(__name__)
app.config['SECRET_KEY'] = var.secret_key

@app.route('/')
def home():
    '''
    Home page that contain 1st 3 posts and a brief introduction.    
    '''
    visits = view_counter('/')
    home_posts = [get_post('wiki-template-guide'),get_post('wiki-template-guide'),get_post('hosting-a-web-server-using-ec2-instances') ] #Shows featured posts. Must be defined manually. If wrong, internal error occurs
    return render_template('home.html', home_posts=home_posts, visits=visits)

@app.route('/links')
def links():
    return render_template('links.html')


''' Currently not working
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    

    #A page for gettingg input submitting data to the db for use as posts.

    #Title = Main title to be shown at the top of post and on the main card.
    #Brief = A short description of the post. Shown below titile on both post and card.
    #Picture = A picture shown at the top of post and card.
    #Content = Text shown as the main content of the post.

    #Note: Timestamp is gained in schema.
    
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        brief = request.form.get('brief')
        picture = request.files.get('picture')
        content = request.form.get('content')

        # Handling images. Checks file for legal extensions and prevent malicious ones. (..\..\)
        if picture and allowed_file(picture.filename):
            filename = secure_filename(picture.filename)
            #Checking for name conflict
            if name_conflict(filename, UPLOAD_FOLDER):
                #Add random number to conflicting filename
                filename =  str(random.randint(100, 999)) + filename
                flash(f'A similar filename exists... renameing to {filename}', 'danger')
            picture.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img_path = f'static/images/{filename}'

        # Validation. Displays message if error with SQL db or if title is missing.
        if not title:
            flash('Title is required!', 'danger')
        else:
            try:
                # Open a connection to the database
                conn = get_db_connection()
                conn.execute(
                    'INSERT INTO posts (title, brief, content, img_path) VALUES (?, ?, ?, ?)',
                    (title, brief, content, img_path)
                )
                conn.commit()  # Commit the transaction to save the changes
                flash('Post created successfully!', 'success')
            except Exception as e:
                flash(f'An error occurred: {e}', 'danger')
            finally:
                conn.close()

            return redirect(url_for('writings'))
'''

@app.route('/writings')
def writings():
    '''
    Shows all posts by fetching all from SQL db (database.db)
    '''
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('writings.html', posts=posts)

@app.route('/<post_name>')
def post(post_name):
    '''
    Template for posts to display. Data fetched using get_post().
    '''
    post = get_post(post_name)
    visits = view_counter(post_name)
    html = Markup(post['content'])
    return render_template('post.html', post=post, visits=visits, html=html)

# Helper functions

def get_db_connection():
    conn = sqlite.connect('instance/'+'database.db')
    conn.row_factory = sqlite.Row
    return conn

def get_post(post_name):
    # open the connection to db
    conn = get_db_connection()
    # select the post base on it's id
    post = conn.execute('SELECT * FROM posts WHERE post_name = ?', (post_name,)).fetchone()
    # close the connection
    conn.close()
    # checking if we already have the post or not
    if post is None:
        abort(404)
    return post 

def view_counter(page_url):
    '''
    Each time a route is visited, this add up and changes value in the dictionary "view_conut"
    '''
    #page_url : views

    global view_count

    if view_count.get(page_url):
        view_count[page_url] += 1
        return view_count[page_url]
    else:
        view_count[page_url] = 1
        return view_count[page_url]
    
if __name__=="__main__":
    app.run()


