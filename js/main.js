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
    // $.getJSON("nightlies", loadnightlies)
    $('.click-bind').click(function() { 
        console.log(this);
        console.log(this.id);
        var rev = this.id;
        $('#modal').dialog({
            height:170,
            width:300, 
            modal:true,
            buttons: 
                {"Works For Me!": function(){
                    $(this).dialog("close");
                    //Get may be a bug!
                    
                    $.get("/working/" + rev, function(data){
                        window.location.reload();
                    });
                    }, 
                "This is buggy!": function(){
                    $(this).dialog("close");
                    $.get("/broken/" + rev, function(data){
                        window.location.reload();
                    });
                    }
                }
            })
    });
});

