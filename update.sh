#!/bin/sh

git pull origin publicrelease
supervisorctl restart 2021dev
