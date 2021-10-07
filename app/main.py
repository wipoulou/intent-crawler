import logging
import socket
import sys

from struct import *


logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    filename="output.log",
    encoding="utf-8",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


def ethernet_head(raw_data):
    dest, src, prototype = unpack("! 6s 6s H", raw_data[:14])
    print(dest, src)
    # dest_mac = get_mac_addr(dest)
    # src_mac = get_mac_addr(src)
    proto = socket.htons(prototype)
    data = raw_data[14:]
    # return dest_mac, src_mac, proto, data


def ipv4_head(raw_data):
    version_header_length = raw_data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack("! 8x B B 2x 4s 4s", raw_data[:20])
    data = raw_data[header_length:]
    return version, header_length, ttl, proto, src, target, data


def get_ip(addr):
    return ".".join(map(str, addr))


if __name__ == "__main__":
    logging.info("Starting")

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    while True:
        raw_data, addr = s.recvfrom(65535)
        eth = ethernet_head(raw_data)
        # print("\nEthernet Frame:")
        # print(
        #     "Destination: {}, Source: {}, Protocol: {}".format(eth[0], eth[1], eth[2])
        # )
        # if eth[2] == 8:
        #     ipv4 = ipv4(ethp[4])
        #     print("\t - " + "IPv4 Packet:")
        #     print(
        #         "\t\t - "
        #         + "Version: {}, Header Length: {}, TTL: {},".format(
        #             ipv4[1], ipv4[2], ipv4[3]
        #         )
        #     )
        #     print(
        #         "\t\t - "
        #         + "Protocol: {}, Source: {}, Target: {}".format(
        #             ipv4[4], ipv4[5], ipv4[6]
        #         )
        #     )

    logging.info("Ending")
