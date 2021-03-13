function alertaConfirmar(url) {

   const swalWithBootstrapButtons = Swal.mixin({
      customClass: {
      confirmButton: 'btn get-started-btn',
      cancelButton: 'btn get-cancel-btn'
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


function alertaExito(mjs) {

   const Toast = Swal.mixin({
      toast: true,
      position: 'top',
      showConfirmButton: false,
      width: '100%',
      timer: 3000,
      timerProgressBar: true,
      didOpen: (toast) => {
         toast.addEventListener('mouseenter', Swal.stopTimer)
         toast.addEventListener('mouseleave', Swal.resumeTimer)
      }
   })
      Toast.fire({
         icon: 'success',
         text: mjs,
      })
    
}
