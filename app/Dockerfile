# start from an official image
FROM python:3.8

# directory of Django installation
RUN mkdir -p /opt/codeleap/
WORKDIR /opt/codeleap/

# copy project code to installation folder
COPY . /opt/codeleap/

# install dependencies
RUN pip install -r requirements.txt

# expose the port 8000
EXPOSE 8000

# migrate database
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "codeleap", "--bind", ":8000", "codeleap.wsgi:application"]