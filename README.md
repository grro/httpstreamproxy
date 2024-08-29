# http streaming proxy
This project implements HTTP streaming proxy that can be used to proxy webcam streams.

```
sudo docker run --name httpproxy --network host -e port=8280 -e target_url="http://localhost:9080/static/root.html" -e verify="False" grro/httpstreamproxy:0.2.3
```

