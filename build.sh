#!/bin/bash

set -ex

rm -rf docs/
sphinx-build -M html source docs
mv docs/html/* docs
touch docs/.nojekyll
