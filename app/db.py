from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017") # Adjust if needed
db = client["CDF"]                       
collection = db["polytgotcoll"]    

# Define JSON Schema
schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["source_type", "sub_source", "file_type", "ingested_at", "metadata", "content"],
        "properties": {
            "source_type": { "bsonType": "string" },
            "sub_source": { "bsonType": "string" },
            "file_type": { "bsonType": "string" },
            "ingested_at": { "bsonType": "date" },
            "metadata": {
                "bsonType": "object",
                "additionalProperties": True
            },
            "content": {
                "bsonType": "object",
                "required": ["normalized", "raw", "enriched"],
                "properties": {
                    "normalized": { "bsonType": "object", "additionalProperties": True },
                    "raw": { "bsonType": "string" },
                    "enriched": { "bsonType": "object", "additionalProperties": True }
                }
            }
        }
    }
}

# Apply validator (if collection exists, use collMod)
try:
    db.create_collection("polytgotcoll", validator=schema)
except Exception as e:
    # If already exists, modify the collection
    db.command({
        "collMod": "polytgotcoll",
        "validator": schema,
        "validationLevel": "strict"
    })
