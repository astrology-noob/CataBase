from types import CoroutineType
from flask.templating import render_template
import pymysql as pms

# для сайта
# server: db-learning.ithub.ru
# user: 2p1s14
# password: iamCANCER1

dbh = pms.connect(
        host='db-learning.ithub.ru',
        user='2p1s14',
        password='845-881-014',
        db='2p1s14',
        charset='utf8mb4',
        cursorclass=pms.cursors.DictCursor
    )


def get_id_by_value(value, table_name):
    if value == "" or value == None:
        return pms.NULL
    try:
        with dbh.cursor() as cur:
            cur.execute(f"SELECT id FROM {table_name} WHERE name = '{value}'")
            value_id = cur.fetchall()
            # cur.close()
        return value_id[0]["id"]
    except:
        print("блинб ашиппка(((9((9(")

def get_value_by_id(id, table_name):
    if id == "" or id == None:
        return 'NULL'
    try:
        with dbh.cursor() as cur:
            cur.execute(f"SELECT name FROM {table_name} WHERE id = {id}")
            value_id = cur.fetchall()
            # cur.close()
        return value_id[0]["name"]
    except:
        print("блинб ашиппка(((9((9(")


def insert_cat(val_dict):

    name = val_dict["name"]
    age = val_dict["age"]
    sex_id = get_id_by_value(val_dict["sex"], "project_sex")
    breed_id = get_id_by_value(val_dict["breed"], "project_breeds")
    left_eye_color_id = get_id_by_value(val_dict["left_color"], "project_eye_colors")
    right_eye_color_id = get_id_by_value(val_dict["right_color"], "project_eye_colors")
    fur_color_id = get_id_by_value(val_dict["fur_color"], "project_fur_colors")
    country_id = get_id_by_value(val_dict["country"], "project_countries")
    owner_name = val_dict["owner_name"]
    photo_url = val_dict["photo_url"]
    description = val_dict["desc"]

    # try:
    with dbh.cursor() as cur:

        print(f"INSERT INTO project_cats (name, age, sex_id, breed_id, left_eye_color_id, right_eye_color_id, fur_color_id, country_id, owner_name, photo_url, description) VALUES ('{name}', {age}, {sex_id}, {breed_id}, {left_eye_color_id}, {right_eye_color_id}, {fur_color_id}, {country_id}, '{owner_name}', '{photo_url}', '{description}')")

        cur.execute(f"INSERT INTO project_cats (name, age, sex_id, breed_id, left_eye_color_id, right_eye_color_id, fur_color_id, country_id, owner_name, photo_url, description) VALUES ('{name}', {age}, {sex_id}, {breed_id}, {left_eye_color_id}, {right_eye_color_id}, {fur_color_id}, {country_id}, '{owner_name}', '{photo_url}', '{description}')")
        # cur.close()
    dbh.commit()
    # except:
        # print("блинб ашиппка(((9((9(")

def modify_cat(val_dict, cat_id):

    val_dict["sex"] = get_id_by_value(val_dict["sex"], "project_sex")
    val_dict["breed"] = get_id_by_value(val_dict["breed"], "project_breeds")
    val_dict["left_color"] = get_id_by_value(val_dict["left_color"], "project_eye_colors")
    val_dict["right_color"] = get_id_by_value(val_dict["right_color"], "project_eye_colors")
    val_dict["fur_color"] = get_id_by_value(val_dict["fur_color"], "project_fur_colors")
    val_dict["country"] = get_id_by_value(val_dict["country"], "project_countries")

    cat_info = select_row_by_id(cat_id)

    for i in range(len(cat_info)):
        cat_info_keys = list(cat_info.keys())
        cat_new_keys = list(val_dict.keys())
        if val_dict[cat_new_keys[i]] == pms.NULL and val_dict[cat_new_keys[i]] != cat_info[cat_info_keys[i]]:
            val_dict[cat_new_keys[i]] = cat_info[cat_info_keys[i]]    

    name = val_dict["name"]
    age = val_dict["age"]
    sex_id = val_dict["sex"]
    breed_id = val_dict["breed"]
    left_eye_color_id = val_dict["left_color"]
    right_eye_color_id = val_dict["right_color"]
    fur_color_id = val_dict["fur_color"]
    country_id = val_dict["country"]
    owner_name = val_dict["owner_name"]
    photo_url = val_dict["photo_url"]
    description = val_dict["desc"]
    

    with dbh.cursor() as cur:
        cur.execute(f"UPDATE project_cats SET name = '{name}', age = {age}, sex_id = {sex_id}, breed_id = {breed_id}, left_eye_color_id = {left_eye_color_id}, right_eye_color_id = {right_eye_color_id}, fur_color_id = {fur_color_id}, country_id = {country_id}, owner_name = '{owner_name}', photo_url = '{photo_url}', description = '{description}' WHERE id = {cat_id}")
    dbh.commit()


def delete_row(cat_id):
    with dbh.cursor() as cur:
        cur.execute(f"DELETE FROM project_cats WHERE id = {cat_id}")
    dbh.commit()
    return 0

def select_rows(table_name):
    try:
        with dbh.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name}")
            rows = cur.fetchall()
            # cur.close()
        return rows
    except:
        print("блинб ашиппка(((9((9(")


def select_row_by_id(id):
    # try:
    with dbh.cursor() as cur:
        cur.execute(f"SELECT * FROM project_cats WHERE id = {id}")
        row = cur.fetchall()
        # cur.close()
        try:
            return row[0]
        except:
            return False 
    # except:
    #     print("блинб ашиппка(((9((9(")
