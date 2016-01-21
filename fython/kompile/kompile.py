from ..config import *
from .stack import Stack

def kompile(
	url,
	cwd,
	release,
	force,
	verbose,
):
	stack = Stack(release, cwd, force, verbose)

	stack.load(fytbk.url, cwd)

	stack.load(url, cwd, is_target=1)

	if stack.need_link:
		stack.link()

	return stack.target	