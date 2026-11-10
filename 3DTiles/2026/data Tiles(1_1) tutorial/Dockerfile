# Workspace voor de 3D Tiles 1.1-tutorial: 3d-tiles-validator en http-server.
# De tiles zelf maak je in de tyler-container (zie docker-compose.yml).
FROM node:22.20.0-alpine3.22

# Tool versions (override with: docker compose build --build-arg TILES_VALIDATOR_VERSION=...)
ARG TILES_VALIDATOR_VERSION=0.6.1
ARG HTTP_SERVER_VERSION=14.1.1

# better-sqlite3 (dependency of 3d-tiles-validator) has no prebuilt binary for musl,
# so it is compiled from source; build tools are removed afterwards.
RUN apk add --no-cache --virtual .build-deps python3 make g++ \
    && npm install -g \
        "3d-tiles-validator@${TILES_VALIDATOR_VERSION}" \
        "http-server@${HTTP_SERVER_VERSION}" \
    && npm cache clean --force \
    && apk del .build-deps

WORKDIR /workspace

# Keep the container running so you can work in it with: docker exec -it workspace11 sh
CMD ["sleep", "infinity"]
