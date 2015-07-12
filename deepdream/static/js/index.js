
Dropzone.options.myDropzone = {
init: function () {
    this.on("success", function (file,response) {
      });
  }
};

function checkResult(response) {
	var probe_interval = setInterval(function() {
		$.ajax({
			url: '/deepdreamed',
			type: 'POST',
			data: {file: response},
			success: function(response) {
				if(response !== "pending") {
					clearInterval(probe_interval);
					$(".dropzone").append("<img src='"+response+"' />");	
				}
			}			
		});	
	}, 30000);
} 
