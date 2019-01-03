#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import signal
import sys

# Exporter Python
import exporter as ex


# Funcao captura control C
def exit_gracefully(signum, frame):
		# restore the original signal handler as otherwise evil things will happen
		# in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
		# signal.signal(signal.SIGINT, original_sigint)
		
		try:
				ex.erro("\nSaindo.")
				sys.exit(1)
		
		except KeyboardInterrupt:
				ex.erro("Ok ok, quitting")
				sys.exit(1)
		
		# restore the exit gracefully handler here
		# signal.signal(signal.SIGINT, exit_gracefully)


# Funcao roda o programa
def run_program():
		if sys.version_info[0] < 3:
				print(ex.bcolors.FAIL + "*" * 90 + ex.bcolors.ENDC)
				print(ex.bcolors.WARNING + "Erro. Sua versão do Python é a " + str(
						sys.version_info[0]) + ", e precisamos do Python 3. Atualize e tente novamente." + ex.bcolors.ENDC)
				print(ex.bcolors.FAIL + "*" * 90 + ex.bcolors.ENDC)
		else:
				ex.startAskForModel()


# construtor
if __name__ == '__main__':
		# store the original SIGINT handler
		original_sigint = signal.getsignal(signal.SIGINT)
		signal.signal(signal.SIGINT, exit_gracefully)
		run_program()
