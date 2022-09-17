#!/bin/bash
echo Deployment Script

#cd /home/hackzurich22 || exit

# pull master
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$BRANCH" != "master" ]]; then
  echo 'Aborting script, wrong branch';
  echo "$BRANCH";
  exit 1;
fi

echo "shutting down docker containers"

docker-compose down

git reset --hard
git pull origin master

cd hackzurich22-webapp
npm install
npm run build
cd ..

cd hackzurich22-elevator-screen
npm install
npm run build

cd ..

docker-compose up -d --build --force-recreate

