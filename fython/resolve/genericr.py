from ..config import *
from .defr import defR

def genericR(linecod):
	i = linecod.first_modifier_value

	if i in instruction:
		linecod.adjust_opbol
		return instruction[i]

	elif i == l.defk:
		return defR(linecod)

	else:
		return l.varpec

instruction = {
	l.alloc : l.allocruc,
	l.classk : l.classpec,
	l.critical : l.criticalruc,
	l.dealloc : l.deallocruc,
	l.elifk : l.elifruc,
	l.elsek : l.elseruc,
	l.elwhere : l.elwhereruc,
	l.error : l.errorruc,
	l.ifk : l.ifruc,
	l.importk : l.importpec,
	l.inline : l.inlineruc,
	l.interface : l.interfacepec,
	l.fork : l.forruc,
	l.omp : l.ompruc,
	l.printk : l.printruc,
	l.private : l.privateruc,
	l.public : l.publicruc,
	l.read : l.readruc,
	l.sync : l.syncruc,
	l.where : l.whereruc,
	l.whilek : l.whileruc,
	l.xip : l.xipruc,
}