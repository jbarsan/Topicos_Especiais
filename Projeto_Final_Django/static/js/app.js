// Gatilho para abrir o modal
$(document).ready(function(){
    $('#modal-rodape').modal();
    $('#btn-dropdown-perfil').dropdown({
        belowOrigin: true
    });
  });

  // Função que chama o parallax.
  // É preiciso criar uma função para que não ocorra problemas
  // com o parallax.
function chamaParallax(){
    $('.parallax').parallax();
}

$('.menu-pai').click(function(e){
    e.preventDefault();
    $(this).next('ul').slideToggle('slow');
    $('.menu-filho').not($(this).next()).slideUp('slow');
});

$('#btn-sidebar').click(function(e){
    e.preventDefault();
    $('#wrapper').toggleClass('toggled');
    $('#btn-sidebar').toggleClass('toggled');
});

// Só cria o parallax depois que toda a página for redenrizada
window.load = chamaParallax();

