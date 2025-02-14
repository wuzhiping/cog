# cog
[https://cog.run/](https://github.com/replicate/cog)

```code
sudo curl -o /usr/local/bin/cog -L "https://github.com/replicate/cog/releases/latest/download/cog_$(uname -s)_$(uname -m)"
sudo chmod +x /usr/local/bin/cog

mkdir demo
cd demo
cog init

cog predict -i image=123

cog serve -p 8080

curl -X POST   -H "Content-Type: application/json"   -d $'{
    "input": {
      "image": "zero-shot voice clone"
    },
    "webhook": "https://www.example.com/oauth2/ip",
    "webhook_events_filter": ["start", "log","output","completed"]
    }'   http://127.0.0.1:8080/predictions

cog build -t my-model-img
docker run --rm -it -p 8080:5000 --gpus all my-model-img python -m cog.server.http --threads=10
```
