
Dropzone.options.myDropzone = {
    init: function () {
        this.on("success", function (file,response) {
            console.log(response);
        });
    }
};
function showLoader() {
   $(".loader_container").show(); 
   $(".loader_message").show(); 
}

function hideLoader() {
   $(".loader_container").hide(); 
   $(".loader_message").hide(); 
}

function checkResult(response, dropzone) {
	var probe_interval = setInterval(function() {
		$.ajax({
			url: '/deepdreamed',
			type: 'POST',
			data: {file: response},
			success: function(response) {
				if(response !== "pending") {
					clearInterval(probe_interval);
					$(".drop_container").append("<div><img class='deep_dreamed' src='"+response+"' /></div>");	
                    hideLoader();
                    if(dropzone.files.length > 0) {
                        dropzone.removeFile(dropzone.files[0]);
                    }
				}
			}			
		});	
	}, 30000);
} 
