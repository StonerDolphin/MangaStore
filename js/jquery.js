$(document).ready(function() {
    $("#contactForm").submit(function(e) {
      e.preventDefault(); // Prevenimos el envío del formulario para validar primero
      var email = $("#emailInput").val();
      var comment = $("#commentInput").val();
      var isValid = true; // Bandera de validación
      if (!email) {
        $("#emailInput").addClass("is-invalid");
        $("#emailInputError").text("Debes ingresar un correo electrónico.");
        isValid = false;
      } else if (!/^\S+@\S+\.\S+$/.test(email)) {
        $("#emailInput").addClass("is-invalid");
        $("#emailInputError").text("Debes ingresar un correo electrónico válido.");
        isValid = false;
      } else {
        $("#emailInput").removeClass("is-invalid");
        $("#emailInputError").text("");
      }
      if (!comment) {
        $("#commentInput").addClass("is-invalid");
        $("#commentInputError").text("Debes ingresar tus comentarios.");
        isValid = false;
      } else {
        $("#commentInput").removeClass("is-invalid");
        $("#commentInputError").text("");
      }
      if (isValid) {
        // Si el formulario es válido, podemos enviarlo
        this.submit();
      }
    });
  });