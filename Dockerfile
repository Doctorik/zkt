FROM python:3.9-alpine
WORKDIR /app
COPY ./app.py /app
COPY ./index.html /app/templates/index.html
COPY ./add_blog.html /app/templates/add_blog.html
RUN pip install Flask Flask-RESTful
RUN pip install psycopg2-binary

EXPOSE 5000
ENV FLASK_APP app.py
CMD ["flask", "run", "--host=0.0.0.0"]
