function mostrarVistaPrevia() {
    var archivo = document.getElementById("imagen").files[0];
    if (archivo) {
      var lector = new FileReader();
      lector.onload = function(e) {
        document.getElementById("vista-previa").setAttribute("src", e.target.result);
      };
      lector.readAsDataURL(archivo);
    }
  }
