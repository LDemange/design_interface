# $DEL_BEGIN
FROM python:3.9.7-buster
WORKDIR /prod
COPY design_interface design_interface
COPY requirements.txt requirements.txt
COPY setup.py setup.py
RUN pip install .
#RUN pip install opencv-python
#RUN pip install opencv-python-headless
RUN dpkg -i design_interface/libxcb-util1_0.4.0-0ubuntu3_amd64.deb
RUN apt-get update && apt-get install --assume-yes libgl1
RUN apt-get install -y --assume-yes libxcb-.
RUN apt-get install -y --assume-yes libxkb.
RUN apt-get install -y --assume-yes libdbus.


#CMD uvicorn design_interface.api.fast:app --host 0.0.0.0 --port $PORT
CMD ["python3","design_interface/MainWindow.py"]
# $DEL_END
