# Getting started with novem

This repo provides four example scripts on how to get started with the novem 
datavisualisation platform.

For this to work make sure you've got python 3.8 or newer along with a novem
account.

You need to configure your novem environment first by running `novem --init`

After that you can run `run.sh` to install dependencies and create the visuals

## The examples
This repo contains three example plots along with an example e-mail, you need to
register and validate  your e-mail before you can send it, and if you're on 
novem free you can only send the mail to yourself.

Also note that all visuals are shared with the public, and you'll have to change
that if you want to modify the code and keep it private.

Once you've run the scripts you can use the novem cli to view your plots and 
interact with the platform.

```bash
novem -p # list plots
novem -m # list mails

novem -p nei_rgn_perf -x # surprise
```

For more information just use `novem --help`


Happy hacking!
