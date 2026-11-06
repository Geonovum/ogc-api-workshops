# GDAL on Alpine. Pinned to a stable release: "alpine-small-latest" is a nightly dev build.
FROM ghcr.io/osgeo/gdal:alpine-small-3.13.3

# Tool versions (override with: docker compose build --build-arg PG2B3DM_VERSION=...)
ARG PG2B3DM_VERSION=2.18.1
ARG I3DM_EXPORT_VERSION=2.11.0
ARG TILES_VALIDATOR_VERSION=0.6.1
ARG HTTP_SERVER_VERSION=14.1.1

# Runtime dependencies:
# - nodejs/npm: 3d-tiles-validator and http-server
# - postgresql-client: psql
# - gcompat, icu-libs, libstdc++: needed by the .NET binaries pg2b3dm and i3dm.export
RUN apk add --no-cache \
    nodejs \
    npm \
    postgresql-client \
    curl \
    unzip \
    gcompat \
    icu-libs \
    libstdc++

# npm packages. better-sqlite3 (dependency of 3d-tiles-validator) has no prebuilt
# binary for musl, so it is compiled from source; build tools are removed afterwards.
RUN apk add --no-cache --virtual .build-deps python3 make g++ \
    && npm install -g \
        "3d-tiles-validator@${TILES_VALIDATOR_VERSION}" \
        "http-server@${HTTP_SERVER_VERSION}" \
    && npm cache clean --force \
    && apk del .build-deps

# pg2b3dm and i3dm.export (Geodan), downloaded zips are removed in the same layer
RUN set -eux; \
    cd /tmp; \
    curl -fsSL -o pg2b3dm.zip \
        "https://github.com/Geodan/pg2b3dm/releases/download/v${PG2B3DM_VERSION}/pg2b3dm-linux-x64.zip"; \
    curl -fsSL -o i3dm.export.zip \
        "https://github.com/Geodan/i3dm.export/releases/download/v${I3DM_EXPORT_VERSION}/i3dm.export-linux-x64.zip"; \
    unzip -o pg2b3dm.zip -d /usr/local/bin; \
    unzip -o i3dm.export.zip -d /usr/local/bin; \
    chmod +x /usr/local/bin/pg2b3dm /usr/local/bin/i3dm.export; \
    rm -f /tmp/*.zip /usr/local/bin/*.pdb

WORKDIR /workspace

# Keep the container running so you can work in it with: docker exec -it workspace sh
CMD ["sleep", "infinity"]
