from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/showusers')
def show_users():
    response = requests.get(url="http://3.6.93.159:7883/machstatz/get_all_users")
    response.raise_for_status()
    all_users = response.json()
    return render_template("show-users.html", users=all_users)

@app.route('/addusers', methods =["GET", "POST"])
def add_users():
    if request.method == "POST":
        email_id = request.form.get("email_id")
        # getting input with name = fname in HTML form
        first_name = request.form.get("fname")
        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        password = request.form.get("pwd")
        username = request.form.get("uname")
        url = "http://3.6.93.159:7883/machstatz/add_new_user"
        params = {
            'email': email_id,
            'first_name': first_name,
            'last_name': last_name,
            'pwd': password,
            'username': username,
        }
        response = requests.post(url, json=params)
        print(response.text)
    return render_template("add-users.html")

# def delete_user(email):
    # url = "http://3.6.93.159:7883/machstatz/delete_existing_user"
    # params = {
    #     'email': email,
    # }
    # response = requests.delete(url=url, params=params)
    # print(response.text)
    # return render_template("show-users.html")


if __name__=="__main__":
    app.run(debug=True)