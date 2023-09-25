import os
import stat
import requests
import sys
import subprocess
import docker
import json

print("setting the docker client")
try:
  client = docker.DockerClient(base_url='unix://var/run/docker.sock')
  print("docker client set")
except docker.errors.DockerException as e:
  print(f"error creating docker client: {e}")
  
client.images.pull('nginx')
client.images.pull('ubuntu')
image_list = client.images.list()
for item in image_list:
  print(f"image: {item}")
container = client.containers.run("ubuntu:latest", "echo hello world")


