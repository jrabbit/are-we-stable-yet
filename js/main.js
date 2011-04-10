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
    $('.hidden').hide()
    // $.getJSON("nightlies", loadnightlies)
    $('.click-bind').click(function() { 
        console.log(this);
        console.log(this.id);
        var rev = this.id;
        // $('#r41162').parent().children('.trac-url').text() = trac url
        if ($(this.id).parent().children('.trac-url').text() !== '—'){
            $('#modal').html("If this is a buggy nightly have you reported it on <a href='https://dev.haiku-os.org'>the bug tracker?</a>")
        }else{
            $('#modal').html("Did you report your findings to <a href='" +$(this.id).parent().children('.trac-url').text() + "'> the trac ticket? </a>" )
        };
            
        $('#modal').dialog({
            title:"Update the status of " + rev,
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

