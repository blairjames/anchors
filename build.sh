#!/usr/bin/env bash

source /root/.ssh/agent/root || . /root/.ssh/agent/root

echo $(date) > /home/docker/anchors/log.build

function timestamp () {
    date +"%Y%m%d_%H%M%S"
}

#function () {
#     
#}


docker build . -t blairy/anchors:$(timestamp) || echo 'Docker Build Failed!' 

git="/usr/bin/git -C /home/docker/anchors"

$git pull git@github.com:blairjames/anchors.git || echo 'Pull Failed!'
$git add --all || echo 'Add Failed!'
$git commit -a -m 'Automatic build '$timestp || echo 'Commit Failed!'
$git push || echo 'Push Failed!'

# Prune
cd /home/docker/anchors && /usr/bin/git gc --prune
