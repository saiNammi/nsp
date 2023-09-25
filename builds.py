import os
import stat
import requests
import sys
import subprocess
import docker
import json


def trigger_script_validation_checks(image_name = "registry.access.redhat.com/ubi8/ubi:8.7"):
    # Spawn a container and pass the build script
    client = docker.DockerClient(base_url='unix://var/run/docker.sock')
    container = client.containers.run(
        image_name,
        "pwd",
        network = 'host',
        detach = True,
        volumes = {
            current_dir : {'bind': '/home/tester', 'mode': 'rw'}
        },
        stderr = True, # Return logs from STDERR
    )
    result = container.wait()
    try:
        print(container.logs().decode("utf-8"))
    except Exception:
        print(container.logs())
    container.remove()
    if int(result["StatusCode"]) != 0:
        raise Exception(f"Build script validation failed!")
    else:
        return True

trigger_script_validation_checks()
