all:
	virtualenv -p python2.7 --distribute venv2.7
	virtualenv -p python3.3 --distribute venv3.3
	. venv2.7/bin/activate && pip install termcolor==1.0.0 && python main.py
	. venv3.3/bin/activate && pip install termcolor==1.1.0 && python main.py

clean:
	rm -rf venv*
