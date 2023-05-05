
const mangas = document.getElementById('manga')
document.addEventListener("DOMContentLoaded", e => {

    fetchData()
})
const fetchData = async () => {
    try {
        const res = await fetch('https://manga-e5091-default-rtdb.firebaseio.com/manga.json')
        const data = await res.json()
        productos(data)
    } catch (error) {
        console.log(error)
    }
}
const productos = data => {
    let elemetos = ''
    data.forEach(item => {
        elemetos += `
        <div class="card mb-4 shadow-lg effect" style="width: 18rem;">
            <img class="card-img-top img-fix" src="${item.imagen}" alt="Card image cap">
            <div class="card-body text-center d-flex flex-column justify-content-center">
                <h5 class="card-title">${item.nombre} #${item.volumen}</h5>
                <p class="card-text">${item.editorial}</p>
                <p class="card-text fs-4">$${item.precio}</p>
                <a href="#" class="btn btn-primary ">Ver Producto</a>
            </div>
        </div>
    `
    });
    mangas.innerHTML = elemetos
}



