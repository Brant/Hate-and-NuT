$(function(){

	var loadAds = function(){
		function pw_load(){
			if(arguments.callee.z)return;else arguments.callee.z=true;
			var d=document;var s=d.createElement('script');
			var x=d.getElementsByTagName('script')[0];
			s.type='text/javascript';s.async=true;
			s.src='//www.projectwonderful.com/pwa.js';
			x.parentNode.insertBefore(s,x);
		}
		if (window.attachEvent){
			window.attachEvent('DOMContentLoaded',pw_load);
			window.attachEvent('onload',pw_load);
		}
		else{
			window.addEventListener('DOMContentLoaded',pw_load,false);
			window.addEventListener('load',pw_load,false);
		}
	};

	var myViewport = $(window).width();

	if (myViewport >= 748){
		var aside = $('<aside class="banner-ad header-ad" />').prependTo("#pgHead");
		var adspace = $('<div id="pw_adbox_70365_5_0"></div>').appendTo(aside);
		var placeholder = $('<noscript><map name="admap70365" id="admap70365"><area href="http://www.projectwonderful.com/out_nojs.php?r=0&c=0&id=70365&type=5" shape="rect" coords="0,0,728,90" title=" alt=" target="_blank" /></map><table cellpadding="0" cellspacing="0" style="width:728px;border-style:none;background-color:#ffffff;"><tr><td><img src="http://www.projectwonderful.com/nojs.php?id=70365&type=5" style="width:728px;height:90px;border-style:none;" usemap="#admap70365" alt=" /></td></tr><tr><td style="background-color:#ffffff;" colspan="1"><center><a style="font-size:10px;color:#0000ff;text-decoration:none;line-height:1.2;font-weight:bold;font-family:Tahoma, verdana,arial,helvetica,sans-serif;text-transform: none;letter-spacing:normal;text-shadow:none;white-space:normal;word-spacing:normal;" href="http://www.projectwonderful.com/advertisehere.php?id=70365&type=5" target="_blank">Ads by Project Wonderful!  Your ad here, right now: $0</a></center></td></tr></table></noscript>').appendTo(aside);
	}


	if (!$('body').hasClass("nopg") || myViewport < 1024){
		if (!$("body").hasClass("non-comic")){
			var asideSmall = $('<aside class="in-content-ad-wrap" />');
			
			$(".comic-footer").wrapInner("<section id='comicFooterContent' class='comic-footer-content' />");
			var smallPlace = $("#comicFooterContent");
			asideSmall.insertBefore(smallPlace);

			var adspaceSmall = $('<div class="in-content-ad" id="pw_adbox_70377_6_0"></div>').appendTo(asideSmall);
			var placeholderSmall = $('<noscript><map name="admap70377" id="admap70377"><area href="http://www.projectwonderful.com/out_nojs.php?r=0&c=0&id=70377&type=6" shape="rect" coords="0,0,234,60" title="" alt="" target="_blank" /></map><table cellpadding="0" cellspacing="0" style="width:234px;border-style:none;background-color:#ffffff;"><tr><td><img src="http://www.projectwonderful.com/nojs.php?id=70377&type=6" style="width:234px;height:60px;border-style:none;" usemap="#admap70377" alt="" /></td></tr><tr><td style="background-color:#ffffff;" colspan="1"><center><a style="font-size:10px;color:#0000ff;text-decoration:none;line-height:1.2;font-weight:bold;font-family:Tahoma, verdana,arial,helvetica,sans-serif;text-transform: none;letter-spacing:normal;text-shadow:none;white-space:normal;word-spacing:normal;" href="http://www.projectwonderful.com/advertisehere.php?id=70377&type=6" target="_blank">Ads by Project Wonderful!  Your ad here, right now: $0</a></center></td></tr></table></noscript>').appendTo(asideSmall);
			/*
			var adspaceSmall = $('<div class="in-content-ad" id="pw_adbox_70765_7_0"></div>').appendTo(asideSmall);
			var placeholderSmall = $('<noscript><map name="admap70765" id="admap70765"><area href="http://www.projectwonderful.com/out_nojs.php?r=0&c=0&id=70765&type=7" shape="rect" coords="0,0,300,250" title="" alt="" target="_blank" /></map><table cellpadding="0" cellspacing="0" style="width:300px;border-style:none;background-color:#ffffff;"><tr><td><img src="http://www.projectwonderful.com/nojs.php?id=70765&type=7" style="width:300px;height:250px;border-style:none;" usemap="#admap70765" alt="" /></td></tr><tr><td style="background-color:#ffffff;" colspan="1"><center><a style="font-size:10px;color:#0000ff;text-decoration:none;line-height:1.2;font-weight:bold;font-family:Tahoma, verdana,arial,helvetica,sans-serif;text-transform: none;letter-spacing:normal;text-shadow:none;white-space:normal;word-spacing:normal;" href="http://www.projectwonderful.com/advertisehere.php?id=70765&type=7" target="_blank">Ads by Project Wonderful!  Your ad here, right now: $0</a></center></td></tr></table></noscript>').appendTo(asideSmall);
			*/
		}
	}
	


	if (myViewport >= 748 && !($("body").hasClass("single-row-comic-page")) && !$("body").hasClass("non-comic")){
		var asideRight = $('<aside class="side-banner-medium" />').appendTo("#pageSide");
		var adspaceRight = $('<div id="pw_adbox_70520_3_0"></div>').appendTo(asideRight);
		var placeholderRight = $('<noscript><map name="admap70520" id="admap70520"><area href="http://www.projectwonderful.com/out_nojs.php?r=0&c=0&id=70520&type=3" shape="rect" coords="0,0,160,600" title="" alt="" target="_blank" /></map><table cellpadding="0" cellspacing="0" style="width:160px;border-style:none;background-color:#ffffff;"><tr><td><img src="http://www.projectwonderful.com/nojs.php?id=70520&type=3" style="width:160px;height:600px;border-style:none;" usemap="#admap70520" alt="" /></td></tr><tr><td style="background-color:#ffffff;" colspan="1"><center><a style="font-size:10px;color:#0000ff;text-decoration:none;line-height:1.2;font-weight:bold;font-family:Tahoma, verdana,arial,helvetica,sans-serif;text-transform: none;letter-spacing:normal;text-shadow:none;white-space:normal;word-spacing:normal;" href="http://www.projectwonderful.com/advertisehere.php?id=70520&type=3" target="_blank">Ads by Project Wonderful!  Your ad here, right now: $0</a></center></td></tr></table></noscript>').appendTo(asideRight);
	}


	loadAds();
});
