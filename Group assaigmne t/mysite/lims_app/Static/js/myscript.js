$(document).on('click', '.remove-cart', function(){
    console.log('Remove button clicked');  // Check if the click event is firing
    var id = $(this).attr("pid").toString();
    var eml = this;
    $.ajax({
        type: "GET",
        url: "/removebag",
        data:{
            'bk_id': id
        },
        success: function(data){
            console.log('Ajax request successful');  // Check if the Ajax request is successful
            console.log($(eml).closest('.row'));  // Check if the closest .row element is found
            $(eml).closest('.row').remove();
        }
    });
});

$(document).on('click', '.plus-wishlist', function(){
    let id = $(this).attr('pid').toString();
    let thisBtn = $(this);
    $.ajax({
        type:'GET',
        url: '/pluswishlist',
        data:{
            'bk_id':id,
        },
        success:function(response){
            thisBtn.removeClass('btn-success plus-wishlist');
            thisBtn.addClass('btn-danger minus-wishlist');

            // Update the number of items in the wishlist
            $('#wishitem').text(response.wishitem);
        }
    });
});

$(document).on('click', '.minus-wishlist', function(){
    let id = $(this).attr('pid').toString();
    let thisBtn = $(this);
    $.ajax({
        type:'GET',
        url: '/minuswishlist',
        data:{
            'bk_id':id,
        },
        success:function(response){
            thisBtn.removeClass('btn-danger minus-wishlist');
            thisBtn.addClass('btn-success plus-wishlist');

            // Update the number of items in the wishlist
            $('#wishitem').text(response.wishitem);
        }
    });
});

$(document).on('click', '.plus-baglist', function(){
    let id = $(this).attr('pid').toString();
    let thisBtn = $(this);
    $.ajax({
        type:'GET',
        url: '/plusbaglist',
        data:{
            'bk_id':id,
        },
        success:function(response){
            thisBtn.removeClass('btn-success plus-baglist');
            thisBtn.addClass('btn-secondary minus-baglist');

            // Update the number of items in the baglist
            $('#totalitem').text(response.totalitem);
        }
    });
});

$(document).on('click', '.minus-baglist', function(){
    let id = $(this).attr('pid').toString();
    let thisBtn = $(this);
    $.ajax({
        type:'GET',
        url: '/minusbaglist',
        data:{
            'bk_id':id,
        },
        success:function(response){
            thisBtn.removeClass('btn-secondary minusbaglist');
            thisBtn.addClass('btn-success plusbaglist');
            
            // Update the number of items in the baglist
            $('#totalitem').text(response.totalitem);
        }
    });
});

window.onload = function() {
    var inputElement = document.getElementById("start_date");
    var returnElement = document.getElementById("return_date");
    console.log(inputElement.value)

    var dateString = inputElement.value;

    if (dateString) {
        // Parse the date string into a Date object
        var currentDate = new Date(dateString);

        // Increment the date by 14 days
        currentDate.setDate(currentDate.getDate() + 14);

        // Format the new date as a string in "YYYY-MM-DD" format
        var newDateString = currentDate.toISOString().split('T')[0];

        // Update the input with the new date
        returnElement.value = newDateString;
      } else {
        alert("Please select a date first.");
      }
}

// window.onload = function() {
//     var inputElement = document.getElementById("orderdate");
//     var returnElement = document.getElementById("returndate");
//     var diffElement = document.getElementById("date_difference");
//     var fineElement = document.getElementById("fine");

//     console.log(inputElement.textContent)

//     var dateString = inputElement.textContent;
//     var dateString2 = returnElement.textContent;

//     if (dateString) {
//         // Parse the date string into a Date object
//         var currentDate = new Date(dateString);
//         var returnDate = new Date(dateString2);

//         // Increment the date by 14 days
//         // currentDate.setDate(currentDate.getDate() + 14);

//         // Format the new date as a string in "YYYY-MM-DD" format
//         var newDateString = currentDate.toISOString().split('T')[0];

//         // Update the input with the new date
//         // diffElement.textContent= newDateString;
//         var cal = (returnDate - currentDate)/(1000*60*60*24);
//         diffElement.textContent = cal;
//         // diffElement.textContent = (returnDate - currentDate)/(1000*60*60*24);

//         if(cal < 0){
//             var amount = Math.abs(cal)*10;
//             fineElement.textContent = "Rs." + amount;}
//         else{
//             fineElement.textContent = "Rs. 0";}

//       } 
//     //   else {
//     //     alert("Please select a date first.");
//     //   }
// }

document.addEventListener("DOMContentLoaded", function () {
    var orderDateCells = document.querySelectorAll(".orderdate");
    var returnDateCells = document.querySelectorAll(".returndate");
    var dateDifferenceCells = document.querySelectorAll(".datedifference");
    var fineCells = document.querySelectorAll(".fine");

    for (var i = 0; i < orderDateCells.length; i++) {
      var orderDate = new Date(orderDateCells[i].innerText);
      var returnDate = new Date(returnDateCells[i].innerText);

      // Calculate the time difference in milliseconds
      var timeDifference = returnDate - orderDate;

      // Convert the time difference to days
      var daysDifference = timeDifference / (1000 * 60 * 60 * 24);

      // Update the date_difference cell with the calculated difference
      dateDifferenceCells[i].innerText = Math.round(daysDifference) + " days";

        // Calculate the fine
        if (daysDifference < 0) {
            var amount = Math.abs(daysDifference)*10;
            fineCells[i].innerText = "Rs." + amount;}
        else{
            fineCells[i].innerText = "Rs. 0";}
    }
  });