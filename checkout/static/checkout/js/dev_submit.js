function form2form(formA, formB) {
    $(':input[name]', formA).each(function() {
        $('[name=' + $(this).attr('name') +']', formB).val($(this).val())
    })
}

var form_original = document.getElementById('payment-form');
var form_dev = document.getElementById('develop-form');

form_dev.addEventListener('submit', function(e) {
    e.preventDefault();

    var selectedCountry = $("#id_country", form_original).children("option:selected").val();

    $("#dev_full_name").val($("#id_full_name", form_original).val());
    $("#dev_email").val($("#id_email", form_original).val());
    $("#dev_phone_number").val($("#id_phone_number", form_original).val());
    $("#dev_postcode").val($("#id_postcode", form_original).val());
    $("#dev_town_or_city").val($("#id_town_or_city", form_original).val());
    $("#dev_street_address1").val($("#id_street_address1", form_original).val());
    $("#dev_street_address2").val($("#id_street_address2", form_original).val());
    $("#dev_county").val($("#id_county", form_original).val());
    $("#dev_country").val(selectedCountry);
    $("#dev_save_info").val($("#id_save_info", form_original).val());
    $("#dev_client_secret").val(clientSecret);
    
    form_dev.submit();
});