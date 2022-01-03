from flask import Flask, request, render_template, redirect, url_for
import db_context

app = Flask(__name__)

sex_options = db_context.select_rows("project_sex")
breed_options = db_context.select_rows("project_breeds")
eye_color_options = db_context.select_rows("project_eye_colors")
fur_color_options = db_context.select_rows("project_fur_colors")
country_options = db_context.select_rows("project_countries")

@app.route("/editcat", methods=["POST", "GET"])
def edit_cat():
    message=""
    
    cat_id = request.args.get("cat_id")

    cat = db_context.select_row_by_id(cat_id)

    if cat:
        cat_info = {
            "name": cat["name"],
            "age": cat["age"],
            "sex": db_context.get_value_by_id(cat["sex_id"], "project_sex"),
            "breed": db_context.get_value_by_id(cat["breed_id"], "project_breeds"),
            "left_eye": db_context.get_value_by_id(cat["left_eye_color_id"], "project_eye_colors"),
            "right_eye": db_context.get_value_by_id(cat["right_eye_color_id"], "project_eye_colors"),
            "fur_color": db_context.get_value_by_id(cat["fur_color_id"], "project_fur_colors"),
            "country": db_context.get_value_by_id(cat["country_id"], "project_countries"),
            "owner": cat["owner_name"],
            "photo_url": cat["photo_url"],
            "description": cat["description"]
        }

    if request.method == "POST":
        if request.form.get('submit'):
            form_values = request.form.to_dict()
            db_context.modify_cat(form_values, cat_id)
            message = f"Cat {form_values['name']} successfully modified!"

        elif request.form.get('delete'):
            db_context.delete_row(cat_id)
            return redirect(url_for("index", message=f"Cat with id {cat_id} successfully deleted!"))

    return render_template("addcat.html", cat_info=cat_info, sex_options=sex_options, breed_options=breed_options,
    eye_color_options = eye_color_options, fur_color_options=fur_color_options, country_options = country_options, message=message)


@app.route("/addcat", methods=["POST", "GET"])
def add_cat():

    cat_info = {
        "name": "",
        "age": "",
        "sex": "",
        "breed": "",
        "left_eye": "",
        "right_eye": "",
        "fur_color": "",
        "country": "",
        "owner": "",
        "photo_url": "",
        "description": "",
    }

    message=""


    if request.method == "POST":
        form_values = request.form.to_dict()
        db_context.insert_cat(form_values)
        message = f"Cat {form_values['name']} successfully added to CataBase!"


    return render_template("addcat.html", cat_info=cat_info, sex_options=sex_options, breed_options=breed_options,
    eye_color_options = eye_color_options, fur_color_options=fur_color_options, country_options = country_options, message=message)


@app.route("/searchcat", methods=["POST", "GET"])
def search_cat():
    cats = db_context.select_rows("project_cats_view")

    if request.method == "GET":

        # для поиска кота по фильтрам

        return render_template("searchcat.html", cats=cats)

    return render_template("searchcat.html", cats=cats)


@app.route("/", methods=["POST", "GET"])
def index(message=""):

    if request.method == "POST":

        cat_id = request.form.get("cat_id")

        cond = db_context.select_row_by_id(cat_id)

        if cond:
            return redirect(url_for("edit_cat", cat_id=cat_id))
        else:
            return render_template("index.html", message=f"Cat with id {cat_id} does not exist")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host='db-learning.ithub.ru', port='1114')