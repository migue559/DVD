#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

python /dvd/backend/manage.py collectstatic --noinput
python /dvd/backend/manage.py migrate
python /dvd/backend/manage.py runserver 0.0.0.0:8001