import subprocess
import sys

import cv2
import imutils
import numpy as np
import json

import pika

from blend_images import blend_images
from marker import get_markers_from_image


def create_heatmap(plan_image, transformed_locations):
    # Create a black image with dimensions of the background
    workspace = np.zeros_like(plan_image)

    # Draw white points on the background
    for [x, y, z] in transformed_locations:
        cv2.circle(workspace, (int(x), int(y)), 1, (255, 255, 255), cv2.FILLED)

    # Apply kernel on the picture
    kernel = np.ones((10, 10), np.float32) / (10*10)
    workspace = cv2.filter2D(workspace, -1, kernel)

    colormap = cv2.applyColorMap(workspace, cv2.COLORMAP_JET)

    colormap[:, :, 0] = np.zeros((colormap.shape[0], colormap.shape[1]))

    return blend_images(plan_image, colormap, (0, 0), 1, 1)


class EventParams:
    def __init__(self, out, image_name, image):
        self.out = out
        self.image_name = image_name
        self.image = image


def click_event(event, x, y, flags, params: EventParams):
    if event == cv2.EVENT_LBUTTONDOWN:
        params.out.append([x, y])
        cv2.circle(params.image, (x, y), 3, (255, 0, 0), 5)
        cv2.imshow(params.image_name, params.image)


def define_points(out, image_name, image):
    cv2.imshow(image_name, image)

    cv2.setMouseCallback(image_name, click_event, EventParams(out, image_name, image))


def perspective_transform(points, transformation):
    mapped_coordinates = []

    for i in range(len(points)):
        scaling_factor = np.matmul(transformation, points[i])
        scaled_coordinates = scaling_factor / scaling_factor[2]
        mapped_coordinates.append(scaled_coordinates)

    return mapped_coordinates


def get_tranformation_matrix(store_points, plan_points):
    original_points = np.float32(store_points)
    destination_points = np.float32(plan_points)

    return cv2.getPerspectiveTransform(original_points, destination_points)


def parse_coordinates(file_path):
    with open(file_path) as file:
        data = json.load(file)

    coordinates = []

    for key in data.keys():
        for element in data[key]:
            coordinates.append([element["x"], element["y"], 1])

    return coordinates


def read_points(out, image_name, image):
    define_points(out, image_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class Config:
    def __init__(self, source, plan, data):
        self.source = source
        self.plan = plan
        self.data = data


def parse_args(args):
    source = args[0]
    plan = args[1]
    data = args[2]
    return Config(source, plan, data)


def get_markers_position():
    cap = cv2.VideoCapture("http://192.168.236.63:8080/video")
    markers = None
    while markers is None:
        _, image = cap.read()
        if image is None:
            continue
        image = imutils.resize(image, width=1920)
        cv2.imshow("Image", image)
        markers = get_markers_from_image(image)

    cap.release()
    cv2.destroyAllWindows()

    return list(markers)[:4]


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) != 3:
        print("Usage: perspective.py source_image plan_image data_file")
        sys.exit(1)

    config = parse_args(args)

    store_image = cv2.imread(config.source)
    plan_image = cv2.imread(config.plan)
    plan_image = cv2.resize(plan_image, (int(np.floor(plan_image.shape[1] / 3)), int(np.floor(plan_image.shape[0] / 3))))

    store_points = []
    plan_points = []

    read_points(store_points, "Store", store_image)
    read_points(plan_points, 'Plan', plan_image)

    people_locations = []

    connection = pika.BlockingConnection()
    channel = connection.channel()

    for method_frame, properties, body in channel.consume("coords"):
        body = str(body, 'utf-8')
        body = json.loads(body)

        for key in body.keys():
            for element in body[key]:
                people_locations.append([element["x"], element["y"], 1])

        transformation_matrix = get_tranformation_matrix(store_points, plan_points)
        transformed_locations = perspective_transform(people_locations, transformation_matrix)

        heatmap = create_heatmap(plan_image, transformed_locations)

        cv2.imshow("Heatmap", heatmap)
        cv2.waitKey(16)
