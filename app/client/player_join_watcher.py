# Created by Viktoria 
# (▰˘◡˘▰)
# 13/10/2020
# Student number: R00180598

from __future__ import print_function
import logging

import grpc

import darts_match_pb2 as darts_match_pb2
import darts_match_pb2_grpc as darts_match_pb2_grpc

from domain.visit import Visit

def run():
    with grpc.insecure_channel('127.0.0.1:50055') as channel:
        stub = darts_match_pb2_grpc.DartsMatchStub(channel)
        for response in stub.WatchMatch(
                darts_match_pb2.WatchRequest()):
            print("Player: " + response.player.userName)
            print("Visit: " + Visit(response.darts).to_string())


if __name__ == '__main__':
    logging.basicConfig()
    run()