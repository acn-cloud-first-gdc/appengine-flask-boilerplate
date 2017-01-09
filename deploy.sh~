#!/usr/bin/env bash
function usage {
    cat << EOF

<Usage>: deploy.sh <environment> [version]

Deploys this appengine application to the designated environment (dev/qa/prod).

EOF
   exit 1
}

environment=$1

if [ $# -gt 2 ] || [ $# -lt 1 ]; then
    usage;
fi

gitHash=`git rev-parse --short HEAD`
version=$gitHash

if [ $# -eq 2 ]; then
    version="$2-$gitHash"
fi

if [ "$environment" = "dev" ]; then
    projectId="dev"
    nopromote=""
fi

if [ "$environment" = "qa" ]; then
    projectId="qa"
    nopromote=""
fi

if [ "$environment" = "prod" ]; then
    projectId="prod"
    nopromote=" --no-promote"
fi

cp configurations/${environment}.yaml env_variables.yaml
(gcloud app deploy app.yaml queue.yaml cron.yaml index.yaml --project=$projectId --version=$version $nopromote)
