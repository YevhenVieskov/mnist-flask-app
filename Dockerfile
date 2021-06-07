FROM python:3.7

RUN python -m pip install flask flask-cors gunicorn numpy tensorflow pillow

WORKDIR /app

COPY image.py image.py
COPY run.py run.py
COPY classifier.py classifier.py
COPY model   model
COPY static  static
COPY templates templates

EXPOSE 5000

CMD python app.py

