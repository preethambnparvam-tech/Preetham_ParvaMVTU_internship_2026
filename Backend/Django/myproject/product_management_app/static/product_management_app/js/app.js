const { useState, useEffect } = React;
const API_URL = '/product-management/api/products/';

const App = () => {
    const [products, setProducts] = useState([]);
    const [formData, setFormData] = useState({ name: '', description: '', price: '', stock: '' });
    const [editingId, setEditingId] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    const [activeTab, setActiveTab] = useState('list');

    // Fetch products on load
    useEffect(() => {
        fetchProducts();
    }, []);

    const fetchProducts = async () => {
        setLoading(true);
        try {
            const response = await axios.get(API_URL);
            setProducts(response.data);
            setError('');
        } catch (err) {
            setError('Failed to fetch products');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        try {
            if (editingId) {
                // Update
                await axios.put(`${API_URL}${editingId}/`, formData);
            } else {
                // Create
                await axios.post(API_URL, formData);
            }
            setFormData({ name: '', description: '', price: '', stock: '' });
            setEditingId(null);
            setActiveTab('list');
            fetchProducts();
        } catch (err) {
            setError('Failed to save product');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleEdit = (product) => {
        setFormData({
            name: product.name,
            description: product.description,
            price: product.price,
            stock: product.stock
        });
        setEditingId(product.id);
        setActiveTab('form');
        window.scrollTo(0, 0);
    };

    const handleDelete = async (id) => {
        if (!window.confirm('Are you sure you want to delete this product?')) return;
        setLoading(true);
        try {
            await axios.delete(`${API_URL}${id}/`);
            fetchProducts();
        } catch (err) {
            setError('Failed to delete product');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleCancelEdit = () => {
        setFormData({ name: '', description: '', price: '', stock: '' });
        setEditingId(null);
        setActiveTab('list');
    };

    return (
        <div className="container py-5">
            <div className="row mb-4">
                <div className="col-12 text-center text-primary">
                    <h1 className="fw-bold">Product Management Dashboard</h1>
                    <p className="text-secondary">Manage your inventory with seamless CRUD operations</p>
                </div>
            </div>

            {error && (
                <div className="alert alert-danger" role="alert">
                    {error}
                </div>
            )}

            {/* Navigation Tabs */}
            <ul className="nav nav-pills mb-4 justify-content-center">
                <li className="nav-item">
                    <button
                        className={`nav-link ${activeTab === 'list' ? 'active fw-bold' : ''}`}
                        onClick={() => setActiveTab('list')}
                        style={{ cursor: 'pointer' }}
                    >
                        Inventory List
                    </button>
                </li>
                <li className="nav-item ms-2">
                    <button
                        className={`nav-link ${activeTab === 'form' ? 'active fw-bold' : ''}`}
                        onClick={() => setActiveTab('form')}
                        style={{ cursor: 'pointer' }}
                    >
                        {editingId ? 'Edit Product' : 'Add New Product'}
                    </button>
                </li>
            </ul>

            <div className="row justify-content-center">
                {activeTab === 'form' && (
                    <ProductForm
                        formData={formData}
                        handleInputChange={handleInputChange}
                        handleSubmit={handleSubmit}
                        editingId={editingId}
                        loading={loading}
                        handleCancelEdit={handleCancelEdit}
                    />
                )}

                {activeTab === 'list' && (
                    <InventoryList
                        products={products}
                        loading={loading}
                        onEdit={handleEdit}
                        onDelete={handleDelete}
                    />
                )}
            </div>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
