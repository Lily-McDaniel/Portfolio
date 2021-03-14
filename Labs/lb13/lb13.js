

function calculateSupply(){
  var myAge=document.getElementById('myAge').value;
  var maxAge=100;
  var cupsAmount= document.getElementById('myItem').value;
  var totalSupply=(cupsAmount * 365) * (maxAge - myAge);
  var result= document.getElementById('leftXX').value=totalSupply;
}
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
