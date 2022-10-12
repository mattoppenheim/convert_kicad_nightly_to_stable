# while inotifywait -e close_write <filename>; do make; done
filename = convert_kicad_footprint.py
SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

ifeq ($(origin .RECIPEPREFIX), undefined)
> $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

run:
> pytest --capture=sys

run_prog:y
> python $(filename)

clean:
> rm -rf __pycache__

