/*
 * Google Analytics Events
 */
$(function(){
	var thisPath = (window.location.pathname + window.location.search);
	
	$(".sponsorship-ad-wrapper").delegate(".sponsorship-ad", "click", function(ev){
		var clicked = $(this);
		if (_gaq){
			_gaq.push(['_trackEvent', 'Ad Click', clicked.data("data-sponsorship-ad-code"), thisPath]);	
		}
		else{
			ga('send', 'event', 'Ad Click', clicked.data("data-sponsorship-ad-code"), thisPath);
		}
		
	});
	
	$(".comic-nav-list-item-left").click(function(){
		if (_gaq){
			_gaq.push(['_trackEvent', 'Navigate', "Last Comic", thisPath]);	
		}
		else{
			ga('send', 'event', 'Navigate', "Last Comic", thisPath);
		}
	});
	
	$(".comic-nav-list-item-right").click(function(){
		if (_gaq){
			_gaq.push(['_trackEvent', 'Navigate', "Next Comic", thisPath]);	
		}
		else{
			ga('send', 'event', 'Navigate', "Next Comic", thisPath);
		}
		
	});
	
	$(".pg-foot-wrap a").click(function(ev){
		ev.preventDefault();
		if (_gaq){
			_gaq.push(['_trackEvent', 'Navigate', "Footer", $(ev.target).text()]);	
		}
		else{
			ga('send', 'event', 'Navigate', "Footer", $(ev.target).text());
		}
	});
	
	$(".pg-head .donate-button").click(function(ev){
		if (_gaq){
			_gaq.push(['_trackEvent', 'Navigate', "Header", "Donate"]);	
		}
		else{
			ga('send', 'event', 'Navigate', "Header", "Donate");
		}
		
	});
	
	$(".s .donate-button").click(function(ev){
		if (_gaq){
			_gaq.push(['_trackEvent', 'Navigate', "Sidebar", "Donate"]);	
		}
		else{
			ga('send', 'event', 'Navigate', "Sidebar", "Donate");
		}
		
	});
	
	$(".s .social .social-icon").click(function(ev){
		if (_gaq){
			_gaq.push(['_trackEvent', 'Navigate', "Sidebar", $(ev.target).text()]);	
		}
		else{
			ga('send', 'event', 'Navigate', "Sidebar", $(ev.target).text());
		}
	});
});
