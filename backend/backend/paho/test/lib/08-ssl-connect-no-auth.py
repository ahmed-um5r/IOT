#!/usr/bin/env python3

# Test whether a client produces a correct connect and subsequent disconnect when using SSL.

# The client should connect to port 1888 with keepalive=60, clean session set,
# and client id 08-ssl-connect-no-auth
# It should use the CA certificate ssl/all-ca.crt for verifying the server.
# The test will send a CONNACK message to the client with rc=0. Upon receiving
# the CONNACK and verifying that rc=0, the client should send a DISCONNECT
# message. If rc!=0, the client should exit with an error.

import context
import paho_test

context.check_ssl()

rc = 1
keepalive = 60
connect_packet = paho_test.gen_connect("08-ssl-connect-no-auth", keepalive=keepalive)
connack_packet = paho_test.gen_connack(rc=0)
disconnect_packet = paho_test.gen_disconnect()

ssock = paho_test.create_server_socket_ssl()

client = context.start_client()

try:
    (conn, address) = ssock.accept()
    conn.settimeout(10)

    paho_test.expect_packet(conn, "connect", connect_packet)
    conn.send(connack_packet)

    paho_test.expect_packet(conn, "disconnect", disconnect_packet)
    rc = 0

    conn.close()
finally:
    client.terminate()
    client.wait()
    ssock.close()

exit(rc)
