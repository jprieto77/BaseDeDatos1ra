function editBranch(branchId) {
    window.location.href = `/sucursales/${branchId}/editar`;
}

function confirmDelete(branchId) {
    if (confirm("¿Estás seguro de que deseas eliminar esta sucursal?")) {
        // Lógica para eliminar la sucursal
        window.location.href = `/sucursales/${branchId}/eliminar`;
    }
}