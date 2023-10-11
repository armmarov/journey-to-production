var imgSrc = "";

function base64Url(file){
  return new Promise(function(resolve,reject){
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result) 
      reader.onerror = (error) => reject(error)
      reader.readAsDataURL(file);
  })
}

async function convertImgToBase64(file) {
  imgSrc = await base64Url(file);
  console.log(imgSrc)
}

async function predictImage() {
  $.ajax({
    url: '/yolo/predict',
    method: 'POST',
    dataType : "json",
    contentType: "application/json",
    data: JSON.stringify({
      img: imgSrc
    }),
    success: function(response) {
      console.log(response);
      $('#wizardPictureDetectPreview').attr('src', "data:image/jpeg;base64," + response[0].message).fadeIn('slow');
      // do something with the response data
    },
    error: function(jqXHR, textStatus, errorThrown) {
      console.log(errorThrown);
      // handle the error case
    }
  });
}