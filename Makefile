# Define Python executable
PYTHON = python3.8

# Define the command to run the Flask application
RUN_CMD = $(PYTHON) main.py

# Rule to run the Flask application
run:
	$(RUN_CMD)

# Set Flask export for shell
flask_shell:
	export FLASK_APP=main.py; flask shell