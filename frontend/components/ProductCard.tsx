
import { Product } from "@/types/product";

function ProductCard({ product }: { product:Product }) {
    return (
        <div className="card w-full max-w-sm bg-base-100 shadow-xl">
            <figure>
                <img src={product.image_url} alt={product.name} className="h-48 w-full object-cover"/>
            </figure>
            <div className="card-body">
                <h2 className="card-title">{product.name}</h2>
                <p>{product.description}</p>
                <div className="text-sm text-gray-500">Vendor: {product.vendor}</div>
            </div>
        </div>
    );
}

export default ProductCard;