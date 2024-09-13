from dataclasses import dataclass
from typing import Literal, Optional
from . import default

class Virtualization(default.Virtualization):
    def __init__(self):
        self.name = 'xcp-ng'



    @dataclass
    class Manager(default.Virtualization.Manager):
        def __init__(self, **kwargs):
            return
        """Stores the manager used as API endpoint to retrieve data."""

        @property
        def get(self) -> callable:
            print("Get function called.")
            return Virtualization.get_manager(Virtualization)

        @property
        def filter(self) -> list:
            print('Not implemented yet')
            return []

    @dataclass
    class Cluster(default.Virtualization.Cluster):
        def __init__(self, manager: callable):
            return

        """Class to represent the virtualization clusters/pools on which the VM workloads run """
        @property
        def get(self) -> callable:



            return

        @property
        def filter(self) -> list:
            print('Not implemented yet')
            return []

    @dataclass
    class VM(default.Virtualization.VM):
        """ Class to represent the VM's running on clusters """

        @property
        def get(self) -> callable:
            print('Not implemented yet')
            return

        @property
        def filter(self) -> list:
            print('Not implemented yet')
            return []


    def get_manager(self):
        manager = self.Manager(
            name="xen-orchestra",
            hostname='xo.vels.online',
            username="",
            password="",
            type="xcp-ng"
        )
        return manager