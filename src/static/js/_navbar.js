var navbar_toggle_button = document.getElementById('navbar-toggle-button');
var navbar_close_icon = document.getElementById('navbar-close-icon');
var navbar_open_icon = document.getElementById('navbar-open-icon');
var navbar_nav = document.getElementById('navbar-nav');

navbar_toggle_button.onclick = function() {
  navbar_nav.classList.toggle('hidden');
  navbar_close_icon.classList.toggle('hidden');
  navbar_open_icon.classList.toggle('hidden');
};
