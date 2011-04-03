function loadnightlies(data){
    console.log(data);
    $('footer').text("This was last updated at: " +  data['last-edit']);
    // var info = JSON.parse(data.responseText)
    // for (var i = 0; i < info.length; i++) {
    //     makeBox(info[i], )
    // };
    
};

$(document).ready(function(){
    $.getJSON("nightlies", loadnightlies)
});