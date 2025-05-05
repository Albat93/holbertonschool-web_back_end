#!/usr/bin/env python3
from pymongo import MongoClient

"""
This module is a script that provides some stats about Ngins Logs stored in BDD
"""


def nginx_stats():
    """
    function that provides some stats about Nginx Logs stored in MongoDB
    """
    client = MongoClient()
    db = client.logs  # accede à la bdd logs
    collection = db.nginx  # accède à la collection nginx dans la bdd logs

    # total logs
    total_logs = collection.count_documents({})  # compte le nombre de docs
    # {} est vide donc on compte tous les documents de la collection
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
    print(f"\t{method}: {count}")

    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
        })
    print(f"method=GET path=/status: {status_count}")

    if __name__ == "__main__":
        nginx_stats()
