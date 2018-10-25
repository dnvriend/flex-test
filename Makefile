.PHONY: help init clean validate mock create delete info deploy
.DEFAULT_GOAL := run

export PYTHONWARNINGS=ignore::DeprecationWarning

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

init: ## create env
	pipenv install --three --dev

delete: ## delete env
	pipenv rm

test: ## run tests
	pipenv run pytest -s -v tests
