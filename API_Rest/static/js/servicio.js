function mostrarSelectorFechaHora(servicio) {
    var panelSelector = $('<div></div>');
    var datepicker = $('<input type="text" id="datepicker" placeholder="Selecciona una fecha">');
    
    panelSelector.append(datepicker);
    

    panelSelector.dialog({
        modal: true,
        title: 'Selecciona fecha y hora para ' + servicio,
        buttons: {
            "Confirmar": function () {
                var fechaSeleccionada = datepicker.datepicker('getDate');
               
                Swal.fire({
                    title: '¡Compra exitosa!',
                    html: `Has seleccionado:<br>Fecha: ${fechaSeleccionada}`,
                    icon: 'success',
                    customClass: {
                        popup: 'custom-popup-class',
                        title: 'custom-title-class',
                        htmlContainer: 'custom-html-container-class'
                    }
                });
                $(this).dialog("close");
            },
            "Cancelar": function () {
                $(this).dialog("close");
            }
        },
        close: function () {
            $(this).dialog('destroy').remove();
        }
    });

    datepicker.datepicker({
        minDate: 0,
        onSelect: function (dateText) {
            mostrarHorasDisponibles(servicio, dateText, timepicker);
        }
    });

    // Configura el selector de tiempo sin mostrarlo
    timepicker.timepicker({
        'minTime': '8:00am',
        'maxTime': '6:00pm',
        'showDuration': true,
        'timeFormat': 'h:i A',
        'step': 15,
        'forceRoundTime': true,
        'appendTo': 'body',
        'dynamic': false,
        'disableTextInput': true
    });
}


