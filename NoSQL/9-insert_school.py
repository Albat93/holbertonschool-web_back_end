#!/usr/bin/env python3
"""Module that inserts a new document in a MongoDB collection."""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        **kwargs: Key-value pairs to insert as the document.

    Returns:
        The new document _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
