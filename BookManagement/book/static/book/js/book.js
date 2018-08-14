$(document).ready(function(){
        $.getJSON("/book/search/*/",function(data){
            $.each(data.request_result,function(i,item){
	        var tmp_tr=$('<tr></tr>');
                var tmp_td_book_id=$('<td></td>').text(item.book_id);
                var tmp_td_book_name=$('<td></td>').text(item.book_name);
                var tmp_td_book_author=$('<td></td>').text(item.book_author);
                var tmp_td_button=$('<td></td>');
                var tmp_button=$('<button type="button" onclick="deleteBook(this)" style="border-radius: 0px;" class="btn btn-default col-md-6" id="' + item.book_id +'">delete</button>');
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
    $.getJSON("/book/delete/" + element.id, function(data){
        alert(data.status);
    });
    element.parentNode.parentNode.remove();
}

function showForm(){
    var F = document.getElementById('create_form');
    F.style.display = 'block'
}
