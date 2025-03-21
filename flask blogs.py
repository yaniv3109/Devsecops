from flask import Flask,request, jsonify


app = (Flask(__name__))

blog_data =[
    {
        "id": 1,
        "title": "First Blog",
        "content": "This is the first blog post",
        "author": "John Doe",
        "date_posted": "2023-05-01"
    },
    {
        "id": 2,
        "title": "Second Blog",
        "content": "This is the second blog post",
        "author": "Jane Smith",
        "date_posted": "2023-05-02"
    },
    {
        "id": 3,
        "title": "Third Blog",
        "content": "This is the third blog post",
        "author": "Bob Johnson",
        "date_posted": "2023-05-03"
    }
]

# GET method
@app.get("/blogs")
def all_blogs():
    print(request.remote_addr)
    print(request.headers["User-Agent"])
    return jsonify(blog_data)


@app.get("/blogs/<number_blog>")
def specific_blog(number_blog):
    for blog in blog_data:
        if blog["id"] == int(number_blog):
            return jsonify(blog), 200
    return "Not found", 404


# POST method
@app.post("/blogs")
def create_blog():
    new_blog = request.json
    if validate_new_blog(new_blog):
        new_blog["id"] = blog_data[-1]["id"]+1
        blog_data.append(new_blog)
        return "New blog created successfully", 201
    return "Missing data", 400

def validate_new_blog(blog):
    if "title" not in blog.keys() or\
        "content" not in blog.keys() or\
        "author" not in blog.keys():
        return False
    return True


# PUT method
@app.put("/blogs/<id>")
def update_blog(id):
    # ממיר את ה-id למספר שלם 
    id = int(id)
    # מקבל את הנתונים החדשים מהבקשה (JSON)
    new_data = request.json

    for blog in blog_data:
        if blog["id"] == id:
            blog.update(new_data)
            return jsonify({"message": "Blog updated successfully"})

    return jsonify({"error": "Blog not found"}), 404


# DELETE method
@app.delete("/blogs/<id>")
def delete_blog(id):
    # ממיר את ה-id למספר שלם
    id = int(id)

    for blog in blog_data:
        if blog["id"] == id:
            # הסרת הבלוג שנמצא מהרשימה
            blog_data.remove(blog)
            return jsonify({"Done": f'blog {blog["id"]} delete'})
    return jsonify({"error": "Blog not found"}), 404
    


if __name__ == '__main__':
    app.run(port=6767, debug=True)