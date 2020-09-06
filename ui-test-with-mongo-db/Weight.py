class Weight:
    def __init__(self, userid, value, date, error):
        self.userid = userid
        self.value = value
        self.date = date
        self.error = error


# --------------
# CRUD - WRITE
# --------------


def insert_to_user(mongoconf, userid, weightobject):
    # id
    weightid = 1
    if mongoconf.collection.count_documents({"userid": userid}) > 0:
        weightid = mongoconf.collection.find({"userid": userid}).sort("weightid", -1)[0]["weightid"] + 1

    # insert
    mongoconf.collection.insert_one(
        {"weightid": weightid, "userid": weightobject.userid, "weight": weightobject.value, "date": weightobject.date, "error": weightobject.error})


def insert_csv_to_user(mongoconf, userid, csvfile):
    # id
    weightid = 1
    if mongoconf.collection.count_documents({"userid": userid}) > 0:
        weightid = mongoconf.collection.find().sort("weightid", -1)[0]["weightid"] + 1

    # insert
    for line in csvfile.itertuples():
        mongoconf.collection.insert_one(
            {"weightid": weightid, "userid": userid, "weight": line.kg, "date": line.date, "error": line.error})
        weightid += 1


# --------------
# CRUD - DELETE
# --------------


def delete_by_weight_id(mongoconf, weightid):
    mongoconf.collection.delete_one({"weightid": weightid})


def delete_by_user_id(mongoconf, userid):
    mongoconf.collection.delete_many({"userid": userid})


# --------------
# CRUD - READ
# --------------


def find_by_user_id(mongoconf, userid):
    return mongoconf.collection.find({"userid": userid})


# --------------
# OTHERS
# --------------


def get_collection_count(mongoconf, filter_input):
    return mongoconf.collection.count_documents(filter_input)


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
    if "weights" in fitnessdb.list_collection_names():
        output += "The collection " + "weights" + " exists.\n"

    output += "======================================\n"
    return output
