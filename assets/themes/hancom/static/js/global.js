$(function(){
	var nextComicHref, prevComicHref;
	
	var prevComic = $("#prevComic");
	var nextComic = $("#nextComic");
	
	if (nextComic.length > 0){
		nextComicHref = nextComic.attr("href");
	}
	if (prevComic.length > 0){
		prevComicHref = prevComic.attr("href");
	}
	
	if (prevComicHref){
		$(document).bind('keydown', 'k', function(){
			window.location = prevComicHref; 
		});
	}
	
	if (nextComicHref){
		$(document).bind('keydown', 'l', function(){
			window.location = nextComicHref; 
		});	
	}
	

});