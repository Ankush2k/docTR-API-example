# docTR-API-example

To use Doctr Library as an api with custom function using FastAPI.
This is a POC to implement doctr with FastAPI.

Pre-requisite can be refereced from https://github.com/mindee/doctr.

Dockerized the app to use doctr as api.

Follow below steps to replicate the setup.

1. Clone the environment,
    
     git clone https://github.com/Ankush2k/docTR-API-example
2. Run the below command to build image,
    
    docker build . -t doc_api 
3. Now run the below command to run the docker and expose desired port,

    docker run -p 8000:80 doc_api

