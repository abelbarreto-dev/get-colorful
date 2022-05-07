# Get Colorful

This project take a picture in gray scale and become it a colorful picture. It takes a grey scale image and change it to a colorful image.

# Requiremtents and Dependencies

What was used to do this project, libraries and API's.

## Libraries

* certifi 2021.10.8
* charset-normalizer 2.0.12
* idna 3.3
* requests 2.27.1
* urllib3 1.26.9

You can found that list at [requirements.txt](requirements.txt), to install that, please run: <code>pip install -r requirements.txt</code>.

## Project API

This project as made with [DeepAI](https://deepai.org/machine-learning-model/colorizer) colorizer API, it is a fantastic project. It's an external API.

It returns a json with an **output url** if ```success``` else an **error message.**

At this project, I did a class, you can find [here.](src/core/api/api_deepai.py) It has two methods:

* Method 1 # Download from an URL;
* Method 2 # Download from a local file;

> Note: I imported the method post as ```deep_ai``` from ```requests```library, it was used to make a request from this API. To come here, it is need to pass to a successful validation process before.


# Project Architecture

Look at how the project organization was thought.

```
    src >
    |   core >
    |   |   api >
    |   |   |   __init__.py
    |   |   |   api_deepai.py
    |   |   facade >
    |   |   |   __init__.py
    |   |   message >
    |   |   |   __init__.py
    |   |   service >
    |   |   |   __init__.py
    |   |   singleton >
    |   |   |   __init__.py
    |   |   utils >
    |   |   |   __init__.py
    |   model >
    |   |   __init__.py
    |   |   picture.py
    |   view >
    |   |   __init__.py
    |   __init__.py
    main.py
    LICENSE
    README.md
    requirements.txt
```

# Project Data Model

The file **[```picture.py```](src/model/picture.py)** is the project model class. It is to save data to make required operation. It has the following parameters:

* ```name -> picture file name;```
* ```source -> picture source, online or local file;```
* ```save -> the path where the file changed must be saved;```
