// static/js/gallery_page.js

var currentTime = new Date();
actual_year = currentTime.getFullYear();
actual_month = currentTime.getMonth() + 1;

var page_date = document.getElementById("page-title").innerText
page_year = parseInt(page_date.substr(0, 4));
page_month = parseInt(page_date.slice(-2));

var month_dictionary = [
   { 'long_name':"January", 'number': "01" },
   { 'long_name':"February", 'number': "02" },
   { 'long_name':"March", 'number': "03" },
   { 'long_name':"April", 'number': "04" },
   { 'long_name':"May", 'number': "05" },
   { 'long_name':"June", 'number': "06" },
   { 'long_name':"July", 'number': "07" },
   { 'long_name':"August", 'number': "08" },
   { 'long_name':"September", 'number': "09" },
   { 'long_name':"October", 'number': "10" },
   { 'long_name':"November", 'number': "11" },
   { 'long_name':"December", 'number': "12" },
];

var arrow_dictionary = {'backnav':'&lt;', 'fwdnav':'&gt;'}

if(page_month === 5 && page_year === 2018){
   document.getElementById("backnav").innerHTML = '<a style="cursor:default; color:#C0C0C0; text-shadow:0px 4px #DCDCDC;" href="javascript:void(0)">&lt;</a>';
   var next_month = page_year.toString() + '_' + ((page_month + 1).toString().padStart(2,'0'));
   replace_link("fwdnav", next_month)
}else if(page_month === actual_month && page_year === actual_year){
   document.getElementById("fwdnav").innerHTML = '<a style="cursor:default; color:#C0C0C0; text-shadow:0px 4px #DCDCDC;" href="javascript:void(0)">&gt;</a>';
   var prev_month = page_year.toString() + '_' + ((page_month - 1).toString().padStart(2,'0'));
   replace_link("backnav", prev_month)
}else if (page_month === 1){
   var prev_month = (page_year - 1).toString() + '_12'
   replace_link("backnav", prev_month)
   var next_month = page_year.toString() + '_' + ((page_month + 1).toString().padStart(2,'0'));
   replace_link("fwdnav", next_month)
}else if (page_month === 12){
   var prev_month = page_year.toString() + '_' + ((page_month - 1).toString().padStart(2,'0'));
   replace_link("backnav", prev_month)
   var next_month = (page_year + 1).toString() + '_01'
   replace_link("fwdnav", next_month)
}else{
   var prev_month = page_year.toString() + '_' + ((page_month - 1).toString().padStart(2,'0'));
   replace_link("backnav", prev_month)
   var next_month = page_year.toString() + '_' + ((page_month + 1).toString().padStart(2,'0'));
   replace_link("fwdnav", next_month)
}

function replace_link(id, date){
   var html_text = '<a href="/kidpagegallery/'+date+'/">'+arrow_dictionary[id]+'</a>';
   document.getElementById(id).innerHTML = html_text;
}

document.getElementById("page-title").innerHTML = '<h1>'+month_dictionary[page_month-1].long_name+" "+page_year.toString()+'</h1>';
