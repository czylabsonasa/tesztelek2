// szerző: Kántor Dániel (thx!)

const fs = require('fs');

const solve = require('./solve.js');

var cnt = 0;

while(true){
    let fin = `./io/${cnt}.in`;
    let fout = `./act/${cnt}.out`;


    if(!fs.existsSync(fin)) break;

    let ok = 1;
    let t0 = process.hrtime();
    try{
        solve(fin,fout);
    }
    catch(ex){
        ok = 0;
    }

    t0 = process.hrtime(t0);
    mt=t0[0]+t0[1]/1e9;

    fs.writeFileSync(`./act/${cnt}.info`,`${ok} ${mt.toFixed(4)}`);
    
    cnt++;
}
