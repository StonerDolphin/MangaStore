function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if(cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');




let btns = document.querySelectorAll(".carta , .botones button")
btns.forEach(btn=>{
    btn.addEventListener("click", agregar)
})
function agregar(e){
    let mangaId = e.target.value
    let url = "/agregar"
    let data = {id:mangaId}
    fetch(url, {
        method: "POST",
        headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    })
        .then(res=>res.json())
        .then(data=>{
            console.log(data)
        })
        .catch(error=>{
            console.log(error)
        })
}



document.addEventListener('DOMContentLoaded', function () {
    const botones = document.querySelectorAll('.botones');
    const cartas = document.querySelectorAll('.carta');

    botones.forEach(boton => {
        boton.addEventListener('click', () => {
            Swal.fire('Se agrego al carrito');
            // Aquí puedes agregar la lógica adicional para agregar el producto al carrito
        });
    });

    cartas.forEach(carta => {
        carta.addEventListener('click', () => {
            Swal.fire('Se agrego al carrito');
            // Aquí puedes agregar la lógica adicional para agregar el producto al carrito
        });
    });
});