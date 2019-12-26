# django-key-value-storage

## TTL implemented using django-background-tasks
* for each key-value pair, one background task will be initiated which will be excuted after 5minutes 20 seconds later from it's creation time. Within this time if we perform any PUT/PATCH operation with that pair then the * timestamp will be overriden & another background task will be initiated with the TTL of 5 minutes.

* [if it passes the TTL time then the value will be replaced with an empty string.]

## API end-points

* for single-pair GET,PULL,PATCH
http://127.0.0.1:8000/api/single-pair/{key}

* for single-pair POST
http://127.0.0.1:8000/api/create-pair/

* for all-pairs
http://127.0.0.1:8000/api/all-pairs/



## Credintials

* username: admin
* password: djangoadmin