#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'zjm'

from fabric.api import *
import time

@parallel
def start(app_id):
	sudo('''cat << EOF > /tmp/kill_loop.sh
		#!/bin/bash
		time=\\\$(date +%s)
		while ((\\\$(date +%s) - time < 30));
		do
			ps aux | grep {} | awk '{{print \\\$2}}' | xargs sudo kill -9
			sleep 9
		done
	'''.format(app_id))
	run("nohup /bin/bash /tmp/kill_loop.sh &!")

@parallel
def stop(app_id):
	with settings(warn_only=True):
		run("ps aux | grep kill_loop.sh | awk '{print $2}' | xargs kill -9")