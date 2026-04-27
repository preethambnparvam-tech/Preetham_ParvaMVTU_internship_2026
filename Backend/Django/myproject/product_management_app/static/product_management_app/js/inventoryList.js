const InventoryList = ({ products, loading, onEdit, onDelete }) => {
    return (
        <div className="col-12 mb-4">
            <div className="d-flex justify-content-between align-items-center mb-3">
                <h3 className="text-secondary fw-bold m-0">Inventory List</h3>
                <div className="badge bg-primary fs-6 rounded-pill px-3 py-2">{products.length} Items</div>
            </div>

            {loading && products.length === 0 ? (
                <div className="text-center py-5">
                    <div className="spinner-border text-primary" role="status">
                        <span className="visually-hidden">Loading...</span>
                    </div>
                    <p className="mt-2 text-secondary">Loading inventory...</p>
                </div>
            ) : products.length === 0 ? (
                <div className="text-center py-5 bg-white rounded shadow-sm border-0">
                    <h5 className="text-muted">No products found</h5>
                    <p className="text-sm text-secondary">Add some products using the form to get started.</p>
                </div>
            ) : (
                <div className="row row-cols-1 row-cols-md-2 g-4">
                    {products.map(product => (
                        <div key={product.id} className="col">
                            <div className="card h-100 shadow-sm border-0 product-card">
                                <div className="card-body">
                                    <div className="d-flex justify-content-between">
                                        <h5 className="card-title text-primary fw-bold text-truncate">{product.name}</h5>
                                        <span className="badge bg-success bg-opacity-10 text-success align-self-start py-2 px-2 ms-2 fs-6 border border-success border-opacity-25 rounded-3">
                                            ${parseFloat(product.price).toFixed(2)}
                                        </span>
                                    </div>
                                    <p className="card-text text-muted small mt-2 d-inline-block text-truncate w-100" style={{ maxHeight: '3rem', whiteSpace: 'normal', overflow: 'hidden' }}>{product.description || 'No description provided'}</p>
                                </div>
                                <div className="card-footer bg-white border-top border-light d-flex justify-content-between align-items-center py-3">
                                    <div>
                                        {product.stock > 0
                                            ? <span className="badge bg-info text-white rounded-pill px-2">In Stock: {product.stock}</span>
                                            : <span className="badge bg-danger rounded-pill px-2">Out of Stock</span>
                                        }
                                    </div>
                                    <div className="btn-group">
                                        <button className="btn btn-sm btn-outline-primary" onClick={() => onEdit(product)}>Edit</button>
                                        <button className="btn btn-sm btn-outline-danger" onClick={() => onDelete(product.id)}>Delete</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};
