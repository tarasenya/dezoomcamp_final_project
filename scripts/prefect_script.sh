#!/bin/bash
cd ..
prefect server start & 
sleep 5 && prefect worker start -p general_worker -t process &
sleep 25 && prefect deploy --all --ci && prefect deployment run 'Initial koalas sighting to BQ/initial-ingestion-deployment'