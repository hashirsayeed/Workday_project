import json
from pymongo import MongoClient

#database connection
def db_connect():
    try:
        client = MongoClient("mongodb+srv://hashirsayeed:W7mgODAvAxN0Wyrx@cluster0.hadfslk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client['etl_test']
        collection = db['etl'] 
        return collection
    except Exception as e:
        print("Error while connecting to database!")

def load_data(collection, data):
    try:
        collection.insert_many(data)
    except Exception as e:
        print("Error while uploading data to database!")


#retrieving data from files
def get_data(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
        return data
    except Exception as e:
        print("Error while retrieving data from req.json file!!", e)

#transform data 
def data_transform(req_data, app_data, user_data):
    try:
        #performing merging req data and application data based on req_id
        merged_data = []
        for r in req_data:
            r_copy = r.copy()
            r_copy["applications"] = [app for app in app_data if app["req_id"] == r["req_id"]]
            merged_data.append(r_copy)
        
        #performing the final merge with user data based on name
        for m in merged_data:
            for app in m['applications']:
                for user in user_data:
                    if app["candidate_name"] == user["name"]:
                        app["email"] = user["email"]
                        app["role"] = user["role"]
        return merged_data
    
    except Exception as e:
        print(e)

if __name__ == "__main__":

    try:
        #gathering data
        files_list = ["req.json", "application.json", "user.json"]
        for i in range(len(files_list)):
            if i == 0:
                req_data = get_data(files_list[i])
            elif i == 1:
                app_data = get_data(files_list[i])
            else:
                user_data = get_data(files_list[i])
        #merging data
        merged_data = data_transform(req_data, app_data, user_data)
        #database connection
        collection = db_connect()
        #upload data
        load_data(collection, merged_data)

    except Exception as e:
        print("Error in main!", e)