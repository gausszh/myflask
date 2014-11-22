#!/usr/bin/env python
#coding=utf8

from flask.ext.assets import Bundle, Environment

from . import app

bundles = {
	"all_js": Bundle("js/index.js", "js/home.js", output="gen/js_output.js"),
}

assets = Environment(app)
assets.register(bundles)
