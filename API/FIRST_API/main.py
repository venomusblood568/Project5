# GET == for requesting some kind of data or resources
# POST == for creating a resource 
# PUT == for updating a resource 
# DELETE == for removing or deleteing a resource
from flask import Flask, request,jsonify

#root 
app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    # this is the data which will be printing
    user_data = {
        "user_id" : user_id,
        "name": "SAM",
        "email":"sammy_world@gmail.com"      
    } 
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200 #200 is succesfull code for http and https their are several other code  like series 100,200,300,400,500 etc


if __name__ ==  "__main__":
    app.run(debug=True)

# for some reason I can't see the url so here it is = http://127.0.0.1:5000/get-user/123?extra=%22hello%22
