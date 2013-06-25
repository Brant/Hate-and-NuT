$(function(){

	$(".sponsorship-ad-wrapper").each(function(){
		var adWrapper = $(this);
		
		var sponsorshipURL = adWrapper.data("sponsorship");
		$.get(sponsorshipURL, function(data){
			adWrapper.html(data);
		});
		
		adWrapper.delegate(".sponsorship-ad", "click", function(event){
			var thisAd = $(this);
			var linkURL = thisAd.data("sponsorship-ad-link");
			window.location = linkURL;
			
		});
	});

});