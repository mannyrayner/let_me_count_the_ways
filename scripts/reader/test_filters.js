// Exercise the shipped event handlers with real generated row datasets.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const rows=JSON.parse(fs.readFileSync(0,'utf8')).map(dataset=>({dataset,hidden:false}));
const fields={'#query':{value:''},'#work':{value:''},'#status':{value:''},'#p-min':{value:'0'}};
const events={},count={},empty={};
const form={querySelector:key=>fields[key],addEventListener:(name,fn)=>events[name]=fn};
const document={querySelector:key=>({'#filters':form,'#visible-count':count,'#no-results':empty})[key],querySelectorAll:()=>rows};
vm.runInNewContext(fs.readFileSync('scripts/reader/reader.js','utf8'),{document,setTimeout:fn=>fn()});
const visible=()=>rows.filter(r=>!r.hidden).length;
assert.equal(visible(),252);
fields['#p-min'].value='3';events.input();assert.equal(visible(),23);
fields['#p-min'].value='0';fields['#work'].value='gissing-the-odd-women';events.change();assert.equal(visible(),12);
fields['#work'].value='benedictsson-pengar';events.change();assert.equal(visible(),0);assert.equal(empty.hidden,false);
fields['#work'].value='';fields['#query'].value='no-such-text-7392';events.input();assert.equal(visible(),0);
fields['#query'].value='';events.reset();assert.equal(visible(),252);assert.equal(empty.hidden,true);
let prevented=false;events.submit({preventDefault:()=>prevented=true});assert(prevented);
console.log('Reader filter events verified against all 252 generated rows.');
