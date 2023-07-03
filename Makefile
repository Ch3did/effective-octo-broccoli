# TODO: Create an start to use in firts run

.PHONY: start
# Automate first install
start:
	@echo ">>> Removing Python 3.8 virtualenv if exists..."
	@poetry env remove 3.8 2>/dev/null || :
	@echo ">>> Install Dependencies ..."
	@poetry install
	@echo ">>> Running Git ..."
	@git init && git add . && git commit -m "chore(cookie): first commit"
	@echo ">>> Opening VSCode..."
	@cp env.credentials .env && code .
