/**
* @fileOverview Recovery Pod script.js file.
* @author <a href="https://github.com/aryan008">Adam Ryan</a>
* @version 1.1.1
*/
/*jshint esversion: 6 */

/* The below function adds the class of "active" to the current window location the site user is on */
// https://codepen.io/figarali/pen/araWdP
jQuery(function ($) {
    // find the window location the user is currently on
    let path = window.location.href;
    // for loop to apply a function to each "ul a" tag
    $('ul a').each(function () {
        if (this.href === path) {
            // add the class of active if this href is the window location
            $(this).addClass('active');
        }
    });
});

/* The below function applies the correct class to the score of the user for all entries */
$('.score-percentage').each(function() {
    let tableScore = $(this);
    // get the score of each entry
    let score = tableScore.text()
    // convert each score to numerical
    let numberScore = parseInt(score)
    
    // apply appropriate classes depending on the score
    if (numberScore >=70) {
        $(this).addClass( "recovered" );
    } else if (numberScore >= 50) {
        $(this).addClass( "moderate" );
    } else {
        $(this).addClass( "low" );
    }
}); 