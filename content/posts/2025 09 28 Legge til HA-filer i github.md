---
draft: "false"
date: 2025-09-28
tags:
  - innlegg
title: Legge til HA-filer i github
---

<details>
  <summary>📁 nano gitignore</summary>
nano .gitignore
!*.yaml
!.gitignore
!*.md
!*.sh
!*.js*
#1.ssh/
#lid_rsa*
!node-red/
secrets. yamı
•ssh
•storage
•cloud
-google. token
home-assistant.1og*
id_rsa*

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
git -m "min første oppload"
```
Legg til repository
```
git remote add origin git@github.com:Brukernavngithub/repository.git
```

<details>
  <summary>📁 Definer hvor nøkkel er</summary>
git config core.sshCommand "ssh -i /root/config/.ssh/id_rsa -F /dev/null"

<details>
  <summary>📁 Kopier ut nøkkel og identifiser på github</summary>
cat /root/config/.ssh/id_rsa.pub

!![Image](/images/Pasted%20image%2020250928102507.png)
git push -u origin master

<details>
  <summary>📁 Lag shell command og automasjon</summary>
lag ei fil til shell command i config
nano pushupdates.sh
git add .
git commit -m "config files on `date +'%d-%m-%Y %H:%M:%S'`"
git push -u origin master
Gjør script kjørbart
chmod +x pushupdates.sh
Gjør det kjørbart fra shell command
git config core.sshCommand 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i /config/.ssh/id_rsa -F /dev/null'

<details>
  <summary>📁 Lag automasjon</summary>
alias: Github push
description: ""
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

