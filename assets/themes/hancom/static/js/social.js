$(function(){
	
	function fbGo(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id)) return;
		js = d.createElement(s); js.id = id;
		js.src = "//connect.facebook.net/en_US/all.js#xfbml=1&appId=495389753807975";
		fjs.parentNode.insertBefore(js, fjs);
	};
	
	if ($(".fb-like").length > 0){
		fbGo(document, 'script', 'facebook-jssdk');
	}
	
	
	function plusGo() {
		var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
		po.src = 'https://apis.google.com/js/plusone.js';
		var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
	}
	
	if ($(".g-plusone").length > 0){
		plusGo();
	}
	
	function twitterGo(d,s,id){
		var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';
		if(!d.getElementById(id)){
			js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';
			fjs.parentNode.insertBefore(js,fjs);
		}
	}
	
	if ($(".twitter-share-button").length > 0){
		twitterGo(document, 'script', 'twitter-wjs');
	}
	
});
