# Pull python image
FROM python:3.6

# Create a work dir
WORKDIR /usr/src/app

# copy requirements.txt into workdir created above
COPY requirements.txt ./

# Install all requirements
RUN python -m pip install --user --no-cache-dir -r requirements.txt

# Copy entire project into workdir
COPY . .

# Run our app
CMD ["python", "collector-es-elmundo.py"]
