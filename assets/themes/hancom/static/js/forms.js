$(function(){
	
	var ajaxLoader;
	var container;
	
	if ($("[data-form]").length > 0){
		ajaxLoader = $("<img src='" + siteVars("img") + "ajax.gif' />").appendTo("body").hide();
	}
	
	$("[data-form]").delegate('input[type="submit"]', "click", function(ev){
		ev.preventDefault();
		var submitButton = $(this);
		var form = submitButton.parents("form");
		var url = form.attr("action");
		var data = form.serialize();
		
		form.wrap("<div />");
		var newContainer = form.parent();
		
		newContainer.height(form.height());
		ajaxLoader.appendTo(newContainer);
		ajaxLoader.show();
		form.remove();
		
		$.post(url, data, function(resp){
			container.html(resp);
		});
	});
	
	$("[data-form]").each(function(){
		container = $(this);
		$.get(container.data("form"), function(resp){
			container.html(resp);
		}); 
	});
});
