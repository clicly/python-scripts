class User:
    def __init__(self, username, age, sex, exercises):
        self.username = username
        self.age = age
        self.sex = sex
        self.exercises = exercises


# --------------
# CRUD - WRITE
# --------------


def insert(mongoconf, userobject):
    # id
    userid = 1
    if mongoconf.collection.count_documents({}) > 0:
        userid = mongoconf.collection.find().sort("userid", -1)[0]["userid"] + 1

    # insert
    mongoconf.collection.insert_one(
        {"userid": userid, "username": userobject.username, "age": userobject.age,
         "sex": userobject.sex, "exercises": userobject.exercises})


# --------------
# CRUD - DELETE
# --------------


def delete_by_user_id(mongoconf, userid):
    mongoconf.collection.delete_one({"userid": userid})


def delete_by_username(mongoconf, username):
    mongoconf.collection.delete_many({"username": username})


# --------------
# CRUD - READ
# --------------


def read_user_by_id(mongoconf, userid):
    return mongoconf.collection.find_one({"userid": userid})


def read_user_by_name(mongoconf, username):
    return mongoconf.collection.find_one({"username": username})


def read_all_users(mongoconf):
    return mongoconf.collection.find()

# --------------
# OTHERS
# --------------


def get_collection_count(mongoconf, filter):
    return mongoconf.collection.count_documents(filter)


# --------------
# TEST DB
# --------------


def test_db(mongoconf):
    output = ""
    output += "======================================\n"
    # output += "".join(mongoconf.client.list_database_names())
    if "fitness" in mongoconf.client.list_database_names():
        output += "The database " + "fitness" + " exists.\n"

    fitnessdb = mongoconf.client["fitness"]

    # print(database.list_collection_names())
    if "users" in fitnessdb.list_collection_names():
        output += "The collection " + "users" + " exists.\n"

    output += "======================================\n"
    return output
