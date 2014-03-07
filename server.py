# -*- coding: utf-8 -*-
#! /usr/bin/env python
import sys
sys.path.append('gen-py')

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


import demo.MathService


class MathHandler(demo.MathService.Iface):
    def add(self, a, b):
        return a + b

if __name__ == "__main__":

    processor = demo.MathService.Processor(MathHandler())
    # 设置端口
    transport = TSocket.TServerSocket(port=9900)
    # 设置传输层
    tfactory = TTransport.TBufferedTransportFactory()

    # 设置传输协议
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

    print 'Starting the server...'
    server.serve()
    print 'done'
