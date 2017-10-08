# persist-cache
For hvalidator get the persistence into over database as a daemon

# Usage:
- Start
``
python launch.py start
``
- Stop
``
python launch.py stop
``
- Status
``
python launch.py status
``

# Persistence:
Make persistence into mongodb for every expire data, if you want to save all entry please change 
into ``utils/listener.py`` :
```
if KEY_REDIS_EXPIRE == message[KEY_CHANNEL]:
```
you can delete it to save every entry



