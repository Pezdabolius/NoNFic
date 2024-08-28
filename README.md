# NoNFic

It's a digital platform that allows users to browse and purchase non-fiction literature.

## Quickstart

Run the following commands to bootstrap your environment:

    git clone https://github.com/Pezdabolius/NoNFic.git

    python -m venv my_venv
    my_venv\Scripts\activate
    pip install -r requirements.txt

    create .env file and fill it in

## Run the app with waitress:
    docker compose up
    docker compose exec webapp python manage.py loaddata db.json
    
    
