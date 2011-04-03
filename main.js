function loadnightlies(data){
    console.log(data)
    $('footer').text("This was last updated at: " +  data['last-edit'])
    
}

$(document).ready(function(){
    $.getJSON("nightlies", loadnightlies)
})