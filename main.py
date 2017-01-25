# !/usr/bin/python
# -*- coding: utf-8 -*-


import sys

import exporter as ex

if sys.version_info[0] < 3:
    print(ex.bcolors.FAIL + "*" * 90 + ex.bcolors.ENDC)
    print(ex.bcolors.WARNING + "Erro. Sua versão do Python é a " + str(
        sys.version_info[0]) + ", e precisamos do Python 3. Atualize e tente novamente." + ex.bcolors.ENDC)
    print(ex.bcolors.FAIL + "*" * 90 + ex.bcolors.ENDC)
else:
    ex.startAskForModel()
