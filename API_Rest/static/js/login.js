
function validarLemp() {
    // Lógica de validación para el formulario de empleados
    var errores = "";

    var txtIdEmp = document.getElementById("txtIdEmp").value.trim();
    var txtPasswordEmp = document.getElementById("txtPasswordEmp").value.trim();

    if (txtIdEmp === "") {
        errores += "Ingrese la Id del empleado.\n";
    }

    if (txtPasswordEmp === "") {
        errores += "Ingrese la contraseña.\n";
    }

    return errores;
}

function validarcli() {
    // Lógica de validación para el formulario de empleados
    var errores = "";

    var txtIdEmp = document.getElementById("txtIdEmp").value.trim();
    var txtPasswordEmp = document.getElementById("txtPasswordEmp").value.trim();

    if (txtIdEmp === "") {
        errores += "Ingrese la Id del empleado.\n";
    }

    if (txtPasswordEmp === "") {
        errores += "Ingrese la contraseña.\n";
    }

    return errores;
}




