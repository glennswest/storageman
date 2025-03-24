podman stop rqlite
podman rm rqlite
podman volume rm rqlite-data
podman volume create rqlite-data -o device=/volumes/rqlite -o=o=bind

podman run -d -v rqlite-data:/rqlite:rw,Z --name rqlite -p 4001:4001 docker.io/rqlite/rqlite
