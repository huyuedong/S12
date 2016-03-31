#!/usr/bin/env python
# -*-coding:utf8 -*-

# Copyright (C) 2003-2007  Robey Pointer <robeypointer@gmail.com>
#
# This file is part of paramiko.
#
# Paramiko is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# Paramiko is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Paramiko; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.


import base64
from binascii import hexlify
import getpass
import os
import select
import socket
import sys
import time
import traceback
from paramiko.py3compat import input

import paramiko
try:
    import interactive
except ImportError:
    from . import interactive


# 通过key来认证
def auth_key(client_obj, username):
    default_path = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
    try:
        key = paramiko.RSAKey.from_private_key_file(default_path)
    except paramiko.PasswordRequiredException:
        password = getpass.getpass('RSA key password: ')
        key = paramiko.RSAKey.from_private_key_file(default_path, password)
    client_obj.auth_publickey(username, key)


# 通过密码来认证
def auth_pw(client_obj, username, password):
    client_obj.auth_password(username, password)


def ssh_login(user_obj, host_and_sysuser_obj):
    hostname = host_and_sysuser_obj.host.ip_addr
    port = host_and_sysuser_obj.host.port
    username = host_and_sysuser_obj.sysuser.username
    auth_type = host_and_sysuser_obj.sysuser.auth_type
    # now connect
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((hostname, port))

        t = paramiko.Transport(sock)
        try:
            t.start_client()
        except paramiko.SSHException:
            print('*** SSH negotiation failed.')
            sys.exit(1)

        try:
            keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        except IOError:
            try:
                keys = paramiko.util.load_host_keys(os.path.expanduser('~/ssh/known_hosts'))
            except IOError:
                print('*** Unable to open host keys file')
                keys = {}

        # check server's host key -- this is important.
        key = t.get_remote_server_key()
        if hostname not in keys:
            print('*** WARNING: Unknown host key!')
        elif key.get_name() not in keys[hostname]:
            print('*** WARNING: Unknown host key!')
        elif keys[hostname][key.get_name()] != key:
            print('*** WARNING: Host key has changed!!!')
            sys.exit(1)
        else:
            print('*** Host key OK.')
        if auth_type == u'SSH/KEY':
            auth_key(t, username)
        else:
            password = host_and_sysuser_obj.sysuser.password
            auth_pw(t, username, password)
        if not t.is_authenticated():
            print('*** Authentication failed. :(')
            t.close()
            sys.exit(1)

        chan = t.open_session()
        chan.get_pty()
        chan.invoke_shell()
        print('*** Here we go!\n')
        interactive.interactive_shell(chan)
        chan.close()
        t.close()

    except Exception as e:
        print('*** Caught exception: ' + str(e.__class__) + ': ' + str(e))
        traceback.print_exc()
        try:
            t.close()
        except Exception:
            pass
        sys.exit(1)
