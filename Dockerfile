# 
FROM python:3.9.11
# 
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
# 
COPY ./.env /code/.env
#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# 
COPY ./app /code/app
# 
COPY ./main.py  /code/main.py 
# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["uvicorn", "main:app", "--proxy-headers", "--port", "80"]
