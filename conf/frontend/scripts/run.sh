#!/bin/sh
set -e
. /scripts/base.sh
echo "migue"
echo `val $APP_PORT`
echo "migue"

exec /sbin/su-exec user quasar dev -p $APP_PORT