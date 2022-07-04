FROM python:3.9

RUN pip install django

WORKDIR /usr/src/app

COPY requirements.txt ./ 

RUN pip install -r requirements.txt

COPY . . 

EXPOSE 8000   

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "kolon_wecode.wsgi:application"]  
