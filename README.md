# Weather Flask Application

This Weather Flask Application is a simple web application that provides weather information for a specified location. It is built using Python and Flask framework.

The Weather Flask Application was created following the tutorial https://dev.to/cscarpitta/creating-a-simple-weather-app-with-python-and-flask-5bpd/ written by initialy  https://dev.to/cscarpitta 

##  Features
  - Retrieve current weather data for a specified location.
  - Display the temperature, humidity, and weather description.
  
## Prerequisites
Before running the application, ensure that the following dependencies are installed:

  - Python 3.x
  - Flask
  - requests
  - having a [OpenWeather](https://openweathermap.org/) account for token/API-KEY 
  
You can install the required packages by running the following command:

```
pip install -r requirements.txt
```

## Getting Started
To set up and run the Weather Flask Application on your local machine, follow these steps:

1. Clone the project repository to your computer
```
git clone https://github.com/sowousmane/Flask.git
```

2. Change to the project directory
```
cd Flask
```

3. Create a virtual environment
```
python3 -m venv env
```

4. Activate the virtual environment

- On macOS and Linux:
```
source env/bin/activate
```
- On Windows:
```
env\Scripts\activate
```

5. Install the required dependencies:
```
pip install -r requirements.txt
```

6. Create a .env file 

```
OPEN_WEATHER_TOKEN=your_weather_token
```
7. Run the application:
```
flask --app weather.py --debug run
```

1. Open your web browser and navigate to http://localhost:5000 to access the Weather Flask Application.
   
## Running with Docker Compose

To run the Weather Flask Application using Docker Compose, follow these steps:

1. Make sure you have Docker and Docker Compose installed on your machine. You can download and install them from the [official Docker website](https://www.docker.com/).

2. Clone the project repository to your computer
```
git clone https://github.com/sowousmane/Flask.git
```

3. Change to the project directory
```
cd Flask
```

4. Create a .env file 

```
OPEN_WEATHER_TOKEN=your_weather_token
``` 

5. Build and start the Docker containers using Docker Compose:
```
docker-compose up -d
```

This command will build the Docker image and start the containers in detached mode.

5. Open your web browser and navigate to `http://localhost:5000/forecast?city=Paris` to access the Weather Flask Application running with Docker Compose.

6. To stop and remove the containers, run the following command in the project directory:

```
docker-compose down
```
This will stop and remove the containers created by Docker Compose.

## List of endpoints
- /forecast?city=<CITY_NAME>
  
### Credits
The Weather Flask Application was developed following the tutorial "Creating a Simple Weather App with Python and Flask" by Carlo Scarpitta.
### License
This project is licensed under the MIT License.


