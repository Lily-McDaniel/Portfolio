// this is just jQuery practice
// Line 3 tells the browers to wait until all html, css has loaded before running this js file
$(document).ready(function(){
//jQuery methods go here...
  //sample of jQ move object left
  $(".buttonL").click(function(){
    $("#divv").animate({
      left: '-=50px',
    });
  });
    //sample of jQ move object right
  $(".buttonR").click(function(){
    $("#divv").animate({
      left: '+=50px',
    });
  });
    //sample of jQ move object up
  $(".buttonU").click(function(){
    $("#divv").animate({
      'marginTop': '-=50px',
    });
  });
    //sample of jQ move object down
  $(".buttonD").click(function(){
  $("#divv").animate({
      'marginTop': '+=50px',
    });
  });
    //sample of jQ change object opacity
  $(".buttonOpa").click(function(){
    $("#divv").animate({
      opacity: '-=0.20',
    });
  });
    //sample of jQ change square into circle
  $(".buttonCirc").click(function(){
    $("#divv").animate({
      "border-radius": '50%',
    });
  });
    //sample of jQ change circle into square
  $(".buttonSqua").click(function(){
    $("#divv").animate({
      "border-radius": '0%',
    });
  });
    //sample of jQ change square size smaller
  $(".buttonSizS").click(function(){
    $("#divv").animate({
      height: '-=50px',
      width: '-=50px'
    });
  });
    //sample of jQ change square size larger
  $(".buttonSizL").click(function(){
    $("#divv").animate({
      height: '+=50px',
      width: '+=50px'
    });
  });
    //sample of jQ to reset the square
  $(".buttonReset").click(function(){
    $("#divv").animate({
      width: '200px',
      height: '200px',
      opacity: '+=1',
      "background-color": 'crimson',
      "border-radius": '5px',
      "text-align": 'center'
    });
  });
});

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
