
function bindDataTableCheckAll(){
	$('#checkAll').on('change', function() {
		$('[id=id]').prop('checked', $(this).is(':checked'));
	});
}


function bindIdsToRemove() {

	$('[id=id]').each(function() {
		if($(this).is(':checked')){
			var inputIds = $('<input>').attr('name','ids');
			inputIds.val($(this).val());
			$('#delete_form').append(inputIds);
		}
	});
}