#!/usr/bin/env python3
"""Module that returns a list of schools having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic (str): The topic to search for.

    Returns:
        List of documents (schools) matching the topic.
    """
    return list(mongo_collection.find({ "topics": topic }))
