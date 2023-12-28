import { createApp } from "https://unpkg.com/petite-vue?module";

function ProductsList(props) {
  return {
    $template: "#products-list-template",
    products: props.initialProducts ?? [],
    // fetchProducts() {
    //   fetch("/product")
    //     .then((r) => r.json())
    //     .then((r) => {
    //       if (r.meta.status === 200) {
    //         this.products = r.data;
    //       }
    //     });
    // },
    // mounted() {
    //   this.fetchProducts();
    // },
  };
}

function Product(props) {
  return {
    $template: "#product-template",
    product: props.product,
  };
}

createApp({
  ProductsList,
  Product,
}).mount();
