#!/bin/bash
# sends a GET request with header variable being 'X-School-User-Id' with variable 98
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
