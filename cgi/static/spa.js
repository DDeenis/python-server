import { createApp } from "https://unpkg.com/petite-vue?module";

function ProductsList(props) {
  return {
    $template: "#products-list-template",
    products: [],
    fetchProducts() {
      fetch("/product")
        .then((r) => r.json())
        .then((r) => {
          if (r.meta.status === 200) {
            this.products = r.data;
          }
        });
    },
    mounted() {
      this.fetchProducts();
    },
  };
}

function Product(props) {
  return {
    $template: "#product-template",
    product: props.product,
    addCartClick() {
      fetch("/cart", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("auth-token")}`,
        },
        body: JSON.stringify({
          productId: this.product.id,
          count: 1,
        }),
      })
        .then((r) => r.text())
        .then(console.log)
        .catch((err) => console.error(err));
    },
  };
}

createApp({
  ProductsList,
  Product,
}).mount();
