$("#btnenviarL").click(function (e) {
    var erroresL = validarL();
    if (erroresL !== "") {
        Swal.fire("Error de envío", erroresL, "error");
    } else {
        Swal.fire("Datos Validos", "Bienvenido", "success")
            .then(function () {
                window.location.href = "/index/";

            });
    }
    e.preventDefault();
});

function validarL() {
    var htmlL = "";
    var nombreL = $("#txtUserName").val();
    var passwordL = $("#txtPassword").val();

    if (nombreL === "") {
        htmlL += "-Debe ingresar el nombre de usuario<br>";
    }

    if (passwordL === "") {
        htmlL += "-Debe ingresar la contraseña<br>";
    }  else if (!passwordL.match(/^[a-zA-Z0-9_-]{8,}$/)) {
        htmlL += "-La contraseña debe tener al menos 8 caracteres y solo debe contener letras, números, guiones bajos y guiones\n";
    }

    return htmlL;
}


$("#btnenviarLemp").click(function (e) {
    var errores = validarLemp();
    if (errores !== "") {
        Swal.fire("Error de envío", errores, "error");
    } else {
        Swal.fire("Datos Validos", "Bienvenido", "success")
            .then(function () {
                window.location.href = "/MenuEmpleados/";

            });
    }
    e.preventDefault();
});

function validarLemp() {
    var htmlL = "";
    var txtIdEmp = $("#txtIdEmp").val();
    var txtPasswordEmp = $("#txtPasswordEmp").val();

    if (txtIdEmp === "") {
        htmlL += "+Debe ingresar el nombre de usuario<br>";
    }

    if (txtPasswordEmp === "") {
        htmlL += "-Debe ingresar la contraseña<br>";
    } else if (!txtPasswordEmp.match(/^[a-zA-Z0-9_-]{8,}$/)) {
        htmlL += "-La contraseña debe tener al menos 8 caracteres y solo debe contener letras, números, guiones bajos y guiones\n";
    }

    return htmlL;
}


