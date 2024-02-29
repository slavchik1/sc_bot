build:
	docker build -t slachick/sc_bot:latest .

up: build
	docker rm -f sc_bot
	docker run -it -d --name sc_bot --restart always --log-opt max-size=100m --log-opt max-file=2 slachick/sc_bot:latest
