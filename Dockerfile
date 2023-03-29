FROM python:3.11

WORKDIR /
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8003

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:8003", "-k", "uvicorn.workers.UvicornWorker", "rrhh_personal.app:create_app" ]
