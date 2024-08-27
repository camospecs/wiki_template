import sqlite3 as sqlite

'''
This tool is how I add posts to my website. Users are asked for key details and then this is submited to the sql db.
'''

def prompt_user():
    print('DB Post Builder.')
    title = input('Title: ')
    brief = input('Brief: ')
    c1 = input('HTML File: ') # Max 2500 chars
    c2 = input('HTML File: ')
    c3 = input('HTML File: ')
    c4 = input('HTML File: ')
    c5 = input('HTML File: ')
    img_path = '/static/images/' + input('Head Image Name: ')
    post_name = title.lower().replace(' ', '-')

    content = c1 + c2 + c3 + c4 +c5

    return title, brief, content, img_path, post_name


def add_post(title, brief, content, img_path, post_name):
    #Makes a connection to the db, created new  one if it doesn't wxist
    connection = sqlite.connect('database.db')

    with open('schema.sql') as f:
        connection.executescript(f.read())

    # make the cursor to execute what inside the schema in database
    cur = connection.cursor() 
    cur.execute("""INSERT INTO posts (title, brief, content, img_path, post_name) VALUES (?, ?, ?, ?, ?)""",
            (title, brief, content, img_path, post_name)
            )
    connection.commit()
    connection.close()
    
if __name__=="__main__":
    title, brief, content, img_path, post_name = prompt_user()
    add_post(title, brief, content, img_path, post_name)