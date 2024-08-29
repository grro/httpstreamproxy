# http streaming proxy
This project implements HTTP streaming proxy that can be used to proxy webcam streams.

```
sudo docker run -d --restart always --name httpproxy --network host -e port 8080 -e target_url="https://192.168.1.70/anonymous/jpeg/stream=0" -e verify="False" grro/httpstreamproxy:0.1.0
```

