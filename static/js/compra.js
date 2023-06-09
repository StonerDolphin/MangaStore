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
                minlength: 2,
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
            nombre:{
                required:"Debe ingresar su nombre completo",
                maxlength:"Ingrese un nombre valido"
            },
            run:{
                required:"Debe ingresar su run",
                minlength:"Ingrese un run valido",
                maxlength:"Ingrese un run valido"
            },
            direccion:{
                required:"Debe ingresar una dirección",
                minlength:"Ingrese una dirección valida ",
                maxlength:"Ingrese una dirección valida"
            },
            comuna:{
                required:"Debe ingresar una comuna",
                minlength:"Ingrese una comuna valida ",
                maxlength:"Ingrese una comuna valida"
            },
            region:{
                required:"Debe ingresar una región",
                minlength:"Ingrese una región valida ",
                maxlength:"Ingrese una región valida"
            },
            cpostal:{
                required:"Debe ingresar un código postal",
                maxlength:"Ingrese un código postal valido"
            },
            ntarjeta:{
                required:"Debe ingresar su numero de tarjeta",
                minlength:"Ingrese un numero de tarjeta valido ",
                maxlength:"Ingrese un numero de tarjeta valido"
            },
            mvencimiento:{
                required:"Ingrese el mes de vencimiento de su tarjeta",
                minlength:"Ingrese un mes valido en formato numérico ",
                maxlength:"Ingrese un mes valido en formato numérico "
            },
            avencimiento:{
                required:"Ingrese el año de vencimiento de su tarjeta",
                minlength:"Ingrese un año valido en formato ",
                maxlength:"Ingrese un año valido en formato "
            },
            cvv:{
                required:"Ingrese el código de seguridad de su tarjeta",
                minlength:"Ingrese un código de seguridad valido",
                maxlength:"Ingrese un código de seguridad valido"
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