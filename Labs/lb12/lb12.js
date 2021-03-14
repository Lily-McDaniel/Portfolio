//fortune
function getInfo(){
        var x = document.getElementById("form1");
        var text = "Hi, " + x.elements[0].value + ". You will have " + x.elements[1].value + " children in the future. You will live in " + x.elements[2].value + " and you will be married to " + x.elements[3].value + ".";

        document.getElementById("fortune").innerHTML = text;
      }
//Cylinder Volume
function radius(){
        var w = document.getElementById("form2");
        var r = w.elements[0].value;
        var h = w.elements[1].value;
        var volume = "The volume is " + (3.14 * r * r * h).toFixed(2); //round to 2 decimal places

        document.getElementById("radiusEq").innerHTML = volume;

}
//Quadratic formula
function quadratic(){
        var y = document.getElementById("form3");
        var a = y.elements[0].value;
        var b = y.elements[1].value;
        var c = y.elements[2].value;

        var discriminant = (b * b) - (4 * a * c);
        var xv1 = (((-1 * b) + (Math.sqrt(discriminant)))/(2*a)).toFixed(2); //round to 2 decimal places
        var xv2 = (((-1 * b) - (Math.sqrt(discriminant)))/(2*a)).toFixed(2); //round to 2 decimal places

        var finalOutput = "The discriminant is "+ discriminant + " and the roots are " + xv1 + " and " + xv2+ ".";
  document.getElementById("quadraticEq").innerHTML = finalOutput;
}
//navigation bar open and close functions
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    }
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    }
