$(document).ready(function() {
	$('#btn_new').on('click', function() {
		location.href = "{% url 'client.add' %}";
	});

	oTable = $("#client-datatable").dataTable({

		"sPaginationType" : "bootstrap",
		"aaSorting" : [ [ 1, "asc" ] ],
		"aoColumnDefs" : [ {
			"bSortable" : false,
			"aTargets" : [ 0, 5 ]
		} ],
		"oLanguage" : lang_datatable
	});

	$('#checkAll').on('change', function() {
		$('[id=client_id]').prop('checked', $(this).is(':checked'));
	});

	$('#btn_del').on('click', function() {

		if (confirm('Deseja realmente remover os itens selecionados ?')) {
			bindIds();
			$('#delete_form').submit();
		}
	});
});

function bindIds() {

	var ids = [];

	$('[id=client_id]').each(function() {
		ids.push($(this).val());
	});

	$('[name=ids]').val(ids);
}