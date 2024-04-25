#!/bin/bash
# sends a GET request with header var 'X-School-User-Id' with var 98
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
