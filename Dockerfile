FROM ubuntu:latest
LABEL authors="Ryan Skells"

ENTRYPOINT ["top", "-b"]