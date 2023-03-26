# Aws event driven data processing
> This application showed connection in aws services and return event when user make any changes in files.
> Live demo [_here_](http://mateuszgua.pythonanywhere.com/).

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Project Status](#project-status)
* [Contact](#contact)

## General Information
- This project was created because I wanted run project in aws services.
- I wanted to create application with notifications and queue solution.


## Technologies Used
- Python - version 3.10.6


## Features
List the ready features here:
- Create a user in IAM console,
- Create an S3 bucket, 
- Create a policy and add it to user,
- Create connection with external API and get dummy data for user in json file,
- Upload json file into AWS S3 bucket
- Create eventbridge rules for monitor when object is creating,
- Create sns notification for email,
- Create lambda function,
- Create sqs connection with sns and lambda,
- Create json reader, create dataframe from json and write file in parquet into S3 bucket
- Create parquet file reader in app

## Screenshots
Schematic diagram
![Example screenshot](./static/func-diagram.png)
Page with project workflow
![Example screenshot](./static/pythonanywhere.png)

## Project Status
Project is: in_progress


## Contact
Created by [@DevGua]() - feel free to contact me!