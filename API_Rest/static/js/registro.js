$(document).ready(function () {
    $("#btnvolverlogin").click(function () {
        window.location.href = "/login/";
    });
});

$("#btnCrearCuenta").click(function (e) {
    var erroresR = validarR();
    if (erroresR !== "") {
        Swal.fire("Error de envío", erroresR, "error");
    } else {
        Swal.fire("Datos Validos", "Cuenta creada con exito", "success")
            .then(function () {
                window.location.href = "/login/";

            });
    }
    e.preventDefault();
});

function validarR() {
    var html = "";
    var UserName = $("#txtUserName").val();
    var Password = $("#txtPassword").val();
    var correo = $("#txtCorreoC").val();
    var NumTel = $("#txtNumberTelephone").val();
    var radioMasculino = document.querySelector("#rbtMasculino");
    var RadioFemenino = document.querySelector("#rbtFemenino");
    var RadioOtros = document.querySelector("#rbtOtros");
    var radio = document.querySelector("#ValTerms");

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
    }else if(correo === "" || correo.indexOf("@") === -1) {
        html += "-Debe ingresar el caracter '@' en el correo electronico<br>";
    }
    

    if (NumTel === "" || parseInt(NumTel) > 99999999 || parseInt(NumTel) < 10000000) {
        html += "-El número telefónico debe tener 8 o 9 dígitos<br>";
    }

    if (!radioMasculino.checked && !RadioFemenino.checked && !RadioOtros.checked) {
        html += "-Debe seleccionar un genero<br>";
    }

    if (!radio.checked) {
        html += "-Debe aceptar los términos y condiciones<br>";
    }

    return html;
}

$("#btnLogOut").click(function (e) {
    Swal.fire({
        title: 'Estas seguro de cerrar sesion?',
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: 'Cerrar Sesión',
        denyButtonText: `Continuar en la cuenta`,
      }).then((result) => {
        /* Read more about isConfirmed, isDenied below */
        if (result.isConfirmed) {
          Swal.fire('Selecciono cerrar sesión', 'Hasta luego!', 'success')
          .then(function () {
            window.location.href = "/login/";

        });
        } else if (result.isDenied) {
          Swal.fire('Selecciono no cerrar sesión', '', 'error')
        }
      })
});


