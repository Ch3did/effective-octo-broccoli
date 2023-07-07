.PHONY: start
# Automate first install
start:
	@echo ">>> Starting project"
	@echo ">>> Creating directorys"
	@mkdir tmp/
	@mkdir tmp/pictures
	@echo ">>> Creating env file"
	@cp env.config env
	@echo ">>> Installing Dependences"
	@pip3 install -r requirements.txt



.PHONY: run
# run process
run:
	@python3 tasks.py


.PHONY: folders
# create folders process
folders:
	@echo ">>> Creating dowload folders"
	@mkdir tmp/
	@mkdir tmp/pictures


.PHONY: phrase
# update phrase
phrase:
	@echo ">>> Updating env phrase..."
	@python3 src/helpers/env_update.py -t "phrase"


.PHONY: section
# update section
section:
	@echo ">>> Updating env section..."
	@python3 src/helpers/env_update.py -t "section"



.PHONY: months
# update months
months:
	@echo ">>> Updating env months..."
	@python3 src/helpers/env_update.py -t "months"