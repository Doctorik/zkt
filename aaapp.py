from flask import Flask, request, render_template, jsonify, redirect
from flask_restful import Resource, Api
import psycopg2
import os

app = Flask(__name__)
api = Api(app)


def get_db_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    return psycopg2.connect(DATABASE_URL)


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blog_posts (
            id SERIAL PRIMARY KEY,
            title VARCHAR(100) NOT NULL,
            content TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()


class BlogPost(Resource):
    def get(self, post_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM blog_posts WHERE id = %s', (post_id,))
        post = cursor.fetchone()
        cursor.close()
        conn.close()
        if post:
            return {'id': post[0], 'title': post[1], 'content': post[2]}
        else:
            return {'message': 'Príspevok nenájdený'}, 404

    def post(self):
        data = request.get_json()  
        title = data['title']
        content = data['content']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO blog_posts (title, content) VALUES (%s, %s) RETURNING id;', (title, content))
        post_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()

        return {'id': post_id, 'title': title, 'content': content}, 201


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM blog_posts ORDER BY id DESC')
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/pridat')
def pridat():
    return render_template('add_blog.html')


@app.route('/pridat_prispevok', methods=['POST'])
def pridat_prispevok():
    title = request.form['title']
    content = request.form['content']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO blog_posts (title, content) VALUES (%s, %s) RETURNING id;', (title, content))
    post_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


api.add_resource(BlogPost, '/api/blogpost', '/api/blogpost/<int:post_id>')

if __name__ == '__main__':
    init_db() 
    app.run(debug=True, host='0.0.0.0')
