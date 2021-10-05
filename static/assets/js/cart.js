document.addEventListener("DOMContentLoaded", () => {
  var sum = 0;
  var subtotal = document.getElementById('my_subtotal');
  var price_list = document.getElementsByClassName('my_price');
  var total = document.getElementById('my_total');
  var quantity_list = document.getElementsByClassName('my_quantity');
  for (var i = 0, j = price_list.length; i<j; i++){
    var price = parseInt(price_list[i].getElementsByTagName('span')[0].innerHTML);
    var quantity = parseInt(quantity_list[i].getElementsByTagName('input').value);
    sum += price * price * quantity;

  }
  subtotal.innerHTML = sum;
  });