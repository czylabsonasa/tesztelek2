FLOAT_TOL=1e-6
INT_TOL=1e-16 # func módban probléma lehet, mert az app.m mindent lebegopontosan ir ki


# ismert nyelvek (nem minden modban hasznalhato mindegyik)
# elvileg bármire fel lehet készíteni, de jobb szeretem 
# ellenőrizni, hogy nincs-e probléma az adott nyelvvel (lebegőpontos számok...)
_langs=[
  "python","matlab","octave","julia","node.js","golang",
  "binary"
]

_lang2ext=dict({
    "python"   : "py",
    "matlab"   : "m",
    "octave"   : "m",
    "julia"    : "jl",
    "node.js"  : "js",
    "golang"   : "go",
    "binary"   : "exe" # 
})

# a matlab nincs octave a default
_ext2lang=dict({ 
    "py"   : "python",
    "m"    : "octave",
    "jl"   : "julia" ,
    "js"   : "node.js",
    "go"   : "golang",
    "exe"     : "binary"
})







# func mod parancsai
_fvege=" 1> fake.out 2> fake.out"
_lang2cmdF=dict({
    "python"  :"python3 app.py"+_fvege,
    "matlab"  :"matlab -nojvm -nodesktop -nosplash < app.m"+_fvege,
    "octave"  :"octave-cli app.m"+_fvege,
    "julia"   :"julia app.jl"+_fvege,
    "node.js" :"node app.js "+_fvege
})

_pvege="< io/{:s}.in 1> act/{:s}.out 2> fake.out"
_lang2cmdP=dict({
    "python"  :"python3 solve.py "+_pvege,
    "octave"  :"octave-cli solve.m "+_pvege,
    "julia"   :"julia solve.jl "+_pvege,
    "node.js" :"node solve.js "+_pvege,
    "golang"  :"go run solve.go "+_pvege,
    "binary"  :"./solve.exe "+_pvege # win ???
})

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
