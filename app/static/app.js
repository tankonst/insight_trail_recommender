// we wrap module into a function call to isolate the scope from the global scope

$( "#autocomplete" ).autocomplete({
      source: '/autocomplete',
      minLength: 2,
    });
//
// return;
// (function(){
//   var autocomplete = $('#autocomplete');
//   var autocomplete_result = $('#autocomplete_result');
//
// function updPopup() {
//   if(!autocomplete.val()) {
//     popupClearAndHide();
//     return;
//   }
//
//   if(autocomplete.val() == autocomplete.data('searched')){
//     return;
//   }
//
//   autocomplete.data('searched', autocomplete.val());
//
//   $.get('/autocomplete?query='+encodeURIComponent(autocomplete.val()), function(response){
//       var data = JSON.parse(response);
//       autocomplete_result.html('');
//       $.each(data, function(index,trailName){
//          var element = $('<div></div>')
//          element.html(trailName)
//          element.addClass('autocomplete_item')
//          autocomplete_result.append(element).show()
//
//       });
//   })
//
// }
//
// function popupClearAndHide() {
//   autocomplete_result.text('').hide();
// }
//
// function selectItem(event){
//   $item = $(event.target);
//   autocomplete.val($item.html());
//   popupClearAndHide();
// }
//
// console.log(123);
//
// $('body').on("keyup",'#autocomplete', updPopup);
// $('body').on("change", '#autocomplete',updPopup);
// $('body').on("focus",'#autocomplete', updPopup);
//
// $('body').on("click",'.autocomplete_item', selectItem);
//
//
// })()
