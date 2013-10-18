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
		$(document).bind('keydown', 'a', function(){
			window.location = prevComicHref;
		});

		$(document).bind('keydown', 'j', function(){
			window.location = prevComicHref;
		});
	}

	if (nextComicHref){
		$(document).bind('keydown', 's', function(){
			window.location = nextComicHref;
		});
		$(document).bind('keydown', 'k', function(){
			window.location = nextComicHref;
		});
	}

	var randomLinks = $(".comic-nav-list-item-random a");
	if (randomLinks.length > 0){
		var chronology = randomLinks.first().data("currentchronology");
		$.get("/comic/random/?current_comic=" + chronology).done(function(data){
			randomLinks.attr("href", data.url);
		});
	}


	var nextLink = $("#nextComic");
	if (nextLink.length > 0){
		var nextHref = nextLink.attr("href");
		$("img.comic").wrap("<a href='" + nextHref + "' />");
	}

});
