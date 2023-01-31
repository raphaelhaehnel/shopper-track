# ShopperTrack

## Abstract

ShopperTrack is a project we started during the 6th Hackathon "Great Minds 6" of the Jerusalem College of Technology of Jerusalem.
We worked as a team

The technologies with use: numpy, Nvidia Cuda, PyTorch, RabbitMQ

System diagram of the project

![image](https://user-images.githubusercontent.com/69756617/211169838-2ba0407d-f7e7-4302-afd0-f9e7417e5153.png)

## Usage

The system is controlled by Arduino. To communicate with the computer, we used the protocol Pyfirmata, which allows us to control the Arduino with Python.

This is the main window of the program

![mainwindow](https://user-images.githubusercontent.com/69756617/207135927-f3a22cb2-5cf5-44b5-bc76-adf4b824263d.png)

On this window you can define the differents parameters for the electromagnets

![parameters](https://user-images.githubusercontent.com/69756617/207139507-4ffa3687-1687-4003-87f8-67ed1e39de06.png)

## Circuit schematic

Bellow, the schematic of the circuit we build to control the electromagnets. The two electromegnets are represented by two coils, and the Arduino outputs are represented by the inputs T1 and T2.

<img src="https://user-images.githubusercontent.com/69756617/211169716-2d81b760-e7f6-4d58-947c-b6ec2a8daf05.png" width="500" />

We used NMOS power transistors to control the power on the electromagnets. MOSFET transistors with their heat sink

![image](https://user-images.githubusercontent.com/69756617/211169973-ee6498af-5eee-46d9-ab77-fc78d32cb4e5.png)

#### updates log

18.05.2020 - first update

12.12.2022 - readme updated