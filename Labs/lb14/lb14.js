//side Bar
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

//where the table begins to display
var row = 1;
console.log(row);
var add = document.getElementById("add");
console.log(add);

//function to display items and prices, and quantity
function subPrice(){
  var itemList = ["Banana","Apple","Carrots","Mixed Berries","Smoothie Packet","Chicken"];
  var priceList = [1.05,0.99,3.99,4.50,5.99,10.99];
  var qtyList = [null,null,null,null,null,null];

  var qty1 = document.getElementById('Banana').value;
  var qty2 = document.getElementById('quantity2').value;
  var qty3 = document.getElementById('quantity3').value;
  var qty4 = document.getElementById('quantity4').value;
  var qty5 = document.getElementById('quantity5').value;
  var qty6 = document.getElementById('quantity6').value;

  var userEnter = [qty1,qty2,qty3,qty4,qty5,qty6]; console.log(userEnter);
//subtotals
  var subPrice = [null,null,null,null,null,null];
  var totalPrice = 0;

  console.log(subPrice);

  var display = document.getElementById("display");


//subtotals for loop
   for(var i = 0; i < itemList.length; i++){
    if(userEnter[i] != 0){
      qtyList[i] = userEnter[i];
      subPrice[i] = qtyList[i] * priceList[i];
      totalPrice += subPrice[i];
      console.log(qtyList[i]);
      console.log(subPrice);
      console.log(totalPrice);
    }
  }
//adds new rows everytime press add
  for(var i =0 ; i < itemList.length; i++){

  var newrow = display.insertRow(row++);

  var cell1 = newrow.insertCell(0);
  var cell2 = newrow.insertCell(1);
  var cell3 = newrow.insertCell(2);
  var cell4 = newrow.insertCell(3);



   cell1.innerHTML = itemList[i];
   cell2.innerHTML = qtyList[i];
   cell3.innerHTML = priceList[i];
   cell4.innerHTML = subPrice[i].toFixed(2);
   }
   document.getElementById("total2").innerHTML = "$"+totalPrice.toFixed(2); // round to two decimal places
}
//function to confirm checking out
function buy() {
  var txt;
  if (confirm("Would you like to complete the purchase?")) {
    txt = "Thank you for shopping with us. Come again soon!";
  } else {
    txt = "You canceled the purchase.";
  }
  document.getElementById("confirmBuy").innerHTML = txt;
}
