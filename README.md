# Scrapping_Twitch
Ongoing project to scrap Twitch.tv

*This is the Dev BRanch*

> Information :
The documentation is located : **[Here](htts://github.com/Scraping_Twitch)**

### This is a project made at **ESIEE Paris** for the **DataEngineering** course.

# TO DO 
-[] faire un pipfile pour chaque service ?

When you have multiple Dockerfiles, each representing a different service in your application, it's a good practice to have a separate Pipfile for each service. This is because each service may have different dependencies, and separating them allows for better isolation and control over the dependencies of each service.

In your project structure, you might have a separate directory for each service, and each directory would contain its own Dockerfile and Pipfile. This way, when you build the Docker image for a particular service, it only installs the dependencies that are necessary for that service.

Here's an example of how your project structure might look:

```
.
├── service1
│   ├── Dockerfile
│   └── Pipfile
└── service2
    ├── Dockerfile
    └── Pipfile
```

In each Dockerfile, you would copy the corresponding Pipfile and install the dependencies like this:

```dockerfile
# Dockerfile for service1
FROM python:3.11.2

WORKDIR /app

COPY ./Pipfile /app/Pipfile
COPY ./Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv && pipenv install --system --deploy

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

This approach ensures that each service has its own isolated environment with only the necessary dependencies installed.