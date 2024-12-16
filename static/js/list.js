

    function editProduct(productId) {
        window.location.href = `/productos/${productId}/editar`;
    }

    function confirmDelete(productId) {
        if (confirm("¿Estás seguro de que deseas eliminar este producto?")) {
            // Lógica para eliminar el producto
            window.location.href = `/productos/${productId}/eliminar`;
        }
    }
