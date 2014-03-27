#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('gen-py')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from demo import MathService
from demo.ttypes import *


class MathHandler(MathService.Iface):
    def add(self, a, b):
        print "Receive: %s, %s" %(a, b)
        return a + b


if __name__ == "__main__":

    # 实例化handler
    handler = MathHandler()

    # 设置processor
    processor = MathService.Processor(handler)

    # 设置端口
    transport = TSocket.TServerSocket('localhost', port=9900)

    # 设置传输层
    tfactory = TTransport.TBufferedTransportFactory()

    # 设置传输协议
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print 'Starting the server...'
    server.serve()
    print 'done'
