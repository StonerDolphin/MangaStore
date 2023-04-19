$(document).ready(function(){
    $("#contactForm").submit(function (e){
        e.preventDefault();
        var email=$("#emailInput").value();
        var comentario=$("commentInput").value();
        
        $(".error").remove();
        if (comentario.length == 0) {
            $('#commentInput').after('<span class="error">Este campo es obligatorio</span>');
        }else if (comentario.length < 3) {
            $(".error").remove();
            $('#commentInput').after('<span class="error">Este campo debe tener mínimo 3 caracteres</span>');
        }
        if (email.length == 0) {
            $('#emailInput').after('<span class="error">Este campo es obligatorio</span>');
        } else {
            var regEx = /^[\w-.]+@([\w-]+.)+[\w-]{2,4}$/
            var validEmail = regEx.test(email);
            if (!validEmail) {
            $('#emailInput').after('<span class="error">Ingrese un Email válido</span>');
            }
        }
    })
})