# cog
[https://cog.run/](https://github.com/replicate/cog)

```code
sudo curl -o /usr/local/bin/cog -L "https://github.com/replicate/cog/releases/latest/download/cog_$(uname -s)_$(uname -m)"
sudo chmod +x /usr/local/bin/cog

cog predict -i image=123

cog serve -p 8080

curl -X POST   -H "Content-Type: application/json"   -d $'{
    "input": {
      "image": "zero-shot voice clone"
    },
    "webhook": "https://www.example.com/oauth2/ip"

    }'   http://127.0.0.1:8080/predictions
```
