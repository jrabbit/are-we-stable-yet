function loadnightlies(data){
    console.log(data);
    $('#edited').text("This was last updated at: " +  data['last-edit'] );
    // var info = JSON.parse(data.responseText)
    // for (var i = 0; i < info.length; i++) {
    //     makeBox(info[i], )
    // };
    
};


$(document).ready(function(){
    $('#modal').hide()
    $.getJSON("nightlies", loadnightlies)
    $('.scroll-content-item').click(function() { 
        console.log(this);
        console.log(this.id);
        var rev = this.id;
        $('#modal').dialog({
            height:200, 
            modal:true,
            buttons: 
                {"Works For Me!": function(){
                    $(this).dialog("close");
                    $.get("/working/" + rev);
                    window.location.reload();
                    }, 
                "This is buggy!": function(){
                    $(this).dialog("close");
                    $.get("/broken/" + rev);
                    window.location.reload();
                    }
                }
            })
    });
});

