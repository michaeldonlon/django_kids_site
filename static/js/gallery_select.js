// static/js/gallery_select.js

var currentTime = new Date();
index_year = currentTime.getFullYear()-2000;
actual_year = index_year;
actual_month = currentTime.getMonth() + 1;
var month_dictionary = [
   { 'short_name':"Jan", 'number': "01" },
   { 'short_name':"Feb", 'number': "02" },
   { 'short_name':"Mar", 'number': "03" },
   { 'short_name':"Apr", 'number': "04" },
   { 'short_name':"May", 'number': "05" },
   { 'short_name':"Jun", 'number': "06" },
   { 'short_name':"Jul", 'number': "07" },
   { 'short_name':"Aug", 'number': "08" },
   { 'short_name':"Sep", 'number': "09" },
   { 'short_name':"Oct", 'number': "10" },
   { 'short_name':"Nov", 'number': "11" },
   { 'short_name':"Dec", 'number': "12" },
];

document.getElementById("yearbox").innerHTML = "20" + index_year;
document.getElementById("rightarrowcell").style.color = 'Gainsboro';
document.getElementById("rightarrow").style.cursor = 'default';

deactivate_month()

function move_year(direction){
   if(direction == "down" && index_year > 18){
      index_year -= 1;
   }else if(direction == "up" && index_year < actual_year){
      index_year += 1;
   }
   
   document.getElementById("yearbox").innerHTML = "20" + index_year;

   if(index_year === 18){
      document.getElementById("leftarrowcell").style.color = 'Gainsboro';
      document.getElementById("leftarrow").style.cursor = 'default';
   }else{document.getElementById("leftarrowcell").style.color = 'white';
      document.getElementById("leftarrow").style.cursor = 'pointer';
   }
   if(index_year === actual_year){
      document.getElementById("rightarrowcell").style.color = 'Gainsboro';
      document.getElementById("rightarrow").style.cursor = 'default';
   }else{document.getElementById("rightarrowcell").style.color = 'white';
      document.getElementById("rightarrow").style.cursor = 'pointer';
   }

   deactivate_month()
   
}

function deactivate_month(){
   for (let i = 1; i < 13; i++) {
      var current_cell = "month_cell_"+i;
      if(index_year === 18 && i <= 4){
         document.getElementById(current_cell).innerHTML = '<a style="cursor:default;" href="javascript:void(0)">'+month_dictionary[i-1].short_name+'</a>';
         document.getElementById(current_cell).style.color = 'Gainsboro';
      }else if(index_year === actual_year && i > actual_month){
         document.getElementById(current_cell).innerHTML = '<a style="cursor:default;" href="javascript:void(0)">'+month_dictionary[i-1].short_name+'</a>';
         document.getElementById(current_cell).style.color = 'Gainsboro';
      }else{
         var html_text = '<a href="/kidpagegallery/20'+index_year+'_'+i.toString().padStart(2,'0')+'/">'+month_dictionary[i-1].short_name+'</a>';
         document.getElementById(current_cell).innerHTML = html_text;
         document.getElementById(current_cell).style.color = 'DarkSlateGrey';
      }
   }
}