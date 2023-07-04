# TODO: Create an start to use in firts run

.PHONY: start
# Automate first install
start:
	@echo ">>> Starting project"
	@echo " \n >>> Creating directorys"
	@mkdir tmp/
	@mkdir tmp/pictures
	@echo ">>> Creating Venv"
	@python3 -m venv .venv
	@source .venv/bin/activate
	@pip3 install requirements.txt
	@cp env.credentials .env

.PHONY: run
# Automate first install
run:
	@python3 main.py