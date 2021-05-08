#!/bin/sh
set -e

getent passwd node >/dev/null && deluser node
getent passwd user >/dev/null || adduser -D -u $LOCAL_USER_ID user

chown user:user /home/user

export PATH=/dvd/frontend/node_modules/.bin:$PATH
cd /dvd/frontend

/sbin/su-exec user yarn
