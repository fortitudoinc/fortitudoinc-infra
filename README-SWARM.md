## Initialize Swarm
```
docker swarm init
docker service create --name registry --publish published=5000,target=5000 registry:2
```

## Build Images
```
cd fortitudoinc-infra/
docker-compose -f load-db.yml build
```

## Deploy Stack
```
docker stack deploy --compose-file load-db.yml openmrs
```