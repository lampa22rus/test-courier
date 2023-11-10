FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY ./app .



# RUN alembic upgrade head

# RUN python3.8 main.py --server seed

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]