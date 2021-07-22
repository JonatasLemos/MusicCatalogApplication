const message_ele = document.getElementById("message-container");
if(message_ele){
    setTimeout(function () {
        message_ele.style.display = "none";}, 3000);
}
$(document).ready(function(){
  $('#search-album').click(function(){
      const add_artist = document.getElementById("add_artist");
      const add_album = document.getElementById("add_album");
      const rates = document.getElementById("rates");
      if ((add_artist.checkValidity())&&(add_album.checkValidity())&&(rates.checkValidity())) {
          $("#album-header").hide();
          $("#form-album").hide();
          $("#spinning").show();
      }
    });
});
