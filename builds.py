import os
import stat
import requests
import sys
import subprocess
import docker
import json


client = docker.DockerClient(base_url='unix://var/run/docker.sock')
client.containers.run("ubuntu:latest", "echo hello world")
client.containers.list()
