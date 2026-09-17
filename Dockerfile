FROM python:3.14.6
WORKDIR /mithila
COPY requirements.txt /mithila
RUN pip install -r requirements.txt 
RUN ls
COPY . /mithila
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
# RUN python manage.py runserver  never ending loop chalxa.

# FROM python:3.14.6
# WORKDIR /mithila
# COPY requirements.txt .
# RUN pip install -r requirements.txt 
# COPY . .
# EXPOSE 8000
# CMD ["python","manage.py","runserver"]

