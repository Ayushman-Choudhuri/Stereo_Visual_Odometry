FROM python:3.9


RUN mkdir -p /usr/stereo_visual_odometry
WORKDIR /usr/stereo_visual_odometry

RUN apt-get update && apt-get install -y 

COPY ./requirements.txt ./ 
COPY ./src ./src


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python3", "./src/stereo_odom.py"]
