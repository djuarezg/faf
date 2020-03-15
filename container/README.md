# FAF in Podman container

**Easiest way how to run FAF**
---

## How to deploy

Prerequisites:
A postgres database with semver extension is needed. Using abrt/postgres-semver
image is recommended. Persistent storage is provided by means of a podman volume.
A Redis container is required to run and schedule faf actions from the web UI (see below).
Communication between FAF the database and Redis is ensured by running all three containers
in the same podman pod.

`podman volume create <volume_name>`  
`podman pod create -p 5432:5432 -p 6379:6379 -p 8080:8080 --name <pod_name>`  
`podman run --pod <pod_name> -v <volume_name>:/var/lib/pgsql/data -e POSTGRESQL_ADMIN_PASSWORD=scrt --name db -dit postgres-semver`  

Running FAF is as simple as:

`podman run --pod <pod_name> --name faf -dit -e PGHOST=localhost -e PGUSER=faf -e PGPASSWORD=scrt -e PGPORT=5432 -e PGDATABASE=faf faf-image`

However, if you wish to run and schedule faf actions using the web UI,
you also need to set the necessary environment variables:

`podman run --pod <pod_name> --name faf -dit -e PGHOST=localhost -e PGUSER=faf -e PGPASSWORD=scrt -e PGPORT=5432 -e PGDATABASE=faf -e RDSBROKER=redis://faf-redis:6379/0 -e RDSBACKEND=redis://faf-redis:6379/0 faf-image`

The Redis container can then be downloaded and run as follows:

`podman pull redis:latest`  
`podman run --pod <pod_name> --name faf-redis --hostname faf-redis -dit redis`  

Then FAF is ready for use.

## What's next
You can see incoming reports in webUI. It is accessible on `http://localhost:8080/faf`.

Also to send reports into your own FAF, you have to set up libreport on all
machines, from which you wish to report into your own FAF. To do so, set up
`URL = http://<container_IP>:8080/faf` in `/etc/libreport/plugins/ureport.conf`.

## Configuring FAF
New containers come with fully working and configured FAF (on top of basic configuration
Fedora releases are added, caching is disabled, and FAF accepts unknown components).

To run any FAF action, please run them as faf user.

`podman exec faf faf <action> <arguments>`

## How to build the image
`cd faf/podman`

`make build` to build from copr

`make build_local` to build from currently checked out Github branch

`make build_db` to build database

For easier using and debugging you can use also:

`make run` to run copr version of FAF

`make run_local` to run git version of FAF

`make run_db` to create podman volume (if not yet present) and pod and run database

`make run_redis` to run redis

`make run_all` = `run_db` + `run` + `run_redis`

`make run_all_local` = `run_db` + `run_local` + `run_redis`

`make sh` to jump into bash in the faf container

`make sh_db` to jump into bash in the database container

`make del` to remove faf container

`make del_db` to remove database container and podman pod

`make del_redis` to remove redis container

`make del_all` = `del_redis` + `del` + `del_db`