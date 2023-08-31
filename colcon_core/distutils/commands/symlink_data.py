# Copyright 2023 Open Source Robotics Foundation, Inc.
# Licensed under the Apache License, Version 2.0

from distutils.command.install_data import install_data
import os.path


class symlink_data(install_data):  # noqa: N801
    """Like install_data, but symlink files instead of copying."""

    def copy_file(self, src, dst, **kwargs):  # noqa: D102
        if kwargs.get('link'):
            return super().copy_file(src, dst, **kwargs)

        kwargs['link'] = 'sym'
        src = os.path.abspath(src)
        return super().copy_file(src, dst, **kwargs)
