FROM python:3.7

# Set work directory.
WORKDIR /usr/src/app

# Set environment variables.
ENV DEBUG false

# Install requirements.
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copy project files into container.
COPY . .

# Add and run as non-root user.
RUN useradd -ms /bin/bash exercise
USER exercise

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
