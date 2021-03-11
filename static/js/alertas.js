function alertaConfirmar(url) {

   const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
      confirmButton: 'btn get-started-btn',
      cancelButton: 'btn btn-dark'
      },
      buttonsStyling: false
   })

   swalWithBootstrapButtons.fire({
      title: '¿Continuar?',
      text: "Esta acción no se puede deshacer",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonText: 'Si',
      cancelButtonText: 'No',
      reverseButtons: true
   }).then((result) => {
      if (result.isConfirmed) {
         window.location.pathname = url
         swalWithBootstrapButtons.fire({
            title: 'Borrado!',
            text: 'Tu registro ha sido borrado',
            icon: 'success',
            timer: 1000,
            showConfirmButton: false,
         })
      } else if (
         /* Read more about handling dismissals below */
         result.dismiss === Swal.DismissReason.cancel
         ) {
            swalWithBootstrapButtons.fire({
               title: 'Cancelado',
               text: 'Tu registro se encuentra a salvo :)',
               icon: 'error',
               timer: 1000,
               showConfirmButton: false,
            })
            }
         })
}
