/*
 * Google Analytics Events
 */
$(function(){
	
	var pushAnalyticsEvent = function(cat, ev, label, val){
		if (typeof _gaq === 'undefined') {
			if(val){
				ga('send', 'event', cat, ev, label, val);	
			}
			else{
				ga('send', 'event', cat, ev, label);
			}
		}
		else{
			if (val){
				_gaq.push(['_trackEvent', cat, ev, label, val]);
			}
			else{
				_gaq.push(['_trackEvent', cat, ev, label]);	
			}
		}
	};
	
	var thisPath = (window.location.pathname + window.location.search);
	
	$(".sponsorship-ad-wrapper").each(function(){
		var adWrapper = $(this);
		adWrapper.delegate(".sponsorship-ad", "click", function(event){
			var clicked = $(this);
			pushAnalyticsEvent("Ad Click", clicked.data("sponsorship-ad-code"), thisPath);
		});
	});
	
	$(".comic-nav-list-item-left").click(function(){
		pushAnalyticsEvent("Navigate", "Last Comic", thisPath);
	});
	
	$(".comic-nav-list-item-right").click(function(){
		pushAnalyticsEvent("Navigate", "Next Comic", thisPath);
	});
	
	$(".pg-foot-wrap a").click(function(ev){
		pushAnalyticsEvent("Navigate", "Footer", $(ev.target).text());
	});
	
	$(".pg-head .donate-button").click(function(ev){
		pushAnalyticsEvent("Navigate", "Header", "Donate");
	});
	
	$(".s .donate-button").click(function(ev){
		pushAnalyticsEvent("Navigate", "Sidebar", "Donate");
	});
	
	$(".s .social .social-icon").click(function(ev){
		pushAnalyticsEvent("Navigate", "Sidebar", $(ev.target).text());
	});

	$(".story-arc-from-beginning a").click(function(ev){
		pushAnalyticsEvent("Navigate", "Beginning of Story Arc", $(this).text());
	});

	$(".continuation-of a").click(function(ev){
		pushAnalyticsEvent("Navigate", "Continuation of Strip", $(this).text());
	});
});
