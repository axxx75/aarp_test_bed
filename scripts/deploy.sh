#!/bin/bash
# scripts/deploy.sh
# Script di deploy minimale con problemi di sintassi e quoting

ENV=production
# uso non quotato di variabile che può contenere spazi -> problema
echo Deploying to $ENV

# sintassi non-POSIX: uso di 'function' e array in modo non portabile
function do_deploy() {
    servers=("app1.example.com" "app2.example.com")
    for s in "${servers[@]}"; do
        echo "Deploying to $s"
        ssh ubuntu@$s "mkdir -p /opt/aarp && cp -r ../src /opt/aarp/" || exit 1
    done
}

do_deploy

