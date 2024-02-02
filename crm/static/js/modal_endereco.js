 // modal_endereco.js

 $(document).ready(function(){
   $('#myModal').modal('open');
   alert('hello world! activid');

    $('.containesr').on('click',function () {
       alert('hello world! activid');

      // body...
    })
   

  })
  $('#btn_endereco').on('click',function () {
    
    const template =  "{% include "./address_modal.html" %} "
  

    $('.container').html(template)

   
    
    });