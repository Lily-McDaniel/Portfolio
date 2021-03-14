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

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
