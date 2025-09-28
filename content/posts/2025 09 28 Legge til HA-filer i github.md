---
draft: "false"
date: 2025-09-28
tags:
  - innlegg
title: Legge til HA-filer i github
---
 nano gitignore

nano .gitignore
```
# ta med

!*.yaml

!.gitignore

!*.md

!*.sh

!*.js*

# Ignorer alt i .storage

.storage/**

  

# Men behold selve mappa og disse filene, inputs fra gui og dashbord:

!.storage/

!.storage/lovelace

!.storage/lovelace_dashboards

!.storage/lovelace_resources

!.storage/lovelace.dashboard_responsive

!.storage/input_boolean

!.storage/input_button

!.storage/input_datetime

!.storage/input_number

!.storage/input_select

!.storage/input_text

#Ta med nodered

!node-red/

#Ikke ta med

.cloud/

.ssh/

appdaemon/

blueprints/

custom_components/

deps/

esphome/

glances/

image/

model_cache/

packages/

  

scripts/

themes/

tts/

www/

zigbee2mqtt/

secrets.yamı

.exports

.HA_VERSION

.ios_conf

.jwt_secret

.logi_cache.pickle

.mealie_token

.ps4-games.C863F19FEC5A_4341.json

.sonoff.json.spotify-token-logi_cache.timeline

.timeline

.vacuum

.xbox-token.json

  

•storage

•cloud

-google. token

backup_config.yaml

backup.db

frigate.db

frigate.db-wal

frigate.yml

ha_shell.log

home-assistant.log

home-assistant.log.1

id_rsa*

home-assistant_v2.*

music_assistant.db

zigbee.db

zwcfg_0xfa9afacb.xml

zwscene.xml

home-assistant.log*

*.log

  
  

# ignore logs ekstra sikkerhet

home-assistant.log*

*.log
```

Lag et nytt repository på github
logg inn via ssh på ha
Lag nøkkel i /root/config/.ssh

```
mkdir -p /root/config/.ssh
cd /root/config/.ssh
ssh-keygen -t rsa -b 4096 -C  "eposten@din.no"
```

lagre i /root/config/.ssh(så event flytt med cp om det bir lagret annen plass. Ikke bruk passord om det skal automatiseres)

installer git( i root/config)
```
git init
git add .
git commit -m "min første oppload"
```
Legg til repository
```
git remote add origin git@github.com:Brukernavngithub/repository.git
```
Definer hvor nøkkel er
```
git config core.sshCommand "ssh -i /root/config/.ssh/id_rsa -F /dev/null"
```
 Kopier ut nøkkel og identifiser på github
```
cat /root/config/.ssh/id_rsa.pub
```

!![Image](/images/Pasted%20image%2020250928102507.png)
```
git push -u origin master
```
<details>
  <summary>📁 Lag shell command og automasjon</summary>

lag ei fil til shell command i config

nano pushupdates.sh
```
git add .
git commit -m "config files on `date +'%d-%m-%Y %H:%M:%S'`"
git push -u origin master
```
###### Gjør script kjørbart
```
chmod +x pushupdates.sh
```
###### Gjør det kjørbart fra shell command
```
git config core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i /config/.ssh/id_rsa -F /dev/null'
```
 ###### Lag automasjon
```
alias: Github push
description: 
triggers:
  - trigger: time
    at: "01:00:00"
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
      - sat
      - sun
conditions: []
actions:
  - action: shell_command.pushupdates_github
    data: {}
mode: single
```

