FILES = a b c d e


.PHONY : help clean create start simple parse


help:
	@echo "Usage: 'make <target>' where <target> is one of:"
	@echo " help		to print this help"
	@echo " clean		to remove programs"
	@echo " create		to create programs"
	@echo " start		to do 'clean' and 'create' targets sequentially"
	@echo " simple		to create one program"
	@echo " parse		to run Hightail parser in background"

clean:
	@rm src/*.cpp 2>/dev/null || true
	@rm src/*.py 2>/dev/null || true

create:
	@for file in $(FILES); do cp lib/cpp/_template.cpp src/$$file.cpp; done
	@for file in $(FILES); do cp lib/py/_template.py src/$$file.py; done

start: clean create
	@echo Good luck!

simple: clean
	@cp lib/cpp/_template.cpp src/main.cpp
	@cp lib/py/_template.py src/main.py

parse:
	@(cd bin/ && java -jar Hightail-v0.9.4.jar)&
