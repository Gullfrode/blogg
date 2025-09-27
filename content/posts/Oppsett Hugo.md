
###### Innstaller Hugo
brew install hugo
###### Sync
rsync -av --delete fra til

###### Lag side på github, og legg inn nøkkel fra maskina
generer ssh-key
cd ~/.ssh
 ssh-keygen -t rsa -b 4096 -C "gullfrode@gmail.com"
cat id_rsa.pub
Lim inn innholdet i github
!![Image](/images/Pasted%20image%2020250927165320.png)