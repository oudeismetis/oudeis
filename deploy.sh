#!/bin/bash

BUCKET_NAME=oudeis.co-cdn
DISTRIBUTION_ID=E2D53ONXDBNEGF
PROFILE=oudeis-website

# R ebuild public/ (verbose)
hugo -v 

# Sync Files
aws s3 sync --profile ${PROFILE} --acl "public-read" --sse "AES256" public/ s3://${BUCKET_NAME}/

# Invalidate cache
aws cloudfront create-invalidation --profile ${PROFILE} --distribution-id ${DISTRIBUTION_ID} --paths /index.html /
