$(document).ready(function () {
    // Configura el evento "click" para el enlace con ID "btnLogOut"
    $("#btnCancelarCompra").click(function (e) {
        e.preventDefault(); // Previene el comportamiento predeterminado del enlace

        Swal.fire({
            title: '¿Estás seguro de cancelar la compra?',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: 'Cancelar Compra',
            denyButtonText: `Continuar compra`,
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire('Seleccionaste no cancelar la compra','', 'success')
                .then(function () {
                    window.location.href = "";
                });
            } else if (result.isDenied) {
                Swal.fire('Seleccionaste Cancelar Compra', '', 'error');
            }
        });
    });
});


  
  