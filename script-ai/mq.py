import json

import pika

if __name__ == "__main__":
    connection = pika.BlockingConnection()
    channel = connection.channel()

    for method_frame, properties, body in channel.consume("coords"):
        body = str(body, 'utf-8')
        body = json.loads(body)
        print(body)
