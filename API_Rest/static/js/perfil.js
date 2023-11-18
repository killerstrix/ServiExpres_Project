const profileName = document.getElementById("profile-name");
        const profileAddress = document.getElementById("profile-address");
        const profileAge = document.getElementById("profile-age");
        const profileInfo = document.getElementById("profile-info");
        const editProfileButton = document.getElementById("edit-profile-button");

        let isEditMode = false;

        editProfileButton.addEventListener("click", () => {
            isEditMode = !isEditMode;

            if (isEditMode) {
                editProfileButton.innerText = "Save Profile";
                profileName.contentEditable = true;
                profileAddress.contentEditable = true;
                profileAge.contentEditable = true;
                profileInfo.contentEditable = true;
            } else {
                editProfileButton.innerText = "Edit Profile";
                profileName.contentEditable = false;
                profileAddress.contentEditable = false;
                profileAge.contentEditable = false;
                profileInfo.contentEditable = false;
            }
        });

        document.addEventListener('DOMContentLoaded', function() {
            // Supongamos que tienes un objeto de datos con las citas
            const citasData = [
                { id: 1, fecha: '2023-11-20', hora: '10:00 AM' },
                { id: 2, fecha: '2023-11-22', hora: '02:30 PM' },
                // Agrega más citas según tu estructura de datos
            ];
        
            // Obtén la lista de citas y el botón de cancelar
            const citasList = document.getElementById('citas-list');
            const cancelarCitaBtn = document.getElementById('cancelar-cita-btn');
        
            // Función para mostrar las citas
            function mostrarCitas() {
                // Limpia la lista antes de agregar las nuevas citas
                citasList.innerHTML = '';
        
                // Muestra las citas en la lista
                citasData.forEach(cita => {
                    const listItem = document.createElement('li');
                    listItem.classList.add('list-group-item');
                    listItem.innerHTML = `${cita.fecha} - ${cita.hora}`;
                    citasList.appendChild(listItem);
                });
        
                // Muestra el botón de cancelar solo si hay citas
                cancelarCitaBtn.style.display = citasData.length > 0 ? 'block' : 'none';
            }
        
            // Llama a la función para mostrar las citas al cargar la página
            mostrarCitas();
        
            // Evento para cancelar cita
            cancelarCitaBtn.addEventListener('click', function() {
                // Aquí puedes implementar la lógica para cancelar una cita
                // Puedes mostrar un cuadro de diálogo de confirmación antes de cancelar
                // y luego actualizar la lista de citas y esconder el botón de cancelar
                Swal.fire({
                    title: '¿Estás seguro de cancelar la cita?',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#d33',
                    cancelButtonColor: '#3085d6',
                    confirmButtonText: 'Sí, cancelar'
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Implementa aquí la lógica para cancelar la cita
                        // Por ejemplo, puedes hacer una solicitud al servidor para actualizar la base de datos
        
                        // Después de cancelar, actualiza la lista de citas
                        citasData.pop(); // Supongamos que estás cancelando la última cita, ajusta según tus necesidades
                        mostrarCitas();
        
                        // Muestra un mensaje de éxito
                        Swal.fire('Cita cancelada', '', 'success');
                    }
                });
            });
        });