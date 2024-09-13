from dataclasses import dataclass
from typing import Literal, Optional


class Virtualization(object):
    def __init__(self):
        self.name = 'default'

    @dataclass
    class Manager:
        """Stores the manager used as API endpoint to retrieve data."""
        name: str
        type: Literal['vmware', 'xcp-ng']
        hostname: str
        username: str
        password: str

        @property
        def get(self) -> callable:
            return

        @property
        def filter(self) -> list:
            return []

    @dataclass
    class Cluster:
        """Class to represent the virtualization clusters/pools on which the VM workloads run """
        name: str
        manager: callable

    @dataclass
    class VM:
        """ Class to represent the VM's running on clusters """
        name: str
        cluster: callable
        ip_address: Optional[str]

        @property
        def get(self) -> callable:
            return

        @property
        def filter(self) -> list:
            return []