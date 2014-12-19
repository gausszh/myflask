#!/usr/bin/env python
#coding=utf8

from flask.ext.assets import Bundle, Environment

bundles = {
	"all_js": Bundle("js/index.js", "js/home.js", output="gen/js_output.js", filters="jsmin"),
}

assets = Environment()
# assets.
assets.register(bundles)
