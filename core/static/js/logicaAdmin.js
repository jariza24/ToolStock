$(function () {
    $('.edit').on('click', function () {
        $('#editarProducto').modal('show');
    });

    $('.ver').on('click', function () {
        $('#verProducto').modal('show');
    });

    $('.delete').on('click', function () {
        $('#eliminarProducto').modal('show');
    });
})