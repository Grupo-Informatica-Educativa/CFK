#!/bin/sh

git pull origin release
supervisorctl restart 2021
