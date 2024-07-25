# Import packages
from flask import Flask, jsonify, abort,Response, request


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

# Delete blog

@app.route('/blogs/delete/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    '''Delete blog
    @params:
    blog_id - '''
    for blog in blogs:
        if blog['id'] == blog_id:
            blogs.remove(blog)
            return jsonify({"msg": "Blog deleted successfully", "blog":blog}), 200
    return jsonify({"msg":"Resource not found"})

# Add blog
@app.route('/blogs/addblog', methods=['POST'])
def add_blog():
    '''Add blog'''
    data = request.json
    
    if not data or 'title' not in data or 'content' not in data or 'Author' not in data:
        return jsonify({'error':'Please fill all the fields'}), 400
    new_blog = {
        'id':len(blogs) +1,
        'title':data['title'],
        'content':data['content'],
        'Author':data['Author']
        }
    blogs.append(new_blog)
    return jsonify({"msg":"Blog added successfully."}), 201

# patch blog
@app.route('/blogs/updateblog/<int:blog_id>', methods=['PATCH'])
def patch_blog(blog_id):
    '''Update blog'''
    data = request.json
    blog = next((item for item in blogs if item['id'] == blog_id), None)
    
    if not data or 'title' not in data or 'content' not in data or 'Author' not in data:
        return jsonify({'error':'Please fill all the fields'}), 400
    new_blog = {
        'id':len(blogs) +1,
        'title':data['title'],
        'content':data['content'],
        'Author':data['Author']
        }
    blogs.append(new_blog)
    return jsonify({"msg":"Blog added successfully."}), 201

# put blog
@app.route('/blogs/updateblog/<int:blog_id>', methods=['PUT'])
def put_blog(blog_id):
    '''Update blog'''
    data = request.json
    
    if not data or 'title' not in data or 'content' not in data or 'Author' not in data:
        return jsonify({'error':'Please fill all the fields'}), 400
    
    blog = next((item for item in blogs if item['id'] == blog_id), None)
    
    if blog is None:
        return jsonify({"message":"Resource not found"}), 404
    
    blog['title'] = data['title']
    blog['content'] = data['content']
    blog['Author'] = data['Author']
    
    return jsonify({"msg":"Blog updated successfully."}), 200







if __name__ =='__main__':
    app.run(debug=True, port=5000)