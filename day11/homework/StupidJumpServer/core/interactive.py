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


import socket
import os
import sys
import datetime
from paramiko.py3compat import u
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core import db_modles

logger = logging.getLogger(__name__)

# windows does not have termios...
try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False


def interactive_shell(chan, user_obj, host_and_sysuser_obj, log_info_caches, log_record):
    if has_termios:
        posix_shell(chan, user_obj, host_and_sysuser_obj, log_info_caches, log_record)
    else:
        windows_shell(chan)


def posix_shell(chan, user_obj, host_and_sysuser_obj, log_info_caches, log_record):
    """

    :param chan: 连接实例
    :param user_obj: 用户实例
    :param host_and_sysuser_obj: 主机及主机用户实例
    :param log_info_caches: log缓存
    :param log_record: log_record方法
    :return:
    """
    import select
    
    oldtty = termios.tcgetattr(sys.stdin)
    try:
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        cmd = ""
        tab_flag = False
        while True:
            r, w, e = select.select([chan, sys.stdin], [], [])
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break

                    if tab_flag:  # 如果有回车就记录返回值
                        cmd += x
                        tab_flag = False

                    sys.stdout.write(x)
                    sys.stdout.flush()
                except socket.timeout:
                    pass
            if sys.stdin in r:
                x = sys.stdin.read(1)

                if x != "\r":
                    cmd += x
                    if x == '\t':
                        tab_flag = True
                else:
                    # print("==>", cmd)
                    # 生成日志的表格
                    log_info = db_modles.AuditLog(
                        userprofile_id=user_obj.id,
                        hostandsysuser_id=host_and_sysuser_obj.id,
                        action_type="cmd",
                        cmd=cmd,
                        data=datetime.datetime.now()
                    )
                    log_info_caches.append(log_info)
                    cmd = ""

                    if len(log_info_caches) >= 10:
                        log_record(log_info_caches)
                        log_info_caches = []

                if len(x) == 0:
                    break
                chan.send(x)

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)

    
# thanks to Mike Looijmans for this code
def windows_shell(chan):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
        
    def writeall(sock):
        while True:
            data = sock.recv(256)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break
            sys.stdout.write(str(data.decode()))
            sys.stdout.flush()
        
    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
        
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass
