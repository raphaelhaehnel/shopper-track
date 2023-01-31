import cv2
import imutils


def map_corners_to_centers(corners):
    centers = []

    for corner in corners:
        (topLeft, topRight, bottomRight, bottomLeft) = corner.reshape(4, 2)
        marker_x = int((int(topLeft[0]) + int(bottomRight[0])) / 2.0)
        marker_y = int((int(topLeft[1]) + int(bottomRight[1])) / 2.0)
        centers.append((marker_x, marker_y))

    return centers


def get_markers_from_image(image):
    image = imutils.resize(image, width=600)

    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    aruco_params = cv2.aruco.DetectorParameters_create()
    (corners, ids, _) = cv2.aruco.detectMarkers(image, aruco_dict, parameters=aruco_params)

    if len(corners) < 4:
        return None

    ids = ids.flatten()

    return zip(ids, map_corners_to_centers(corners))


if __name__ == '__main__':
    cap = cv2.VideoCapture("http://192.168.236.63:8080/video")

    markers = None

    while markers is None:
        _, image = cap.read()
        cv2.imshow("Image", image)
        markers = get_markers_from_image(image)

    for marker in markers:
        print(marker)
