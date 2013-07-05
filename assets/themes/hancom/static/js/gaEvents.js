/*
 * Google Analytics Events
 */
$(function(){
	var thisPath = (window.location.pathname + window.location.search);
	
	$(".sponsorship-ad-wrapper").delegate(".sponsorship-ad", "click", function(ev){
		var clicked = $(this);
		_gaq.push(['_trackEvent', 'Ad Click', clicked.data("data-sponsorship-ad-code"), thisPath]);
	});
	
	$(".comic-nav-list-item-left").click(function(){
		_gaq.push(['_trackEvent', 'Navigate', "Last Comic", thisPath]);
	});
	
	$(".comic-nav-list-item-right").click(function(){
		_gaq.push(['_trackEvent', 'Navigate', "Next Comic", thisPath]);
	});
	
	$(".pg-foot-wrap a").click(function(ev){
		ev.preventDefault();
		_gaq.push(['_trackEvent', 'Navigate', "Footer", $(ev.target).text()]);
	});
	
	$(".pg-head .donate-button").click(function(ev){
		_gaq.push(['_trackEvent', 'Navigate', "Header", "Donate"]);
	});
	
	$(".s .donate-button").click(function(ev){
		_gaq.push(['_trackEvent', 'Navigate', "Sidebar", "Donate"]);
	});
	
	$(".s .social .social-icon").click(function(ev){
		_gaq.push(['_trackEvent', 'Navigate', "Sidebar", $(ev.target).text()]);
	});
});
