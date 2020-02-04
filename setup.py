from cx_Freeze import setup, Executable

includefiles = ['default.txt']
includes = []
excludes = []
packages = []

setup(
	name='Diceware',
	version='1',
	packages=[''],
	url='',
	license='',
	options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
	author='and.re',
	author_email='',
	description='Diceware Password Generator',
	executables = [Executable("diceware.py")]
)
