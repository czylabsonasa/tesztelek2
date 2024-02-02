# modify the executable path according to your system
# using raw string one can avoid escaping \
# on windows put here the full paths of the executables
python_exe   =   r"python"
matlab_exe   =   r"matlab"
octave_exe   =   r"octave-cli"
julia_exe    =   r"julia"
golang_exe   =   r"go"
nodejs_exe   =   r"node"

######################################################################################

FLOAT_TOL=1e-4
INT_TOL=1e-16 # func módban probléma lehet, mert az app.m mindent lebegopontosan ir ki


# ismert nyelvek (nem minden modban hasznalhato mindegyik)
# elvileg bármire fel lehet készíteni, de jobb szeretem 
# ellenőrizni, hogy nincs-e probléma az adott nyelvvel (lebegőpontos számok...)
_langs=[
  "python","matlab","octave","julia","node.js","golang",
  "binary"
]

_lang2ext=dict({
    "python"   :   "py",
    "matlab"   :   "m",
    "octave"   :   "m",
    "julia"    :   "jl",
    "node.js"  :   "js",
    "golang"   :   "go",
    "binary"   :   "exe" # 
})

# a matlab nincs octave a default
_ext2lang=dict({ 
    "py"   :   "python",
    "m"    :   "octave",
    "jl"   :   "julia" ,
    "js"   :   "node.js",
    "go"   :   "golang",
    "exe"  :   "binary"
})







# func mod parancsai
_fvege=" 1> fake.out 2> fake.out"
def mkFunMode(exe, args):
  return "{} {} {}".format(exe, args, _fvege)

# _lang2cmdF=dict({
    # "python"  :"python3 app.py"+_fvege,
    # "matlab"  :"matlab -nojvm -nodesktop -nosplash < app.m"+_fvege,
    # "octave"  :"octave-cli app.m"+_fvege,
    # "julia"   :"julia app.jl"+_fvege,
    # "node.js" :"node app.js "+_fvege
# })


_lang2cmdF=dict({
    "python"  : mkFunMode(python_exe,   "app.py"),
    "matlab"  : mkFunMode(matlab_exe,   "-nojvm -nodesktop -nosplash < app.m"),
    "octave"  : mkFunMode(octave_exe,   "app.m"), 
    "julia"   : mkFunMode(julia_exe,    "app.jl"),
    "node.js" : mkFunMode(nodejs_exe,   "app.js"),
})


_pvege="< io/{:s}.in 1> act/{:s}.out 2> fake.out"
def mkProgMode(exe, args):
  return "{} {} {}".format(exe, args, _pvege)


_lang2cmdP=dict({
    "python"  : mkProgMode(python_exe,   "solve.py"),
    "octave"  : mkProgMode(octave_exe,   "solve.m"), 
    "julia"   : mkProgMode(julia_exe,    "solve.jl"),
    "node.js" : mkProgMode(nodejs_exe,   "solve.js"),
    "golang"  : mkProgMode(golang_exe,   "run solve.go"),
    "binary"  : mkProgMode("",           "./solve.exe"),
})        


# _lang2cmdP=dict({
    # "python"  :"python3 solve.py "+_pvege,
    # "octave"  :"octave-cli solve.m "+_pvege,
    # "julia"   :"julia solve.jl "+_pvege,
    # "node.js" :"node solve.js "+_pvege,
    # "golang"  :"go run solve.go "+_pvege,
    # "binary"  :"./solve.exe "+_pvege # win ???
# })

_modes=["prog","func"]


_defaultargs=dict({
  "lang":"",
  "problem":"",
  "sol":"",
  "mode":"prog",
  "TEST_DIR":"testdir",
  "PROBLEM_DIR":"problems"
})

config_gen=dict({
  "defaultargs":_defaultargs,
  "modes":_modes,
  "lang2cmd":dict({"prog":_lang2cmdP, "func":_lang2cmdF}),
  "lang2ext":_lang2ext,
  "ext2lang":_ext2lang,
  "langs":_langs
})
