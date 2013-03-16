$(function() {
    $('#action-toggle').change(function(e) {
        var checked = $(this).prop('checked');
        $('td.action-checkbox input[type=checkbox]').prop('checked', checked);
    });
});