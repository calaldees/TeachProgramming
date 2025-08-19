.PHONY: run
run:
	${MAKE} --directory teachprogramming/lib

.PHONY: test
test:
	${MAKE} --directory teachprogramming/static/language_reference
	${MAKE} --directory teachprogramming/lib/verify_snippets
