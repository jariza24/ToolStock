$(function () {
    $('.edit').on('click', function () {
        $('#editarProducto').modal('show');
    });

    $('.delete').on('click', function () {
        $('#eliminarProducto').modal('show');
    });
})