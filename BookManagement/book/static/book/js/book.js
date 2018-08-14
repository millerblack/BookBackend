$(document).ready(function(){
        $.getJSON("/book/search/*/",function(data){
            $.each(data.request_result,function(i,item){
	        var tmp_tr=$('<tr></tr>');
                var tmp_td_book_id=$('<td></td>').text(item.book_id);
                var tmp_td_book_name=$('<td></td>').text(item.book_name);
                var tmp_td_book_author=$('<td></td>').text(item.book_author);
                var tmp_td_button=$('<td></td>');
		var tmp_button=$('<button type="button" style="border-radius: 0px;" class="btn btn-default col-md-6" formmethod="post"><a href="/book/delete/' + item.book_id + '/">delete</a></button>');
		tmp_td_button.append(tmp_button)
		tmp_tr.append(tmp_td_book_id)
		tmp_tr.append(tmp_td_book_name)
		tmp_tr.append(tmp_td_book_author)
		tmp_tr.append(tmp_td_button)
                $("#book_table").append(tmp_tr);
	    });
        });
})


function deleteBook(element){
    alert(element.id)
    var tmp_button=$('<button type="button" onclick="deleteBook(this)" style="border-radius: 0px;" class="btn btn-default col-md-6" formmethod="post" formaction="book/delete/' + item.book_id +'">delete</button>');
}

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
