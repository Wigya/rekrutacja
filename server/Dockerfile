FROM python:3.11.5
RUN pip install poetry==1.6.1

WORKDIR /server

COPY pyproject.toml poetry.lock ./

COPY . .
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 8000

CMD ["python3", "application/app.py"]
