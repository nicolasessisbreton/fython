# unit, in order of: fython.language.language
code_suffix = 'cod'
spec_suffix = 'pec'
instruction_suffix = 'ruc'
symbol_suffix = 'bol'
lexem_suffix = 'x'

code = 'code'
linecod = 'linecod'
childcod = 'childcod'
friendcod = 'friendcod'

spec = 'spec'
module = 'module'

importpec ='importpect'

interfacepec = 'interfacepec'

classpec = 'classpec'
typepec = 'typepec'
methodpec = 'methodpec'

routpec = 'routpec'

varpec = 'varpec'

instruction = 'instruction'

element = 'element'

symbol = 'symbol'
enumbol = 'enumbol'

ibol = 'ibol'

dotbol = 'dotbol'

funbol = 'funbol'
slicebol = 'slicebol'

parbol = 'parbol'
ketbol = 'ketbol'

bitbol = 'bitbol'

opbol = 'opbol'

packagebol = 'packagebol'

semibol = 'semibol'

lexem = 'lexem'

bofx ='bofx'
eofx = 'eofx'

linefeedx = 'linefeedx'
newlinex = 'newlinex'

indentx = 'indentx'
dedentx = 'dedentx'

stringx = 'stringx'
multiline_string_tickx = 'multiline_string_tickx'
multiline_string_quotex = 'multiline_string_quotex'
string_tikcx = 'string_tikcx'
string_quotex = 'string_quotex'

funx = 'funx'
slicex = 'slicex'

lpackagex = 'lpackagex'
rpackagex = 'rpackagex'

interpolationx = 'interpolationx'

namex = 'namex'

numberx = 'numberx'

eopx = 'eopx'

iopx = 'iopx'

bopx = 'bopx'

opx = 'opx'
uopx = 'uopx'
ropx = 'ropx'

udotx = 'udotx'
bdotx = 'bdotx'

semix = 'semix'

commax = 'commax'
colonx = 'colonx'

lparx = 'lparx'
rparx = 'rparx'

lketx ='lketx'
rketx = 'rketx'

lpcax = 'lpcax'
lkcax = 'lkcax'

commentx = 'commentx'
multiline_commentx = 'multiline_commentx'
singleline_commentx = 'singleline_commentx'

spacex = 'spacex'

lexems = (
	bofx,
	eofx,

	linefeedx,
	newlinex,

	lpackagex,
	rpackagex, 
	
	interpolationx,

	indentx,
	dedentx,

	stringx,

	funx,
	slicex,

	numberx,

	namex,

	eopx, 
	
	iopx,

	bopx,
	
	opx,
	uopx,
	ropx,
	
	udotx,
	bdotx,

	semix,
	
	commax,
	colonx,

	lparx,
	rparx,

	lketx,
	rketx,

	lkcax,
	lpcax,
)

# terminal
terminal = [
	childcod,
	enumbol,
	ibol,
	newlinex,
]

# keyword
alloc = 'alloc'
breakk = 'break'
classk = 'class'
critical = 'critical'
continuek = 'continue'
dealloc = 'dealloc'
defk = 'def'
elifk = 'elif'
elsek = 'else'
elwhere = 'elwhere'
error = 'error'
fop = 'fop'
fork = 'for'
ifk = 'if'
importk = 'import'
inline = 'inline'
interface = 'interface'
omp = 'omp'
passk = 'pass'
printk = 'print'
private = 'private'
public = 'public'
read = 'read'
riturn = 'return'
stop = 'stop'
sync = 'sync'
where = 'where'
whilek = 'while'
xip = 'xip'

# spec instruction
allocruc = 'allocruc'
breakruc = 'breakruc'
continueruc = 'continueruc'
criticalruc = 'criticalruc'
deallocruc = 'deallocruc'
ifruc = 'ifruc'
iruc = 'iruc'
elementruc = 'elementruc'
elifruc = 'elifruc'
elseruc = 'elseruc'
elwhereruc = 'elwhereruc'
errorruc = 'errorruc'
fopruc = 'fopruc'
forruc = 'forruc'
importpec = 'importpec'
inlineruc = 'inlineruc'
interfacepec = 'interfacepec'
lexiruc = 'lexiruc'
ompruc = 'ompruc'
passruc = 'passruc'
printruc = 'printruc'
privateruc = 'privateruc'
publicruc = 'publicruc'
readruc = 'readruc'
returnruc = 'returnruc'
stopruc = 'stopruc'
syncruc = 'syncruc'
whereruc = 'whereruc'
whileruc = 'whileruc'
xipruc = 'xipruc'
