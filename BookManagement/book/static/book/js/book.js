$(document).ready(function(){
        alert("hello!");
        $.getJSON("/book/search/*/",function(result){
            alert("hello2!")
        });
})


function showClassmates(result){
    $("#btn-group-vertical-classmates").empty();
    var chosen_list=new Array();
    
    $(".btn.btn-default.btn-class").filter(function(){
        judgeflag=false;
        if($(this).attr("chosen_state")=="1"){
            judgeflag=true;
            chosen_list.push($(this).text());
        }
        return judgeflag;                        
    });
    $.each(result,function(i,field){
        var chosen_list_x;
        for (chosen_list_x in chosen_list){
            if(chosen_list[chosen_list_x]==i){
                $.each(field,function(j,field2){
                    var tmp_button=$('<button type="button" style="border-radius: 0px;" class="btn btn-default btn-classmate btn-info" data-toggle="button" chosen_state=0></button>').text(j);
                    tmp_button.attr("title",j);
                    $("#btn-group-vertical-classmates").append(tmp_button);
                });
            }
        }
    });
}

function showClassmateDetail(result,selected_classmate){
    var classmate_context_item;
    $("#context_div").empty();
    $.each(result,function(i,field){
        $.each(field,function(j,field2){
            if(j==selected_classmate){
                $.each(field2,function(k,field3){
                    //alert(k);
                    //alert(field3);
                    classmate_context_item=k + ": " + field3;
                    var tmp_p=$('<p></p>').text(classmate_context_item);
                    $("#context_div").append(tmp_p);
                    });
            }
        });
    });
}
