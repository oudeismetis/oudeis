#!/bin/bash

BUCKET_NAME=oudeis.co-cdn
DISTRIBUTION_ID=E2D53ONXDBNEGF
PROFILE=oudeis-website

# Rebuild public/ (verbose)
hugo -v 

# TODO Just sync newly edited files
# find public -type f -mtime -10
# Sync Files
aws s3 sync --profile ${PROFILE} --acl "public-read" --sse "AES256" --cache-control max-age=604800 public/ s3://${BUCKET_NAME}/

# Invalidate cache
aws cloudfront create-invalidation --profile ${PROFILE} --distribution-id ${DISTRIBUTION_ID} --paths /index.html /blog/* /projects/* /about/*
