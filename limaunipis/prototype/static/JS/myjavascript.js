'use strict';

$(document).ready(function(){
	$(".item").click(function(){
		$(this).toggleClass("item2");
	});
});

// this is for star rating system using jquery prototype
// $.fn.stars = function() {
// 	return $(this).each(function() {

// 		var rating = $(this).data("rating");

// 		var numStars = $(this).data("num-stars");

// 		var fullStar = new Array(Math.floor(rating + 1)).join('<i class="fa fa-star"></i>');

// 		var halfStar = ((rating%1) !== 0) ? '<i class="fa fa-star-half-empty"></i>': '';

// 		var noStar = new Array(Math.floor(numStars + 1 - rating)).join('<i class="fa fa-star-o"></i>');

// 		$(this).html(fullStar + halfStar + noStar);

// 	});
// }

$.fn.stars = function() {
	return $(this).each(function() {

		var rating = $(this).data("rating");

		var numStars = $(this).data("num-stars");

		var fullStar = new Array(Math.floor(rating + 1)).join('<i class="fa fa-star"></i>');

		var halfStar = ((rating%1) !== 0) ? '<i class="fa fa-star-half-empty"></i>': '';

		var noStar = new Array(Math.floor(numStars + 1 - rating)).join('<i class="fa fa-star-o"></i>');

		$(this).html(fullStar + halfStar + noStar);

	});
};	


//  $('body').on('ready','.contentgroup',function(){
// 	 $('stars').stars(;)
//  });
