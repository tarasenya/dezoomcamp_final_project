#!/bin/bash
cd ..
prefect server start & 
sleep 10 && prefect worker start -p general_worker -t process &
sleep 20 && prefect deploy --all --ci && prefect deployment run 'Initial koalas sighting to BQ/initial-ingestion-deployment'