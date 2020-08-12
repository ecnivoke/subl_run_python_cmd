import sublime
import sublime_plugin
import subprocess
import os


class Run_pythonCommand(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = os.path.split(self.view.file_name())[0]
		file = os.path.split(self.view.file_name())[1]
		dir_path = os.path.dirname(os.path.realpath(__file__))

		if file.find('.py') > -1:
			file = file.split('.py')[0]
			subprocess.Popen([dir_path + '/run_python.bat', folder, file])

		else:
			print('"' + file + '" is not a python file')
