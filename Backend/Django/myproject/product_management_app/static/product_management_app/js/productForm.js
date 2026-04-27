const ProductForm = ({ formData, handleInputChange, handleSubmit, editingId, loading, handleCancelEdit }) => {
    return (
        <div className="col-md-8 col-lg-6 mb-4">
            <div className="card shadow-sm border-0">
                <div className="card-header bg-white border-bottom border-light">
                    <h4 className="mb-0 text-primary">{editingId ? 'Edit Product' : 'Add New Product'}</h4>
                </div>
                <div className="card-body">
                    <form onSubmit={handleSubmit}>
                        <div className="mb-3">
                            <label className="form-label fw-bold text-secondary">Product Name</label>
                            <input type="text" className="form-control bg-light" name="name" value={formData.name} onChange={handleInputChange} required />
                        </div>
                        <div className="mb-3">
                            <label className="form-label fw-bold text-secondary">Description</label>
                            <textarea className="form-control bg-light" name="description" value={formData.description} onChange={handleInputChange} rows="3"></textarea>
                        </div>
                        <div className="row">
                            <div className="col-md-6 mb-3">
                                <label className="form-label fw-bold text-secondary">Price ($)</label>
                                <input type="number" step="0.01" className="form-control bg-light" name="price" value={formData.price} onChange={handleInputChange} required />
                            </div>
                            <div className="col-md-6 mb-3">
                                <label className="form-label fw-bold text-secondary">Stock</label>
                                <input type="number" className="form-control bg-light" name="stock" value={formData.stock} onChange={handleInputChange} required />
                            </div>
                        </div>
                        <div className="d-grid gap-2">
                            <button type="submit" className={`btn ${editingId ? 'btn-warning text-white fw-bold' : 'btn-primary fw-bold'}`} disabled={loading}>
                                {loading ? 'Processing...' : (editingId ? 'Update Product' : 'Save Product')}
                            </button>
                            {editingId && (
                                <button type="button" className="btn btn-outline-secondary" onClick={handleCancelEdit}>
                                    Cancel Edit
                                </button>
                            )}
                        </div>
                    </form>
                </div>
            </div>
        </div>
    );
};
