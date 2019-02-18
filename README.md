# Overview:

The task is to create a Flask server that will return all animals living in a specific city. 
The result should be returned as JSON.

You have two csv files:
1. master.csv - contains the name of the resident and address (city)
2. pets.csv - contains the name of the pet and owner


## Running the Application

### STEP 1 - Create virtual environment 

Create a virtual environment using python 3. You should do this in the directory of your app or directory with all yours envs.

To create virtual environment:

``` $ virtualenv -p python3 <env_name> ```

To run virtual environment:

``` $ source <env_name>/bin/activate ```


### STEP 2 - Install all of the dependencies

- Flask==1.0.2
- pandas==0.24.1

Make sure you have installed all above extensions. You can install them easily by using the requirements.txt file. 

``` $  pip install -r requirements.txt ```


### STEP 3 - Start-up app

Change path to your directory app and run script

``` $ python3 main.py ```


### STEP 4 - Flask Server

Open your web browser and enter the URL http://127.0.0.1:5000/api/v1/city

city - insert here one of the city names that appear in the csv file. You should see a white screen with the dict.
```
{
"pets": []
}
```

Note: 127.0.0.1 means ‘home’, i.e. this computer. :5000 means ‘port 5000’, which is the port the web server is running on.

### STEP 5 - Docer

You can run app via Docker. Just follow the next steps:

** 5.1 Build the docker image **

$ docker build -t flask-ny-app:latest .

** 5.2 Run the docker container **

Run the docker container from a created image by:

$ docker run -d -p 5000:5000 flask-ny-app

Once again, open your web browser and enter the URL http://127.0.0.1:5000/api/v1/city

