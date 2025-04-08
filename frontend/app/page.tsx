"use client";

import { useEffect, useState } from "react";
import axios from "axios";

import ProductCard from "@/components/ProductCard";
import { Product } from "@/types/product";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

export default function Home() {
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    axios
      .get<Product[]>(`${process.env.NEXT_PUBLIC_API_BASE_URL}/api/products/`)
      .then((res) => setProducts(res.data))
      .catch((err) => console.error("Error fetching products:", err));
  }, []);

  return (
    <>
      <Header />
      <main className="flex flex-col min-h-screen p-6 max-w-[1200px] mx-auto items-center">
        <section className="space-y-4">
          <h2 className="text-gray-500">Products</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {products.map((product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        </section>
      </main>
      <Footer />
    </>
  );
}
