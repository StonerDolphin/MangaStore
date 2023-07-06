function descargarBoleta(event) {
        event.preventDefault(); // Evitar recarga de página

        Swal.fire({
            title: 'Descargando boleta',
            html: 'La boleta se descargará en <b></b> milisegundos.',
            timer: 2000,
            timerProgressBar: true,
            didOpen: () => {
                Swal.showLoading();
                const b = Swal.getHtmlContainer().querySelector('b');
                timerInterval = setInterval(() => {
                    b.textContent = Swal.getTimerLeft();
                }, 100);
            },
            willClose: () => {
                clearInterval(timerInterval);
            }
        }).then((result) => {
            if (result.dismiss === Swal.DismissReason.timer) {
                console.log('La alerta se cerró automáticamente por el temporizador');
            }
        });
    }
    function enviarBoleta() {
  Swal.fire({
    title: '¿Enviar boleta al correo?',
    text: '¿Deseas enviar la boleta al correo electrónico registrado?',
    icon: 'question',
    showCancelButton: true,
    confirmButtonText: 'Sí',
    cancelButtonText: 'No'
  }).then((result) => {
    if (result.isConfirmed) {
      // Aquí puedes agregar la lógica para enviar la boleta al correo
      Swal.fire(
        'Boleta enviada',
        'La boleta ha sido enviada correctamente al correo electrónico.',
        'success'
      );
    } else if (result.dismiss === Swal.DismissReason.cancel) {
      // Aquí puedes agregar la lógica cuando el cliente selecciona "No"
      Swal.fire(
        'Operación cancelada',
        'No se ha enviado la boleta al correo electrónico.',
        'info'
      );
    }
  });
}