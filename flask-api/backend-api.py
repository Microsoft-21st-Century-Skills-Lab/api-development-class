# Import packages
from flask import Flask, jsonify, abort,Response


# Instantiate flask
app = Flask(__name__)

blogs = [
    {'id':1, 'title':'First Blog', 'content':'dshhdshdsdhsdhfhsfghsjgfhsgdjsdksjgfjskfjs', 'Author':'Rashid'},
    {'id':2, 'title':'Second Blog', 'content':'dshhdshdsdhsdhfhsfghsjgfhsgdjsdksjgfjskfjs', 'Author':'Yanet'},
    {'id':3, 'title':'Third Blog', 'content':'dshhdshdsdhfffghsjgfhsgdjsdksjgfjskfjs', 'Author':'Opiyo'}
]

# Hello world API
@app.route('/', methods=['GET'])
def home():
    '''Hello world.'''
    return "Hello World"


@app.route('/blogs', methods=['GET'])
def get_blogs():
    '''Get a list a of blogs'''
    return jsonify(blogs)



@app.route('/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    '''Get a blogs
    @params:
    blog_id - '''
    blog = next((item for item in blogs if item['id'] == blog_id), None)    
    if blog is None:
        return jsonify({"message":"Resource not found"}), 404
    return jsonify({"blog":blog})



if __name__ =='__main__':
    app.run(debug=True, port=5000)