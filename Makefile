all: env test packages

clean:
	bin/clean.sh

env:
	bin/env.sh

test: env
	bin/test.sh

packages: env
	bin/packages.sh
