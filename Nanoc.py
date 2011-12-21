import sublime, sublime_plugin

class NanocDeployCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		print "Deploying..."
		self.view.window().run_command("exec", {"cmd": ["rake","deploy:rsync"], "working_dir": self.view.window().folders()[0]})
