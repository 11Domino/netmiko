"""Centec OS Support"""
from netmiko.cisco_base_connection import CiscoBaseConnection
import time
import re


class CentecOSBase(CiscoBaseConnection):
    def session_preparation(self):
        """Prepare the session after the connection has been established."""
        self._test_channel_read(pattern=r"[>#]")
        self.set_base_prompt()
        self.disable_paging()
        self.set_terminal_width(command="terminal length 0")
        # Clear the read buffer
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def config_mode(self, config_command="configure terminal", pattern=""):
        """
        Enter into configuration mode on remote device.

        Centec IOS devices abbreviate the prompt at 20 chars in config mode
        """
        if not pattern:
            pattern = re.escape(self.base_prompt[:16])

        return super().config_mode(config_command=config_command, pattern=pattern)

    def save_config(self, cmd="write", confirm=False, confirm_response=""):
        """Save config: write"""
        return super().save_config(
            cmd=cmd, confirm=confirm, confirm_response=confirm_response
        )


class CentecOSSSH(CentecOSBase):

    pass


class CentecOSTelnet(CentecOSBase):

    pass
