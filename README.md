# steamy-mp4

A python utility that extracts the mp4 video urls for a given steam url

## How it works

1. Install the required python packages.

```bash
python -m pip install -r requirements.txt
```

2. Create a file called `urls.txt` in which each steam url is placed on a new line like this:

Note it is important that there is an ending `/` for the name extraction to work.

```text
https://store.steampowered.com/app/1578520/Samurai_Zero/
https://store.steampowered.com/app/1219240/BioGun/
https://store.steampowered.com/app/1485070/Esse_Proxy/
```

3. Run the python script and collect the output json file:

```bash
python main.py
```
