$(document).ready(function () {
    $('select').material_select();
    $('#btn-dropdown-perfil').dropdown({
        belowOrigin: true
    });
    $('.modal').modal({
        dismissible: true,
        startingTop: '4%',
        endingTop: '10%',
    });
});


$(document).ready(function () {
    $('.telefone').mask('(00) 00000-0000');
    $('.cpf').mask('000.000.000-00'), {reverse: true};
    $('.cep').mask('00000-000');
    $('.num-doc').mask('000');
    $('.ano-doc').mask('0000');
    $('.process-num').mask('00.0000/0000');
});


axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "XCSRF-TOKEN";

