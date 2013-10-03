clean:
	rm -r *.pyc

unit:
	nosetests -a '!integration' --rednose

integration:
	nosetests --rednose

cov:
	./bin/coverage html test_s3manager.py