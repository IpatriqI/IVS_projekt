.PHONY: all pack clean test doc run profile

all:
	@echo "Installing dependencies..."
	python3 -m pip install -r requirements.txt
	@echo "Building all targets..."
	python3 -m nuitka --follow-imports calculator.py

pack:
	@echo "Packing project files..."
	tar -czvf project.tar.gz calculator.py mathematical_library.py math_library_tests.py profiling.py profiling_user_input.py Makefile requirements.txt

clean:
	@echo "Cleaning up..."
	rm -f *.pyc
	rm -rf __pycache__
	rm -f project.tar.gz

test:
	@echo "Running library tests..."
	python3 -m unittest math_library_tests.py

doc:
	@echo "Generating documentation..."
	doxygen Doxyfile

run:
	@echo "Running the calculator program..."
	python3 calculator.py

profile:
	@echo "Profiling the standard deviation calculation..."
	python3 -m cProfile -o profiling_output.prof profiling.py

