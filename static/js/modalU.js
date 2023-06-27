function showAlert(href) {
    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-success',
            cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
    });

    swalWithBootstrapButtons.fire({
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: '¡Sí, bórralo!',
        cancelButtonText: '¡No, cancela!',
        reverseButtons: true
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = href;
            swalWithBootstrapButtons.fire(
                '¡Eliminado!',
                'El usuario ha sido eliminado.',
                'success'
            );
        } else if (result.dismiss === Swal.DismissReason.cancel) {
            swalWithBootstrapButtons.fire(
                'Cancelado',
                'El usuario está a salvo :)',
                'error'
            );
        }
    });
}

// Adjuntar evento de clic al botón de eliminación
document.querySelectorAll('.btnEliminacion').forEach(function(el) {
    el.addEventListener('click', function(e) {
        e.preventDefault();
        showAlert(this.getAttribute('href'));
    });
});
