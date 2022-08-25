# $DEL_BEGIN
FROM python:3.9.7-buster
WORKDIR /prod
COPY design_interface design_interface
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install --upgrade pip
RUN apt-get update && apt install --assume-yes apt-utils
RUN apt-get update && pip install .
RUN apt-get update && pip install opencv-python
RUN apt-get update && apt install --assume-yes libxcb-icccm4  
RUN apt-get update && apt install --assume-yes libxcb-image0 
RUN apt-get update && apt-get install libxcb-util1
#CMD uvicorn design_interface.api.fast:app --host 0.0.0.0 --port $PORT
CMD ["python3","design_interface/MainWindow.py"]
# $DEL_END
