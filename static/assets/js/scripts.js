jQuery(document).ready(function($) {
    $('.order-button').on('click', function() {
        orderId = $(this).data('id');
        $.ajax({
            url: 'ws/get_order_products/' + orderId,
            dataType: 'json',
            success: function(data) {
                lis = '';
                $.each(data.order_products, function(index, value) {
                    lis += '<li>' + value.product__name + ' | Qtd: ' + value.quantity + '</li>';
                });
                $('.product-list').append(lis);
            }
        });
    });
});