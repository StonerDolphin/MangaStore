$(document).ready(function(){
    let nombre = $("#nombre")
    let email = $("#email")
    let direccion = $("#direccion")
    let comuna = $("#comuna")
    let region = $("#region")
    let cpostal = $("#cpostal")
    let run = $("#run")
    let ntarjeta = $("#ntarjeta")
    let mvencimiento = $("#mvencimiento")
    let avencimiento = $("#avencimiento")
    let cvv = $("#cvv")

    $("#formulario-compra").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 1,
                maxlength: 100
            },
            email:{
                required: true,
                email:true
            },
            direccion:{
                required: true,
                minlength: 3,
                maxlength: 100
            },
            comuna:{
                required: true,
                minlength: 3,
                maxlength: 50
            },
            region:{
                required: true,
                minlength: 3,
                maxlength: 100
            },
            cpostal:{
                required: true,
                minlength: 1,
                maxlength: 10
            },
            run:{
                required: true,
                minlength: 9,
                maxlength: 15
            },
            ntarjeta:{
                required: true,
                minlength: 12,
                maxlength: 20
            },
            mvencimiento:{
                required: true,
                minlength: 1,
                maxlength: 2
            },
            avencimiento:{
                required: true,
                minlength: 2,
                maxlength: 4
            },
            cvv:{
                required: true,
                minlength: 3,
                maxlength: 3
            }
        },
        messages:{
            email:{
                required:"Ingrese una direccion de correo",
                email:"Debe Ingresar un correo Electronico valido"
            },
            run:{
                required:"Debe ingresar su run",
                minlength:"Ingrese un run valido",
                maxlength:"Ingrese un run valido"
            },
            direccion:{
                required:"Debe ingresar una direccion",
                minlength:"Ingrese una direccion valida ",
                maxlength:"Ingrese una direccion valida"
            }
        }
    })
    
    $("#guardarC").click(function(){
        if($("#formulario-compra").valid()==false){
            return;
        }
    })

    $()
})