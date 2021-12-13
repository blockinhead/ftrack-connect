# :coding: utf-8
# :copyright: Copyright (c) 2014 ftrack

import os
import qtawesome as qta

from ._version import __version__


def load_icons(font_folder):
    font_folder = os.path.abspath(font_folder)
    print('loading icons from :{} '.format(font_folder))

    qta.load_font(
        'ftrack',
        'ftrack-icon.ttf',
        'ftrack-icon-charmap.json',
        directory=font_folder
    )
