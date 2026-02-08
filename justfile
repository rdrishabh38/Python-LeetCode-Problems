# Starts the Postgres container in detached mode
up:
    docker compose up -d

# Stops and removes the Postgres container
down:
    docker compose down