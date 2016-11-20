[![Build Status](https://travis-ci.org/ACCUConf/ACCUConf_Website.svg?branch=master)](https://travis-ci.org/ACCUConf/ACCUConf_Website)

Static page content: ![Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png)

Flask application code: [![Licence](https://img.shields.io/badge/license-GPL_3-green.svg)](https://www.gnu.org/licenses/gpl-3.0.txt)


# ACCU Conference Website

## Introduction

This repository contains the framework for the [ACCU Conference website](http://conference.accu.org)
(http://conference.accu.org). The driver and manager of the dynamic content is a Flask application, the
static content is managed as a Nikola website. It is assumed that Python 3 is used for both Flask and
Nikola.

## The Toolchain

Git, obviously, but also [Nikola](https://getnikola.com/) and [Flask](http://flask.pocoo.org/).

Many operating system distributions package Nikola and Flask (some only the Python 2 version though :-( If
there is not a suitable package then creating a virtualenv and installing Nikola and Flask from PyPI using
pip works well – Python 3 being the most senble choice of Python obviously.

For Linux users, and particularly for those not accustomed to Python development, a simple solution is to
install the free Conda system from Continuum Analytics, a company heavily involved in open source.
The `miniconda3` distribution is to be preferred, since unlike the full `conda3`  it installs a fairly
small set of modules and downloads the rest as required to build virtualenvs. Since the only thing you
have to do to enable Conda is add its `bin` directory to your path you can enable it just to work on this
site and remove it afterwards and it will be pretty much isolated from anything else you do on the same
machine. The `miniconda` downloads page is at http://conda.pydata.org/miniconda.html and instructions for
installing on Linux are at http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install (Mac OS
and Windows users should find their instructions on the same page).

The following instructions assume that the `conda` command is already available in your environment.



## The Licence

All text material in the Nikola managed part of this repository is licenced
under
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License](http://creativecommons.org/licenses/by-nd-nc/4.0/). The
code of the Flask application is licenced under
the [GNU Public Licence version 3](https://www.gnu.org/licenses/gpl-3.0.en.html) (GPLv3).
