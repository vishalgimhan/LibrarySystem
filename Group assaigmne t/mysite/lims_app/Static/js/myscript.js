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