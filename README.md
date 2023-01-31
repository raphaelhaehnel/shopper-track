![image](https://user-images.githubusercontent.com/69756617/215852417-8d4304ed-195f-4b70-a93d-47a83a74b9d7.png)

## Abstract

ShopperTrack is a project we started during the 6th Hackathon "Great Minds 6" of the Jerusalem College of Technology of Jerusalem.
We are a team of 4 students: Raphael Haehnel, Hillel Saal, Yehochoua Lalou and Chmouel Hai Illouz.
We developped a software based on machine learning and computer vision to analyze the activity of the customer in a shop from the video cameras of the shop. Our product detects people in the shop and create a map that contains the informations about the positions of the customers inside the shop, where they use to gather, their favorite path, which products they choose. From this data we collect, we are able to easily understand how the shop infrastructure is accessible and user-friendly.

The technologies with use: Numpy, Nvidia Cuda, PyTorch (Yolo), RabbitMQ


## Usage

There are two script we are running in parallel: the Yolo algorithm to detect the people on one hand, and the watcher script on the other hand that receive the messages from the first script and dispatch them to the function that generate the heatmap of the shop

Image from the video cameras

![image](https://user-images.githubusercontent.com/69756617/215865908-15b7c41c-42ac-4856-8730-7b040d469622.png)

Generation of the heatmap

![image](https://user-images.githubusercontent.com/69756617/215865951-ac57280f-2883-4a18-be78-57edeaece24c.png)





