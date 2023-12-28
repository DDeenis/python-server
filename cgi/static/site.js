function authClick() {
  const cred = btoa("user:password");
  fetch("/auth", {
    headers: {
      Authorization: `Basic ${cred}`,
    },
  })
    .then((r) => r.json())
    // .then((r) => r.text())
    // .then((r) =>
    //   JSON.parse(r, (key, val) => (key === "token" ? BigInt(val) : val))
    // )
    .then((r) => {
      console.log(r);
      localStorage.setItem("auth-token", r.data.token);
    })
    .catch((err) => console.error(err));
}

function infoClick() {
  fetch("/auth", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${localStorage.getItem("auth-token")}`,
    },
  })
    .then((r) => r.json())
    .then(console.log);
}

function publishClick() {
  fetch("/product", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${localStorage.getItem("auth-token")}`,
    },
    body: JSON.stringify({
      name: "Коробка 34x56",
      price: 29.5,
      image: "box3.jpg",
    }),
  })
    .then((r) => r.json())
    .then(console.log);
}

function getProductsClick() {
  fetch("/product")
    .then((r) => r.json())
    .then(console.log);
}
