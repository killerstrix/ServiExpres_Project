
$(document).ready(function () {
    $("#btnvolverlogin").click(function () {
        window.location.href = "/";
    });
});


$("#btnCrearCuenta").click(function (e) {
    var erroresR = validarR();
    if (erroresR !== "") {
        Swal.fire("Error de envío", erroresR, "error");
    } else {
        Swal.fire("Datos Validos", "Cuenta creada con exito", "success")
            .then(function () {
                window.location.href = "";

            });
    }
    e.preventDefault();
});

function validarR() {
    var html = "";
    var UserName = $("#txtUserName").val();
    var Password = $("#txtPassword").val();
    var correo = $("#txtCorreoC").val();
    var Edad = $("#txtAge").val();
    var Comuna = $("ComunaC").val();
    var NumTel = $("#txtNumberTelephone").val();
    var radioMasculino = document.querySelector("#rbtMasculino");
    var RadioFemenino = document.querySelector("#rbtFemenino");
    var RadioOtros = document.querySelector("#rbtOtros");
    var radio = document.querySelector("#ValTerms");
    var edadNumero = parseInt(Edad);
    if (UserName === "") {
        html += "-Debe ingresar el nombre de usuario<br>";
    } else if (!UserName.length > 7) {
        html += "-El nombre de usuario debe tener al menos 8 caracteres<br>";
    }

    if (Password === "") {
        html += "-Debe ingresar la contraseña<br>";
    }else if (!Password.match(/^[a-zA-Z0-9_-]{8,}$/)) {
        html += "-La contraseña debe tener al menos 8 caracteres y solo debe contener letras, números, guiones bajos y guiones<br>";
    }

    if (correo === "") {
        html += "-Debe ingresar el correo electrónico<br>";
    }else if(correo === ""  ||correo.indexOf("@") === -1) {
        html += "-Debe ingresar el caracter '@' en el correo electronico<br>";
    }

    if (edadNumero === "") {
        html += "-Debe ingresar la edad<br>"
    }else if(!edadNumero > 18) {
        html += "-Debe ser mayor de 18 años para acceder a la pagina<br>";
    }

    if(Comuna ==="0") {
        html += "-Debe seleccionar una comuna<br>"
    }


    if (!radioMasculino.checked && !RadioFemenino.checked && !RadioOtros.checked) {
        html += "-Debe seleccionar un genero<br>";
    }

    if (!radio.checked) {
        html += "-Debe aceptar los términos y condiciones<br>";
    }

    return html;
}

$(document).ready(function () {
    // Configura el evento "click" para el enlace con ID "btnLogOut"
    $("#btnLogOut").click(function (e) {
        e.preventDefault(); // Previene el comportamiento predeterminado del enlace

        Swal.fire({
            title: '¿Estás seguro de cerrar sesión?',
            showDenyButton: true,
            showCancelButton: true,
            confirmButtonText: 'Cerrar Sesión',
            denyButtonText: `Continuar en la cuenta`,
        }).then((result) => {
            if (result.isConfirmed) {
                Swal.fire('Seleccionaste cerrar sesión', 'Hasta luego!', 'success')
                .then(function () {
                    window.location.href = "/loginEmpleado/";
                });
            } else if (result.isDenied) {
                Swal.fire('Seleccionaste no cerrar sesión', '', 'error');
            }
        });
    });
});




