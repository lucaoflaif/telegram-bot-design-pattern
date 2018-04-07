from env import ENV as env

### This is an example of a Mongo DB connection using the dotenv file ###

# MONGO_HOST = env.get("MONGO_HOST")
# MONGO_PORT = int(env.get("MONGO_PORT"))

# DATABASE_NAME = env.get("MONGO_DATABASE_NAME")

# the CONNECTION var will be imported in the core.py file, don't rename it
# unless you want to change its import statement

# CONNECTION = mongoengine.connect(db=DATABASE_NAME,
#                                  host=MONGO_HOST,
#                                  port=MONGO_PORT)