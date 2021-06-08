#!/bin/sh

git pull origin main
supervisorctl restart 2021dev

