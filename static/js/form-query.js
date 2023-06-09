//validaciones footer
$(document).ready(function(){
    let email=$("#emailInput")
    let mensaje=$("#commentInput")
    $("#contactForm").validate({
        rules:{
            correo:{
                required: true,
                email: true
            },
            mensaje:{
                required: true,
                minlength:5,
                maxlength:1000
            }
        },
        messages:{
            correo:{
                required:"Ingrese una direccion de correo valido.",
                email:"Debe Ingresar un correo Electronico"
            },
            mensaje:{
                required:"Se debe escribir un comentario",
                minlength:"El comentario debe contener un minimo de 4 letras",
                maxlength:"El comentario debe contener un maximo de 1000 letras"
            }
        }
    })
    
    $("#guardar").click(function(){
        if($("#contactForm").valid()==false){
            return;
        }
    })

    $()
})


