// static/js/gallery_modal.js

function modalclick(image_id, thumb_src) {
  var modal = document.getElementById("myModal");

  // Get the image and insert it inside the modal
  var img = document.getElementById(image_id);
  var modalImg = document.getElementById("img01");
  modal.style.display = "block";
  
  // Create a regex to omit the '_thumb' part of the 
  // url and use the rest 

  //match this to drop the thumbs url
  var img_name_patt = /(?<=thumbs\/).+(?=_thumb)/i;
  var img_name = thumb_src.match(img_name_patt);
  img_name = img_name + ".jpg";

  //get the full domain
  var domain_url = thumb_src.substring(0, thumb_src.lastIndexOf('thumbs'));

  modalImg.src = domain_url+img_name;

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() { 
  modal.style.display = "none";
  }
}