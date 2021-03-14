
function myFunction(){
  var p = document.createElement("p");
  var form = document.getElementById("myform");
  p.innerHTML = "// Name: " + form.elements[0].value + " // Position: " + form.elements[1].value + " // ID Number: " + form.elements[2].value + " // Phone Number: " + form.elements[3].value;
  document.body.appendChild(p);
}
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
