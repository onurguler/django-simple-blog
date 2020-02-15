var account_dropdown_button = document.getElementById('account_dropdown_button');
var account_dropdown_overlay = document.getElementById('account_dropdown_overlay');
var account_dropdown_menu = document.getElementById('account_dropdown_menu');

account_dropdown_button.onclick = function() {
  account_dropdown_overlay.classList.toggle('hidden');
  account_dropdown_menu.classList.toggle('hidden');
}

account_dropdown_overlay.onclick = function() {
  account_dropdown_overlay.classList.toggle('hidden');
  account_dropdown_menu.classList.toggle('hidden');
}
