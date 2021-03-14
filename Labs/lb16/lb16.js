//play ninjas
var user = prompt("Pssst. Hello there... Who are you?");
var c = confirm("Do you want to play Ninjas");
if (c){
  var ninja = {
    beltColor: prompt("What level of belt does your ninja have?"),
    ninjaName: prompt("What is the ninja's name?"),
    powers: prompt("Tell me 3 super powers: you seperate each power with a coma").split(",")
  };
  alert("Well " + user + ", your ninja, " + ninja.ninjaName + ", has a " + ninja.beltColor + " belt, and the powers of: " + ninja.powers[0] + ", " + ninja.powers[1] + " and " + ninja.powers[2] + "! Let's play!");
}
console.log("GoodBye!!!");
//side nav
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
//typewriting after the ninja disappears
var i = 0;
var txt = 'Pssssst! You made the ninja disappear. Goodluck finding them again.';
var speed = 100;

function replace() {
  if (i < txt.length) {
    document.getElementById("psst").innerHTML += txt.charAt(i);
    i++;
    setTimeout(replace, speed);
  }
}
//jQuery practice
// Line 3 tells the browers to wait until all html, css has loaded before running this js file
$(document).ready(function(){
//jQuery methods go here...
  //sample of jQ slide action
  $("#ninja").click(function(){
    $("#ninja").slideToggle(200);
  });
  $("#scream").hover(function(){
    $("#scream").fadeToggle(1000);
  });
  //sample of jQ fade action
  $("#sword").hover(function(){
    $("#sword").fadeToggle(1000);
  });
  //sample of jQ fade action
  $("#punch").hover(function(){
    $("#punch").fadeToggle(1000);
  });
  $("button").click(function(){
    var div = $("div");
    div.animate({height: '98%', opacity: '0.4'}, "slow");
    div.animate({width: '98%', opacity: '0.8'}, "slow");
    div.animate({height: '100px', opacity: '0.4'}, "slow");
    div.animate({width: '100px', opacity: '0.8'}, "slow");
  });
});
