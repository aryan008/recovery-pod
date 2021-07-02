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