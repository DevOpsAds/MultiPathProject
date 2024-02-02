

  let url = 'http://localhost:8000/address/filter_cep/?cep=30880-420'
  

  
 

  $(document).ready(function(){
    $('#id_cep').focus();
    //alert('em activid')
  })

  $('.cep').on('keypress', function(event) {
     let cep = $(this).val();
     



    //super
    let keyCode = event.which || event.KeyCode;
    console.log("tecla"+ event.which+ "minha url0 "+ url);
    if (keyCode === 13){

      let qtdeDeDigitosCep=cep.length
      if (qtdeDeDigitosCep < 9 && qtdeDeDigitosCep == 8) {
        cep = cep.slice(0,5)+ "-" + cep.slice(5);
        console.log("novo cep"+ cep);
      } else {
        alert('digitação errada')
      }
      let postData = $('form').serialize();
      let url = 'http://localhost:8000/address/filter_cep/?cep='+cep
      //alert('function acesso tecla enter'+url)

      $.ajax({
        type: 'GET',
        url:url,
        data:{
          data: postData,
        },
        success: function(response) {
         console.log('retorno em Json 76') 
         console.log(response.data)
         $('#id_endereco').val(response.data[0]);
         $('#id_bairro').val(response.data[1]);
         $('#id_cidade').val(response.data[2]);
         $('#id_uf').val(response.data[3]);
          
         
          // body...
        }
      });
    
    }
      if (keyCode === 44){
      event.preventDefault();
        $('#id_cep').val('');
        $('#id_cep').attr('placeholder','...insira o cep.');

    } 

  });


