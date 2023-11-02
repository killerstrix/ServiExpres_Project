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