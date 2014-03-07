#! /usr/bin/env python

import sys
sys.path.append("gen-py")

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from demo import MathService
from demo.ttypes import *

# Make Socket
# 建立socket, IP 和port要写对
transport = TSocket.TSocket('localhost', 9900)

# Buffering is critical. Raw sockets are very slow
# 选择传输层，这块要和服务器的设置一样
transport = TTransport.TBufferedTransport(transport)

# Wrap in a protocol
# 选择传输协议，这个也要和服务器保持一致，负责无法通信
protocol = TBinaryProtocol.TBinaryProtocol(transport)

# Create a client to use the protocol encoder
client = MathService.Client(protocol)

# Connect!
transport.open()

# Call server services
rst = client.add(1, 2)
print rst

# close transport
transport.close()
