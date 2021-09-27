var thedate = document.getElementById("kidimage-header").innerText
theyear = thedate.substr(0, 4);
themonth = parseInt(thedate.slice(-2));

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

document.getElementById("kidimage-header").innerHTML = '<h1>'+month_dictionary[themonth-1].long_name+" "+theyear+'</h1>';