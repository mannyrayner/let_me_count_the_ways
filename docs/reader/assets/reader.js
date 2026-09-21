"use strict";
const form=document.querySelector("#filters");
if(form){
 const rows=Array.from(document.querySelectorAll("#case-table tbody tr"));
 const count=document.querySelector("#visible-count");
 function apply(){
  const query=form.querySelector("#query").value.toLocaleLowerCase().trim();
  const work=form.querySelector("#work").value;
  const status=form.querySelector("#status").value;
  const p=Number(form.querySelector("#p-min").value);
  let n=0;
  for(const row of rows){
   const visible=(!query||row.dataset.search.includes(query))&&(!work||row.dataset.work===work)&&(!status||row.dataset.status===status)&&Number(row.dataset.p)>=p;
   row.hidden=!visible;if(visible)n++;
  }
  count.textContent=n+" of "+rows.length+" occurrences";
  document.querySelector("#no-results").hidden=n!==0;
 }
 form.addEventListener("input",apply);form.addEventListener("change",apply);
 form.addEventListener("reset",()=>setTimeout(apply,0));
 form.addEventListener("submit",event=>event.preventDefault());apply();
}
