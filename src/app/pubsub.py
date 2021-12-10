# -*- coding: utf-8 -*-
from google.cloud import pubsub_v1
import os

def publish_new_score_topic(msg):
    project_id = os.environ.get('GCP_PROJECT')
    topic_id = "topic-new-score-created"
    publisher = pubsub_v1.PublisherClient()
    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_id}`
    topic_path = publisher.topic_path(project_id, topic_id)
    # Data must be a bytestring
    data = msg.encode("utf-8")
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())
    print(f"Published messages to {topic_path}.")
    return future

if __name__ == '__main__':
    publish_new_score_topic('{"cpf":123456789,\
        "request_datetime":"2021-01-01", \
        "score":750, "status":"APROVADO"}')