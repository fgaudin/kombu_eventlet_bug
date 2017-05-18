Installing
==========

virtualenv -p python3.4 .virtualenv
source .virtualenv/bin/activate

pip install -r requirements.txt


Reproducing the bug
===================

in one console:

./runserver.sh

in a second console:

./test.sh

Expected error on the first call:

AttributeError: 'LifoQueue' object has no attribute 'mutex'

The problem comes from kombu.resource.LifoQueue having 
'eventlet.green.Queue.LifoQueue' as base class instead of the standard python 3
LifoQueue.
