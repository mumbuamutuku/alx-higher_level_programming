#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -si "$1" | head -1 | cut -d ' ' -f2
